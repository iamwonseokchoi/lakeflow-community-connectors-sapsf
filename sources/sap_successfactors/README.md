# Lakeflow SAP SuccessFactors Community Connector

This documentation provides setup instructions and reference information for the SAP SuccessFactors source connector.

The Lakeflow SAP SuccessFactors Connector allows you to extract data from your SAP SuccessFactors tenant and load it into Databricks. This connector supports incremental synchronization for ~690 entities across all major SAP SuccessFactors modules including Employee Central, Recruiting, Performance, Time & Attendance, and more.


## Prerequisites

- SAP SuccessFactors tenant with API access enabled
- API user account with OData API permissions
- Network connectivity from Databricks to your SAP SuccessFactors API endpoint

### Required Permissions

The API user must have the following permissions in SAP SuccessFactors:

- **OData API Access**: Enabled for all modules you wish to ingest
- **Read access**: To entities in Employee Central, Recruiting, Performance, Time, etc.
- **Admin Center access**: To retrieve company settings and configuration

To configure API permissions:
1. Log in to SAP SuccessFactors Admin Center
2. Navigate to **Manage Permission Roles**
3. Ensure the API user's role has OData API permissions for required entities


## Setup

### Required Connection Parameters

To configure the connector, provide the following parameters in your connector options:

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `api_server` | string | Yes | SAP SuccessFactors API server hostname (without https://) | `api8.successfactors.com` |
| `company_id` | string | Yes | Your company/tenant identifier | `MYCOMPANY` |
| `user_id` | string | Yes | API user ID with data read permissions | `apiuser` |
| `password` | string | Yes | API user password | `********` |
| `auth_type` | string | No | Authentication type (default: "basic") | `basic` |
| `page_size` | string | No | Records per page (default: "1000") | `1000` |

### Table-Specific Options

The following options can be passed via `table_options` in your pipeline_spec for advanced use cases:

| Option | Applicable To | Description |
|--------|---------------|-------------|
| `custom_filter` | OData v2/v4 entities | Custom OData $filter expression |
| `$select` | OData v2/v4 entities | Specify columns to retrieve |
| `$expand` | OData v2 entities only | Expand navigation properties |
| `userId` | TimeAccountBalance | User ID for balance query |
| `timeAccountType` | TimeAccountBalance | Time account type filter |
| `asOfDate` | TimeAccountBalance | As-of date for balance query |
| `page` | REST entities | Page number for pagination |
| `pageSize` | REST entities | Page size for pagination |

**Note:** To use these options, include them in the `externalOptionsAllowList` when creating your UC connection (see CLI example below).

> **Important - externalOptionsAllowList**: The allowlist must include:
> - **System options** (required by pipeline infrastructure): `tableName`, `tableNameList`, `tableConfigs`, `isDeleteFlow`
> - **Connector-specific options** (for advanced queries): `custom_filter`, `$select`, `$expand`, `userId`, `timeAccountType`, `asOfDate`, `page`, `pageSize`
>
> If using the community connector CLI tool (`tools/community_connector`), system options are added automatically.

### Finding Your API Server

Your SAP SuccessFactors API server depends on your data center location:

1. Log in to SAP SuccessFactors
2. Check the URL format: `https://{datacenter}.successfactors.com`
3. Use the corresponding API endpoint

**Common API Servers:**

| Region | Data Centers | API Server |
|--------|--------------|------------|
| Americas | DC2, DC4, DC8, DC10, DC12 | `api.successfactors.com`, `api2.successfactors.com`, `api8.successfactors.com` |
| Europe | DC5, DC15, DC16, DC17, DC18, DC19 | `api.successfactors.eu`, `api4.successfactors.eu` |
| Asia Pacific | DC20, DC22 | `api.sapsf.ap1.hana.ondemand.com` |
| Middle East | DC21 | `api.sapsf.uae1.hana.ondemand.com` |

### Getting Your Company ID

1. Log in to SAP SuccessFactors Admin Center
2. Navigate to **Company Settings** or **Company System and Logo Settings**
3. Find **Company ID** in the Company Information section

### Create a Unity Catalog Connection

A Unity Catalog connection for this connector can be created in two ways:

**Option 1: Via Databricks CLI**

```bash
databricks connections create --json '{
  "name": "sap_successfactors_connection",
  "connection_type": "GENERIC_LAKEFLOW_CONNECT",
  "options": {
    "sourceName": "sap_successfactors",
    "api_server": "api8.successfactors.com",
    "company_id": "YOUR_COMPANY_ID",
    "user_id": "YOUR_USER_ID",
    "password": "YOUR_PASSWORD",
    "externalOptionsAllowList": "tableName,tableNameList,tableConfigs,isDeleteFlow,custom_filter,$select,$expand,userId,timeAccountType,asOfDate,page,pageSize"
  }
}'
```

**Option 2: Via Lakeflow Community Connector UI**

1. Follow the Lakeflow Community Connector UI flow from the **Add Data** page
2. Select **SAP SuccessFactors** as the connector
3. Enter connection parameters as prompted

The connection can also be created using the standard Unity Catalog API.


## Supported Objects

The SAP SuccessFactors connector supports **~690 entities** across the following modules:

### Employee Central (~80 entities)

Core employee data including personal information, employment, job, and compensation records.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `User` | userId | lastModifiedDateTime | cdc |
| `EmpEmployment` | personIdExternal, userId | lastModifiedDateTime | cdc |
| `EmpJob` | seqNumber, startDate, userId | lastModifiedDateTime | cdc |
| `EmpCompensation` | seqNumber, startDate, userId | lastModifiedDateTime | cdc |
| `EmpPayCompRecurring` | seqNumber, startDate, userId | lastModifiedDateTime | cdc |
| `PerPerson` | personIdExternal | lastModifiedDateTime | cdc |
| `PerPersonal` | personIdExternal, startDate | lastModifiedDateTime | cdc |
| `PerEmail` | personIdExternal, emailType | lastModifiedDateTime | cdc |
| `PerPhone` | personIdExternal, phoneType | lastModifiedDateTime | cdc |
| `PerAddressDEFLT` | personIdExternal, addressType, startDate | lastModifiedDateTime | cdc |
| `EmpCostAssignment` | effectiveStartDate, worker | lastModifiedDateTime | cdc_with_deletes |
| `EmpEmploymentTermination` | personIdExternal, userId | lastModifiedDateTime | cdc |

### Foundation Objects (~25 entities)

Organizational structure and configuration data.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `FODepartment` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOCompany` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOCostCenter` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOJobCode` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOLocation` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOBusinessUnit` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FODivision` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOPayGrade` | externalCode, startDate | lastModifiedDateTime | cdc |
| `FOPayGroup` | externalCode, startDate | lastModifiedDateTime | cdc |
| `Position` | code | lastModifiedDateTime | cdc |

### Platform Services (~30 entities)

Workflow, picklists, and system configuration.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `PickList` | picklistId | lastModifiedDateTime | cdc |
| `PickListV2` | PickListV2_id | lastModifiedDateTime | cdc |
| `PicklistOption` | id | lastModifiedDateTime | cdc |
| `WfRequest` | wfRequestId | lastModifiedOn | cdc |
| `WfRequestStep` | wfRequestStepId | lastModifiedOn | cdc |
| `TodoEntryV3` | todoEntryId | lastModifiedDateTime | cdc |
| `Attachment` | attachmentId | lastModifiedDateTime | cdc |
| `Photo` | photoType, userId | lastModifiedDateTime | cdc |
| `DynamicGroup` | groupID | lastModifiedDateTime | cdc |
| `SecondaryAssignment` | effectiveStartDate, externalCode | lastModifiedDateTime | cdc_with_deletes |

### Recruiting (~50 entities)

Candidate, job requisition, and application data.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `Candidate` | candidateId | lastModifiedDateTime | cdc |
| `CandidateLight` | candidateId | lastModifiedDateTime | cdc |
| `JobApplication` | applicationId | lastModifiedDateTime | cdc |
| `JobRequisition` | jobReqId | lastModifiedDateTime | cdc_with_deletes |
| `JobRequisitionPosting` | jobPostingId | lastModifiedDateTime | cdc |
| `JobOffer` | offerApprovalId | lastModifiedDateTime | cdc |
| `OfferLetter` | offerApprovalId | lastModifiedDateTime | cdc |
| `JobApplicationInterview` | applicationInterviewId | lastModifiedDateTime | cdc |
| `InterviewOverallAssessment` | interviewOverallAssessmentId | lastModifiedDateTime | cdc |

### Performance & Goals (~100 entities)

Performance reviews, goals, and continuous performance management.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `Goal_1` to `Goal_8` | id | lastModified | cdc_with_deletes |
| `GoalTask_1` to `GoalTask_8` | id | lastModified | cdc |
| `FormHeader` | formDataId | lastModifiedDateTime | cdc |
| `FormContent` | formContentId | lastModifiedDateTime | cdc |
| `FormObjective` | formContentId, formDataId, itemId, sectionIndex | lastModifiedDateTime | cdc |
| `FormTemplate` | formTemplateId | lastModifiedDateTime | cdc |
| `Achievement` | achievementId | lastModifiedDateTime | cdc_with_deletes |
| `Activity` | activityId | lastModifiedDateTime | cdc_with_deletes |
| `Feedback` | feedbackId | lastModifiedDateTime | cdc_with_deletes |
| `CalibrationSession` | sessionId | lastModifiedDateTime | cdc |

### Time & Attendance (~40 entities)

Time tracking, leave management, and work schedules.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `TimeAccount` | externalCode | lastModifiedDateTime | cdc |
| `TimeAccountDetail` | TimeAccount_externalCode, externalCode | lastModifiedDateTime | cdc |
| `TimeAccountType` | externalCode | lastModifiedDateTime | cdc |
| `TimeType` | externalCode | lastModifiedDateTime | cdc |
| `EmployeeTime` | externalCode | lastModifiedDateTime | cdc_with_deletes |
| `EmployeeTimeSheet` | externalCode | lastModifiedDateTime | cdc |
| `EmployeeTimeSheetEntry` | EmployeeTimeSheet_externalCode, externalCode | lastModifiedDateTime | cdc |
| `WorkSchedule` | externalCode | lastModifiedDateTime | cdc |
| `WorkScheduleDay` | WorkSchedule_externalCode, day | lastModifiedDateTime | cdc |
| `HolidayCalendar` | externalCode | lastModifiedDateTime | cdc |
| `Holiday` | HolidayCalendar_externalCode, holidayDate | lastModifiedDateTime | cdc |

### Succession & Development (~50 entities)

Talent management, succession planning, and skills.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `TalentPool` | code | lastModifiedDateTime | cdc |
| `Successor` | id | lastModifiedDateTime | cdc |
| `NominationTarget` | nominationId | lastModifiedDateTime | cdc |
| `Competency` | competencyId | lastModifiedDateTime | cdc |
| `CompetencyEntity` | externalCode | lastModifiedDateTime | cdc |
| `JobProfile` | externalCode | lastModifiedDateTime | cdc |
| `SkillEntity` | externalCode | lastModifiedDateTime | cdc |
| `CertificationEntity` | externalCode | lastModifiedDateTime | cdc |
| `RightToReturn` | positionId, returnToWorkDate, userId | lastModifiedDateTime | cdc_with_deletes |

### Benefits (~60 entities)

Benefit plans, enrollment, and claims.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `BenefitEnrollment` | enrollmentId | lastModifiedDateTime | cdc |
| `BenefitProgram` | programId | lastModifiedDateTime | cdc |
| `BenefitInsurancePlan` | planId | lastModifiedDateTime | cdc |
| `BenefitInsuranceCoverage` | coverageId | lastModifiedDateTime | cdc |
| `BenefitSavingsPlan` | planId | lastModifiedDateTime | cdc |
| `BenefitPensionPlan` | planId | lastModifiedDateTime | cdc |
| `BenefitEmployeeClaim` | claimId | lastModifiedDateTime | cdc |

### Onboarding (~25 entities)

New hire onboarding processes and tasks.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `ONB2Process` | processId | lastModifiedDateTime | cdc |
| `ONB2ProcessTask` | processTaskId | lastModifiedDateTime | cdc |
| `ONB2OnboardeeDetails` | processId | lastModifiedDateTime | cdc |
| `ONB2OffboardeeDetails` | processId | lastModifiedDateTime | cdc |
| `ONB2Equipment` | externalCode | lastModifiedDateTime | cdc |
| `ComplianceProcess` | processId | lastModifiedDateTime | cdc |
| `ComplianceProcessTask` | processTaskId | lastModifiedDateTime | cdc |

### Finance & Operations (~20 entities)

General ledger, payroll, and legal entity configuration.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `GLAccountMapping` | externalCode | lastModifiedDateTime | cdc |
| `PayrollConfigurationCategory` | externalCode | lastModifiedDateTime | cdc |
| `PayrollSystemConfiguration` | externalCode | lastModifiedDateTime | cdc |
| `LegalEntityUSA` | LegalEntity_externalCode, externalCode | lastModifiedDateTime | cdc |
| `LegalEntityDEU` | LegalEntity_externalCode, externalCode | lastModifiedDateTime | cdc |
| `NonRecurringPayment` | externalCode | lastModifiedDateTime | cdc |
| `RecurringDeduction` | effectiveStartDate, userSysId | lastModifiedDateTime | cdc |

### SCIM Identity (5 entities)

Identity management via SCIM 2.0 protocol.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `ScimUser` | id | lastModified | cdc |
| `ScimGroup` | id | lastModified | cdc |
| `ScimSchema` | id | - | snapshot |
| `ScimResourceType` | id | - | snapshot |
| `ScimServiceProviderConfig` | id | - | snapshot |

### Learning (1 entity)

Learning history data.

| Entity | Primary Key(s) | Cursor Field | Ingestion Type |
|--------|---------------|--------------|----------------|
| `LearningHistoryData` | lmsId, userId | lastModifiedDateTime | cdc |

### Full Entity List

To see all supported entities programmatically:

```python
from sources.sap_successfactors.sap_successfactors import LakeflowConnect

# Total count
print(f"Total entities: {len(LakeflowConnect._ENTITY_REGISTRY)}")

# List by module
for module, tables in sorted(LakeflowConnect._MODULE_TABLES.items()):
    print(f"\n{module}: {len(tables)} entities")
    for table in sorted(tables)[:5]:
        print(f"  - {table}")
    if len(tables) > 5:
        print(f"  ... and {len(tables) - 5} more")
```


## Ingestion Types

| Type | Description | Delete Handling |
|------|-------------|-----------------|
| `cdc` | Change Data Capture with cursor-based incremental sync | No delete sync |
| `cdc_with_deletes` | CDC with soft-delete detection | Detects deleted records via `mdfSystemRecordStatus='D'` or entity-specific fields |
| `snapshot` | Full table refresh each sync | Full replace |
| `append` | Append-only (event logs) | No updates |

### Entities with Delete Synchronization

The following entities support `cdc_with_deletes` for tracking deleted records:

- **Goals**: `Goal_1` through `Goal_8`, `Goal_101`
- **Employee Central**: `EmpCostAssignment`, `SecondaryAssignment`
- **Time**: `EmployeeTime`
- **Performance**: `Achievement`, `Activity`, `Feedback`, `PMActivity`, `PMAchievement`
- **Recruiting**: `JobRequisition`
- **Succession**: `RightToReturn`
- **Finance**: `BudgetPeriodGO`, `FundCenterGO`, `GrantGO`


## Data Type Mapping

| SAP SuccessFactors Type | Databricks Type | Notes |
|------------------------|-----------------|-------|
| Edm.String | STRING | Text fields, IDs |
| Edm.Int32 | BIGINT | Numeric values (converted to avoid overflow) |
| Edm.Int64 | BIGINT | Large numeric values |
| Edm.Double | DOUBLE | Decimal values |
| Edm.Decimal | DOUBLE | Decimal values |
| Edm.Boolean | BOOLEAN | True/false |
| Edm.DateTime | STRING | ISO 8601 format, parse downstream |
| Edm.DateTimeOffset | STRING | ISO 8601 with timezone |
| Edm.Binary | STRING | Base64 encoded |
| Navigation (single) | STRING | Foreign key reference |
| Navigation (collection) | STRING | JSON array |


## How to Run

### Step 1: Clone/Copy the Source Connector Code

Follow the Lakeflow Community Connector UI, which will guide you through setting up a pipeline using the selected source connector code.

Alternatively, manually copy the connector files to your Databricks workspace:

```bash
# Using databricks CLI sync
databricks sync sources/sap_successfactors /Workspace/Users/you@example.com/sap_successfactors
```

### Step 2: Configure Your Pipeline

1. Update the `pipeline_spec` in `ingest.py` to include the tables you need.

2. The `pipeline_spec` structure:

```python
pipeline_spec = {
    "connection_name": "your_connection_name",  # Must match UC connection
    "objects": [
        {
            "table": {
                "source_table": "EntityName",       # SAP SF entity name
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",       # or SCD_TYPE_1, APPEND_ONLY
                    "primary_keys": '["key1", "key2"]',  # JSON array string
                    "sequence_by": "lastModifiedDateTime"  # Cursor field
                }
            }
        },
        # Add more tables...
    ]
}
```

### table_configuration Options

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| `scd_type` | string | Yes | `SCD_TYPE_1`, `SCD_TYPE_2`, or `APPEND_ONLY` |
| `primary_keys` | string | Yes | JSON array string of primary key columns |
| `sequence_by` | string | Yes | Cursor field name for ordering |

### SCD Type Selection Guide

| SCD Type | When to Use | Behavior |
|----------|-------------|----------|
| `SCD_TYPE_1` | Current state only needed | Overwrites records on update |
| `SCD_TYPE_2` | Historical tracking needed | Keeps history with start/end dates |
| `APPEND_ONLY` | Event/audit logs | Never updates, only appends |

**Recommendation**: Use `SCD_TYPE_2` for most HR entities to maintain audit history.

### Step 3: Run and Schedule the Pipeline

**Create Pipeline via CLI:**

```bash
databricks pipelines create --json '{
  "name": "sap_successfactors_pipeline",
  "catalog": "main",
  "schema": "sap_sf_data",
  "serverless": true,
  "continuous": false,
  "development": true,
  "libraries": [
    {"file": {"path": "/Workspace/Users/you@example.com/sap_successfactors/ingest.py"}}
  ]
}'
```

**Start Pipeline:**

```bash
# Get pipeline ID from create output
databricks pipelines start-update "<pipeline_id>"

