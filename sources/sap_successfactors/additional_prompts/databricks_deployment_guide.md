# Databricks Deployment Guide for Lakeflow Community Connectors

This guide provides detailed instructions for deploying Lakeflow Community Connectors to Databricks, with specific focus on Unity Catalog connection creation, DLT pipeline configuration, and laptop-based development workflows. It supplements the main development prompts (Steps 1-7) with deployment-specific guidance.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Unity Catalog Connection Setup](#unity-catalog-connection-setup)
4. [DLT Pipeline Configuration](#dlt-pipeline-configuration)
5. [Deployment Workflow](#deployment-workflow)
6. [Testing and Validation](#testing-and-validation)
7. [Configuration Management](#configuration-management)
8. [Troubleshooting](#troubleshooting)
9. [Quick Reference](#quick-reference)

---

## Overview

### Purpose
This guide fills deployment gaps in the connector development workflow:
- **Step 6 (Documentation)** references Unity Catalog connections but lacks implementation details
- **Step 7 (Connector Spec)** defines parameters but doesn't explain how they're used in Databricks
- No existing guide covers the laptop-to-Databricks development iteration cycle

### When to Use This Guide
- After completing connector implementation (Step 2)
- Before or during testing (Step 3)
- When creating user-facing documentation (Step 6)
- For debugging deployment issues

### Development Workflow Philosophy
Traditional workflows (git commit → push → workspace pull → test) are too slow for AI-assisted development. This guide uses **direct file uploads** via `databricks sync` for fast iteration:
- Changes are live in seconds, not minutes
- Works seamlessly with AI coding assistants
- Immediate feedback without git operations
- Commit to git only when ready for production

---

## Prerequisites

### 1. Databricks CLI Installation

```bash
# Install Databricks CLI (latest version)
pip install databricks-cli

# Or using Homebrew on macOS
brew tap databricks/tap
brew install databricks

# Verify installation
databricks --version
```

### 2. Authentication Setup

```bash
# Configure authentication (interactive)
databricks configure

# Or set environment variables
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"

# Verify authentication
databricks current-user me
```

### 3. Required Permissions

| Permission | Purpose |
|------------|---------|
| `USE CATALOG` on target catalog | Access catalog for tables |
| `USE SCHEMA` on target schema | Access schema for tables |
| `CREATE TABLE` on target schema | Create destination tables |
| `CREATE CONNECTION` | Create Unity Catalog connections |
| `CAN_MANAGE` on compute | Run DLT pipelines |
| Workspace folder write access | Upload connector files |

### 4. Workspace Environment Setup

```bash
# Get current user info
USER_NAME=$(databricks current-user me --output json | jq -r '.userName')
WORKSPACE_URL=$(databricks auth env --output json | jq -r '.env.DATABRICKS_HOST')

# Create target schema if needed (replace 'main' with your catalog)
SCHEMA_NAME="sap_successfactors_data"
databricks schemas create "$SCHEMA_NAME" main --comment "SAP SuccessFactors connector data"
```

---

## Unity Catalog Connection Setup

### Connection Type
All Lakeflow Community Connectors use the `GENERIC_LAKEFLOW_CONNECT` connection type. This is a special Unity Catalog connection type that:
- Stores connector credentials securely
- Passes connection options to the connector at runtime
- Supports table-specific options via `externalOptionsAllowList`

### Connection Parameters Structure

```json
{
  "name": "connection_name",
  "connection_type": "GENERIC_LAKEFLOW_CONNECT",
  "options": {
    "sourceName": "sap_successfactors",
    "param1": "value1",
    "param2": "value2",
    "externalOptionsAllowList": "option1,option2"
  }
}
```

**Key Fields:**
| Field | Description |
|-------|-------------|
| `sourceName` | Must match the connector directory name (e.g., `sap_successfactors`) |
| `externalOptionsAllowList` | Comma-separated list of table-specific options allowed to pass through |
| Other options | Connector-specific authentication and configuration parameters |

### Creating Connection via Databricks CLI

```bash
# Set source name
SOURCE_NAME="sap_successfactors"
CONNECTION_NAME="${SOURCE_NAME}_connection"

# Create connection with your connector's specific parameters
# Replace the options with your connector's actual parameters from connector_spec.yaml
databricks connections create \
  --json '{
    "name": "'$CONNECTION_NAME'",
    "connection_type": "GENERIC_LAKEFLOW_CONNECT",
    "options": {
      "sourceName": "'$SOURCE_NAME'",
      "api_url": "https://api.successfactors.com",
      "company_id": "YOUR_COMPANY_ID",
      "username": "YOUR_USERNAME",
      "api_key": "YOUR_API_KEY",
      "externalOptionsAllowList": "start_date,end_date,entity_type"
    }
  }'
```

### Connection Options from connector_spec.yaml

The connection options come from your `connector_spec.yaml` file:

```yaml
# Example connector_spec.yaml structure
connection:
  parameters:
    - name: api_url
      type: string
      required: true
      description: SAP SuccessFactors API endpoint URL

    - name: company_id
      type: string
      required: true
      description: Your SAP SuccessFactors company ID

    - name: username
      type: string
      required: true
      description: API username with data read permissions

    - name: api_key
      type: string
      required: true
      description: API key for authentication

external_options_allowlist: "start_date,end_date,entity_type"
```

### Understanding externalOptionsAllowList

The `externalOptionsAllowList` enables table-specific configuration options:

**Without allowlist** - Only connection-level options are available:
```python
# Connector receives only connection options
options = {"api_url": "...", "company_id": "...", ...}
```

**With allowlist** - Table-specific options can be passed:
```python
# In pipeline spec
{
  "table": {
    "source_table": "employees",
    "table_configuration": {
      "start_date": "2024-01-01",  # Allowed via externalOptionsAllowList
      "end_date": "2024-12-31"
    }
  }
}

# Connector receives merged options
table_options = {"start_date": "2024-01-01", "end_date": "2024-12-31"}
```

### Validating Connection Creation

```bash
# List connections to verify
databricks connections list --output json | jq '.[] | select(.name == "'$CONNECTION_NAME'")'

# Get connection details
databricks connections get "$CONNECTION_NAME"

# Test connection (if connector supports it)
# Note: Full validation requires running the pipeline
```

### Updating Connection Options

```bash
# Update connection with new options
databricks connections update "$CONNECTION_NAME" \
  --json '{
    "options": {
      "sourceName": "'$SOURCE_NAME'",
      "api_url": "https://new-api.successfactors.com",
      "company_id": "NEW_COMPANY_ID",
      "username": "new_username",
      "api_key": "new_api_key",
      "externalOptionsAllowList": "start_date,end_date,entity_type,custom_filter"
    }
  }'
```

### Deleting Connection

```bash
# Delete connection (required before recreation)
databricks connections delete "$CONNECTION_NAME"
```

---

## DLT Pipeline Configuration

### Pipeline Architecture

A DLT pipeline for Lakeflow connectors consists of:

1. **Pipeline Definition** - Created via API/CLI with configuration
2. **ingest.py** - Entry point that defines tables to ingest
3. **Connector Code** - Generated merged Python source file
4. **Supporting Libraries** - libs/ and pipeline/ directories

### Pipeline Configuration Parameters

There are two types of configuration:

#### 1. Spark Configuration (Pipeline-Level)
Set in DLT pipeline `configuration` section, accessed via `spark.conf.get()`:

```python
# These are set in pipeline creation JSON
"configuration": {
  "source_name": "sap_successfactors",
  "num_tables": "5",           # Read by ingest.py for table discovery
  "default_page_size": "1000"  # Connector-specific default
}

# Accessed in ingest.py
source_name = spark.conf.get("source_name")
num_tables = spark.conf.get("num_tables", "1")
```

#### 2. Table Configuration (Per-Table)
Set in pipeline_spec within ingest.py:

```python
pipeline_spec = {
  "connection_name": "sap_successfactors_connection",
  "objects": [
    {
      "table": {
        "source_table": "employees",
        "table_configuration": {
          "scd_type": "SCD_TYPE_2",
          "primary_keys": '["employee_id"]',
          "sequence_by": "last_modified_date",
          "start_date": "2024-01-01"  # Table-specific option
        }
      }
    }
  ]
}
```

### Table Configuration Special Keys

| Key | Purpose | Values |
|-----|---------|--------|
| `scd_type` | Change tracking strategy | `SCD_TYPE_1` (overwrite), `SCD_TYPE_2` (history), `APPEND_ONLY` |
| `primary_keys` | Override connector defaults | JSON array string: `'["id"]'` or `'["id1", "id2"]'` |
| `sequence_by` | Cursor field for ordering | Column name string |
| Other keys | Passed to connector as `table_options` | Connector-specific |

### Creating Pipeline via CLI

```bash
# Helper function to create pipeline
createpipeline() {
  local SOURCE_NAME="sap_successfactors"
  local CONNECTION_NAME="${SOURCE_NAME}_connection"

  # Get user info
  USER_NAME=$(databricks current-user me --output json | jq -r '.userName')
  WORKSPACE_URL=$(databricks auth env --output json | jq -r '.env.DATABRICKS_HOST')

  # Set paths
  WORKSPACE_PATH="/Workspace/Users/$USER_NAME"
  PROJECT_NAME="${SOURCE_NAME}"
  PROJECT_PATH="$WORKSPACE_PATH/$PROJECT_NAME"

  # Pipeline name (sanitized)
  PIPELINE_NAME="$(echo $USER_NAME | cut -d'@' -f1 | tr '.' '_')_${SOURCE_NAME}"

  # Check if pipeline exists and delete it
  PIPELINE_ID=$(databricks pipelines list-pipelines \
    --filter "name LIKE '$PIPELINE_NAME'" \
    --output json | jq -r '.[0].pipeline_id // empty')

  if [ -n "$PIPELINE_ID" ]; then
    echo "Deleting existing pipeline: $PIPELINE_ID"
    databricks pipelines delete "$PIPELINE_ID"
    sleep 5
  fi

  # Create schema if it doesn't exist
  if ! databricks schemas get "main.${PIPELINE_NAME}" &>/dev/null; then
    echo "Creating schema: main.${PIPELINE_NAME}"
    databricks schemas create "${PIPELINE_NAME}" main
  fi

  # Create new pipeline
  databricks pipelines create \
    --json '{
      "name": "'$PIPELINE_NAME'",
      "catalog": "main",
      "schema": "'${PIPELINE_NAME}'",
      "configuration": {
        "source_name": "'$SOURCE_NAME'"
      },
      "serverless": true,
      "continuous": false,
      "development": true,
      "libraries": [
        {
          "file": {
            "path": "'$PROJECT_PATH'/ingest.py"
          }
        }
      ]
    }' | tee /tmp/$PIPELINE_NAME.json

  # Extract pipeline ID
  PIPELINE_ID=$(cat /tmp/$PIPELINE_NAME.json | jq -r '.pipeline_id')

  echo ""
  echo "Pipeline created with ID: $PIPELINE_ID"
  echo "View pipeline at: $WORKSPACE_URL/pipelines/$PIPELINE_ID"
}
```

### Pipeline Configuration Options

```json
{
  "name": "pipeline_name",
  "catalog": "main",
  "schema": "target_schema",
  "configuration": {
    "source_name": "sap_successfactors",
    "custom_config": "value"
  },
  "serverless": true,
  "continuous": false,
  "development": true,
  "libraries": [
    {
      "file": {
        "path": "/Workspace/Users/.../ingest.py"
      }
    }
  ]
}
```

| Option | Description | Recommended |
|--------|-------------|-------------|
| `serverless` | Use serverless compute | `true` for development |
| `continuous` | Run continuously vs triggered | `false` for testing |
| `development` | Development mode (no production checkpoints) | `true` during dev |
| `channel` | Feature channel | `"PREVIEW"` for latest features |

---

## Deployment Workflow

### Directory Structure for Deployment

```
sources/{source_name}/
├── {source_name}.py                           # Your connector implementation
├── _generated_{source_name}_python_source.py  # Generated merged file
├── __init__.py                                # Package init
├── connector_spec.yaml                        # Connection parameters
├── ingest.py                                  # Pipeline entry point
├── README.md                                  # User documentation
├── test/
│   └── test_{source_name}_lakeflow_connect.py
└── configs/
    └── dev_config.json                        # Dev credentials (git-ignored)
```

### Step 1: Generate Merged Source File

```bash
# From repository root
SOURCE_NAME="sap_successfactors"

# Generate the merged source file
python tools/scripts/merge_python_source.py $SOURCE_NAME

# Verify output
ls -la sources/$SOURCE_NAME/_generated_${SOURCE_NAME}_python_source.py
```

### Step 2: Upload Files to Workspace

```bash
# Helper function for file upload
copydir() {
  trap 'trap - ERR; return 1' ERR
  set -e

  SOURCE_NAME="sap_successfactors"

  # Get user info
  USER_NAME=$(databricks current-user me --output json | jq -r '.userName')
  WORKSPACE_URL=$(databricks auth env --output json | jq -r '.env.DATABRICKS_HOST')

  # Set paths
  WORKSPACE_PATH="/Workspace/Users/$USER_NAME"
  PROJECT_NAME="${SOURCE_NAME}"
  PROJECT_PATH="$WORKSPACE_PATH/$PROJECT_NAME"

  # Generate the merged source file
  python tools/scripts/merge_python_source.py $SOURCE_NAME

  # Create temp directory with only required files
  TEMP_DIR=$(mktemp -d)
  mkdir -p "$TEMP_DIR/libs" "$TEMP_DIR/sources/$SOURCE_NAME" "$TEMP_DIR/pipeline"

  # Copy required files
  cp -v libs/source_loader.py libs/spec_parser.py libs/utils.py "$TEMP_DIR/libs/"
  cp -v sources/$SOURCE_NAME/__init__.py "$TEMP_DIR/sources/$SOURCE_NAME/"
  cp -v sources/$SOURCE_NAME/_generated_${SOURCE_NAME}_python_source.py "$TEMP_DIR/sources/$SOURCE_NAME/"
  cp -v pipeline/ingestion_pipeline.py "$TEMP_DIR/pipeline/"

  # Copy ingest.py and original connector (needed for list_tables())
  cp -v sources/$SOURCE_NAME/ingest.py "$TEMP_DIR/ingest.py"
  cp -v sources/$SOURCE_NAME/${SOURCE_NAME}.py "$TEMP_DIR/sources/$SOURCE_NAME/"

  # Sync to Databricks workspace
  databricks sync "$TEMP_DIR" "$PROJECT_PATH"

  # Cleanup
  rm -rf "$TEMP_DIR"

  echo "Files uploaded to: $WORKSPACE_URL$PROJECT_PATH"
  set +e
}

# Execute upload
copydir
```

### Step 3: Create ingest.py

Create `sources/{source_name}/ingest.py`:

```python
from pipeline.ingestion_pipeline import ingest
from libs.source_loader import get_register_function

# Source configuration
source_name = "sap_successfactors"
connection_name = "sap_successfactors_connection"

# Pipeline specification
pipeline_spec = {
    "connection_name": connection_name,
    "objects": [
        {
            "table": {
                "source_table": "employees",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["employee_id"]',
                    "sequence_by": "last_modified_date"
                }
            }
        },
        {
            "table": {
                "source_table": "job_info",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["job_info_id"]'
                }
            }
        }
    ]
}

# Register source and run ingestion
register_lakeflow_source = get_register_function(source_name)
register_lakeflow_source(spark)
ingest(spark, pipeline_spec)
```

### Step 4: Create and Run Pipeline

```bash
# Create pipeline
createpipeline

# Start the pipeline
databricks pipelines start-update "$PIPELINE_ID"

echo "Pipeline started. Monitor at: $WORKSPACE_URL/pipelines/$PIPELINE_ID"
```

### Iterative Development Cycle

```
┌─────────────────────────────────────────────────────────────┐
│  1. Edit connector code locally                              │
│     └── sources/sap_successfactors/sap_successfactors.py    │
│                                                              │
│  2. Run copydir to upload changes                            │
│     └── Generates merged file and syncs to workspace        │
│                                                              │
│  3. Start pipeline update                                    │
│     └── databricks pipelines start-update "$PIPELINE_ID"    │
│                                                              │
│  4. Monitor and debug                                        │
│     └── Check pipeline UI or logs for errors                │
│                                                              │
│  5. Repeat until working                                     │
│                                                              │
│  6. Commit to git when ready                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Testing and Validation

### Starting Pipeline

```bash
# Start pipeline with incremental update
databricks pipelines start-update "$PIPELINE_ID"

# Start with full refresh (re-ingest all data)
databricks pipelines start-update "$PIPELINE_ID" --full-refresh
```

### Monitoring Pipeline Status

```bash
# Get pipeline status
databricks pipelines get "$PIPELINE_ID" --output json | jq -r '.state'

# Get latest update status
databricks pipelines get "$PIPELINE_ID" --output json | jq '.latest_updates[0]'

# Watch pipeline events (useful for debugging)
databricks pipelines list-pipeline-events "$PIPELINE_ID" --output json | jq '.[0:5]'
```

### Validating Data Ingestion

```sql
-- In Databricks SQL or notebook
-- Check table exists and has data
SELECT COUNT(*) FROM main.{schema_name}.employees;

-- Check recent records
SELECT * FROM main.{schema_name}.employees
ORDER BY _ingest_timestamp DESC
LIMIT 10;

-- Check SCD Type 2 history (if enabled)
SELECT * FROM main.{schema_name}.employees
WHERE employee_id = 'EMP001'
ORDER BY __START_AT;
```

### Verifying Incremental Sync

```bash
# Run first sync
databricks pipelines start-update "$PIPELINE_ID"

# Wait for completion, then run again
databricks pipelines start-update "$PIPELINE_ID"

# Check that only new/changed records were processed
# (Look at pipeline metrics in UI)
```

---

## Configuration Management

### Updating Pipeline Configuration

```bash
# Get current pipeline spec
CURRENT_SPEC=$(databricks pipelines get "$PIPELINE_ID" --output json | jq '.spec')

# Update configuration while preserving other settings
UPDATED_SPEC=$(echo "$CURRENT_SPEC" | jq '.configuration.new_param = "new_value"')

# Apply update
databricks pipelines update "$PIPELINE_ID" --json "$UPDATED_SPEC"

# Verify update
databricks pipelines get "$PIPELINE_ID" --output json | jq '.spec.configuration'
```

### Adding New Tables

1. Update `ingest.py` with new table configuration
2. Run `copydir` to upload changes
3. Start pipeline update (no need to recreate pipeline)

```python
# Add to pipeline_spec["objects"]
{
    "table": {
        "source_table": "new_table_name",
        "table_configuration": {
            "scd_type": "SCD_TYPE_1",
            "primary_keys": '["id"]'
        }
    }
}
```

### Changing SCD Type

```bash
# Update table configuration in ingest.py
# Change from SCD_TYPE_1 to SCD_TYPE_2

# Upload changes
copydir

# Full refresh required for SCD type changes
databricks pipelines start-update "$PIPELINE_ID" --full-refresh
```

---

## Troubleshooting

### Common Issues

#### 1. Import Errors
**Symptom**: `ModuleNotFoundError: No module named 'sources.sap_successfactors'`

**Solution**: Ensure all required files are uploaded:
```bash
# Verify file structure in workspace
databricks workspace ls "$PROJECT_PATH" --long
databricks workspace ls "$PROJECT_PATH/sources/$SOURCE_NAME" --long
databricks workspace ls "$PROJECT_PATH/libs" --long
```

#### 2. Connection Not Found
**Symptom**: `Connection 'xxx_connection' not found`

**Solution**: Verify connection exists and name matches:
```bash
# List all connections
databricks connections list

# Check exact connection name
databricks connections get "$CONNECTION_NAME"
```

#### 3. Permission Denied
**Symptom**: `User does not have permission to CREATE TABLE`

**Solution**: Grant necessary permissions:
```sql
-- Grant schema access
GRANT USE SCHEMA ON SCHEMA main.{schema_name} TO `user@example.com`;
GRANT CREATE TABLE ON SCHEMA main.{schema_name} TO `user@example.com`;
```

#### 4. Schema Mismatch
**Symptom**: `AnalysisException: cannot resolve column`

**Solution**:
- Verify schema returned by `get_table_schema()` matches actual data
- Check for case sensitivity issues in column names
- Run full refresh after schema changes

#### 5. Offset/Incremental Issues
**Symptom**: Data not updating or duplicates appearing

**Solution**:
- Verify `read_table_metadata()` returns correct `cursor_field`
- Check offset handling in `read_table()`
- Run full refresh to reset state

#### 6. Rate Limiting
**Symptom**: API errors with 429 status code

**Solution**:
- Implement backoff in connector code
- Reduce batch size via table configuration
- Add delay between API calls

### Debugging Commands

```bash
# View pipeline logs
databricks pipelines list-pipeline-events "$PIPELINE_ID" --output json | \
  jq '.[] | select(.level == "ERROR") | {timestamp, message}'

# Get detailed error from latest update
databricks pipelines get "$PIPELINE_ID" --output json | \
  jq '.latest_updates[0].state_update_message'

# Check cluster logs (for serverless pipelines)
# Go to pipeline UI → Cluster → Driver Logs
```

### Reset and Cleanup

```bash
# Delete pipeline and recreate
databricks pipelines delete "$PIPELINE_ID"
createpipeline

# Drop and recreate destination tables (use with caution)
# In Databricks SQL:
# DROP SCHEMA main.{schema_name} CASCADE;
# CREATE SCHEMA main.{schema_name};

# Reset checkpoints (force full refresh)
databricks pipelines start-update "$PIPELINE_ID" --full-refresh
```

---

## Quick Reference

### Shell Functions Template

Add these to your `.bashrc` or `.zshrc`:

```bash
# Set connector variables
export SOURCE_NAME="sap_successfactors"
export CONNECTION_NAME="${SOURCE_NAME}_connection"

# Get user context
get_user_context() {
  USER_NAME=$(databricks current-user me --output json | jq -r '.userName')
  WORKSPACE_URL=$(databricks auth env --output json | jq -r '.env.DATABRICKS_HOST')
  WORKSPACE_PATH="/Workspace/Users/$USER_NAME"
  PROJECT_PATH="$WORKSPACE_PATH/$SOURCE_NAME"
  PIPELINE_NAME="$(echo $USER_NAME | cut -d'@' -f1 | tr '.' '_')_${SOURCE_NAME}"
  export USER_NAME WORKSPACE_URL WORKSPACE_PATH PROJECT_PATH PIPELINE_NAME
}

# Upload files
copydir() {
  get_user_context
  # ... (full implementation above)
}

# Create pipeline
createpipeline() {
  get_user_context
  # ... (full implementation above)
}

# Start pipeline
startpipeline() {
  get_user_context
  PIPELINE_ID=$(databricks pipelines list-pipelines \
    --filter "name LIKE '$PIPELINE_NAME'" \
    --output json | jq -r '.[0].pipeline_id')
  databricks pipelines start-update "$PIPELINE_ID" "$@"
  echo "Monitor at: $WORKSPACE_URL/pipelines/$PIPELINE_ID"
}

# Get pipeline status
pipelinestatus() {
  get_user_context
  PIPELINE_ID=$(databricks pipelines list-pipelines \
    --filter "name LIKE '$PIPELINE_NAME'" \
    --output json | jq -r '.[0].pipeline_id')
  databricks pipelines get "$PIPELINE_ID" --output json | jq '{state, latest_update: .latest_updates[0]}'
}
```

### Common CLI Commands

```bash
# Connection management
databricks connections list
databricks connections create --json '{...}'
databricks connections get <name>
databricks connections delete <name>

# Pipeline management
databricks pipelines list-pipelines --filter "name LIKE 'pattern'"
databricks pipelines create --json '{...}'
databricks pipelines get <id>
databricks pipelines update <id> --json '{...}'
databricks pipelines delete <id>
databricks pipelines start-update <id> [--full-refresh]
databricks pipelines list-pipeline-events <id>

# Workspace operations
databricks workspace ls <path>
databricks sync <local-path> <workspace-path>

# Schema management
databricks schemas list <catalog>
databricks schemas create <schema> <catalog>
databricks schemas get <catalog>.<schema>
```

### Configuration Checklist

Before deploying a new connector:

- [ ] Connector implementation complete (`{source_name}.py`)
- [ ] All `LakeflowConnect` methods implemented
- [ ] `connector_spec.yaml` created with all parameters
- [ ] `__init__.py` exists in source directory
- [ ] `ingest.py` created with pipeline spec
- [ ] Merged source generated via `merge_python_source.py`
- [ ] Unity Catalog connection created
- [ ] Destination schema created
- [ ] Files uploaded to workspace
- [ ] Pipeline created and started
- [ ] Data verified in destination tables

### Ingestion Type Reference

| Type | Use Case | Offset Tracking | Delete Handling |
|------|----------|-----------------|-----------------|
| `cdc` | Records with update timestamps | Cursor field (timestamp) | No |
| `cdc_with_deletes` | CDC + explicit deletes | Cursor field + delete cursor | `read_table_deletes()` |
| `snapshot` | Full table refreshes | None | Full replace |
| `append` | Append-only logs | Cursor field or page | No |

### SCD Type Reference

| Type | Behavior | Use Case |
|------|----------|----------|
| `SCD_TYPE_1` | Overwrite on update | Current state only |
| `SCD_TYPE_2` | Track history with start/end dates | Historical tracking |
| `APPEND_ONLY` | Never update, only append | Event logs |