# For full refresh (re-ingest all data)
databricks pipelines start-update "<pipeline_id>" --full-refresh
```


## Pipeline Configuration Examples

### Example 1: Core HR Data

Essential employee and employment data:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {"table": {"source_table": "User", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["userId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "EmpEmployment", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["personIdExternal", "userId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "EmpJob", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["seqNumber", "startDate", "userId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "EmpCompensation", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["seqNumber", "startDate", "userId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "PerPerson", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["personIdExternal"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "PerPersonal", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["personIdExternal", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
    ]
}
```

### Example 2: Organizational Structure

Foundation objects for org hierarchy:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {"table": {"source_table": "FOCompany", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FODepartment", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FOCostCenter", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FOLocation", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FOJobCode", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FOPayGrade", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode", "startDate"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "Position", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["code"]', "sequence_by": "lastModifiedDateTime"}}},
    ]
}
```

### Example 3: Recruiting Pipeline

Candidate and job application data:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {"table": {"source_table": "Candidate", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["candidateId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "JobRequisition", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["jobReqId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "JobApplication", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["applicationId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "JobOffer", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["offerApprovalId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "JobApplicationInterview", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["applicationInterviewId"]', "sequence_by": "lastModifiedDateTime"}}},
    ]
}
```

### Example 4: Time & Attendance

Time tracking and leave data:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {"table": {"source_table": "TimeAccount", "table_configuration": {"scd_type": "SCD_TYPE_1", "primary_keys": '["externalCode"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "EmployeeTime", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "EmployeeTimeSheet", "table_configuration": {"scd_type": "SCD_TYPE_1", "primary_keys": '["externalCode"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "WorkSchedule", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "HolidayCalendar", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["externalCode"]', "sequence_by": "lastModifiedDateTime"}}},
    ]
}
```

### Example 5: Performance & Goals

Performance management data:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {"table": {"source_table": "Goal_1", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["id"]', "sequence_by": "lastModified"}}},
        {"table": {"source_table": "FormHeader", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["formDataId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "FormContent", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["formContentId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "Achievement", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["achievementId"]', "sequence_by": "lastModifiedDateTime"}}},
        {"table": {"source_table": "Feedback", "table_configuration": {"scd_type": "SCD_TYPE_2", "primary_keys": '["feedbackId"]', "sequence_by": "lastModifiedDateTime"}}},
    ]
}
```

### Example 6: Using table_options for Advanced Filtering

Use `table_options` to apply custom OData filters or select specific columns:

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        {
            "table": {
                "source_table": "User",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["userId"]',
                    "sequence_by": "lastModifiedDateTime"
                },
                "table_options": {
                    "custom_filter": "status eq 'active'",
                    "$select": "userId,firstName,lastName,email,department"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpJob",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                },
                "table_options": {
                    "custom_filter": "emplStatus eq 'A'",
                    "$expand": "userNav"
                }
            }
        },
    ]
}
```

**Note:** Ensure `externalOptionsAllowList` includes the options you want to use when creating your UC connection.


## Best Practices

- **Start Small**: Begin with 5-10 core entities (e.g., User, EmpJob, FODepartment) to validate connectivity and configuration
- **Use Incremental Sync**: All `cdc` entities support incremental reads via cursor field to minimize API calls
- **Monitor Rate Limits**: SAP SuccessFactors has API rate limits; the connector automatically retries on 429 errors with exponential backoff
- **Test in Development**: Use `development: true` in pipeline config for faster iteration and debugging
- **Schedule Appropriately**: For large tenants, schedule during off-peak hours to minimize impact on SAP SF performance
- **Handle 403/404 Gracefully**: Not all entities may be available in your tenant; the connector handles these gracefully


## Troubleshooting

### Common Issues

**401 Unauthorized**
- Verify the username format is `user_id` (not `user_id@company_id`) in the connection parameters
- Confirm the password is correct
- Check if the API user account is active and not locked

**403 Forbidden**
- The API user lacks OData API permissions for the requested entity
- Verify permissions in Admin Center > Manage Permission Roles
- Some entities require specific module licenses

**404 Not Found**
- The entity may not be available in your tenant configuration
- Check if the module is enabled and configured
- The entity name is case-sensitive

**429 Rate Limited**
- The connector automatically retries with exponential backoff
- Consider reducing the number of concurrent tables in a single pipeline run
- Schedule pipelines during off-peak hours

**Schema Mismatch**
- Entity schemas can vary by tenant configuration and customizations
- The connector uses dynamic schema inference to handle this
- If issues persist, check for custom fields in Admin Center

### Debug Steps

1. **Verify Connection**: Test with a simple entity like `User`
2. **Check Permissions**: Ensure the API user has OData API access
3. **Review Logs**: Pipeline logs contain detailed error messages
4. **Test API Directly**: Use Postman or curl to verify API access:

```bash
curl -X GET "https://api8.successfactors.com/odata/v2/User?\$top=1" \
  -H "Authorization: Basic $(echo -n 'user_id@company_id:password' | base64)" \
  -H "Accept: application/json"
```


## References

- [SAP SuccessFactors API Documentation](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM)
- [OData API Reference](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/6de35b8efd244dd7b7789e4c2f4dc53c.html)
- [SAP SuccessFactors Data Dictionary](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/c7f3e4c0e7d9452a9ac61e9b3b5b87c4/3d3f4c0e7d9452a9ac61e9b3b5b87c4.html)
- [SAP API Business Hub](https://api.sap.com/products/SAPSuccessFactors/overview)
- [Lakeflow Community Connectors Repository](../../prompts/README.md)
