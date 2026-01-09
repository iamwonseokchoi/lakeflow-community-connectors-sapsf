from pipeline.ingestion_pipeline import ingest
from libs.source_loader import get_register_function

# =============================================================================
# SAP SuccessFactors Connector Pipeline Configuration
# =============================================================================

# Source configuration
source_name = "sap_successfactors"
connection_name = "sap_successfactors_connection"  # Must match your UC connection

# =============================================================================
# Pipeline Specification
#
# This defines which tables to ingest and how to handle them.
# Modify the "objects" list to include tables you need.
#
# For full list of ~690 entities, see README.md or run:
#   from sources.sap_successfactors.sap_successfactors import LakeflowConnect
#   print(LakeflowConnect._ENTITY_REGISTRY.keys())
#
# table_configuration options:
#   - scd_type: SCD_TYPE_1 (overwrite), SCD_TYPE_2 (history), APPEND_ONLY
#   - primary_keys: JSON array string, e.g., '["userId"]' or '["key1", "key2"]'
#   - sequence_by: Cursor field for ordering (usually lastModifiedDateTime)
# =============================================================================

pipeline_spec = {
    "connection_name": connection_name,
    "objects": [
        # =====================================================================
        # Employee Central Core - Essential employee data
        # =====================================================================
        {
            "table": {
                "source_table": "User",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpEmployment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
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
                }
            }
        },
        {
            "table": {
                "source_table": "PerPerson",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerPersonal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        # =====================================================================
        # Foundation Objects - Organizational structure
        # =====================================================================
        {
            "table": {
                "source_table": "FODepartment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOCompany",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOCostCenter",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOLocation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        # =====================================================================
        # Time & Attendance
        # =====================================================================
        {
            "table": {
                "source_table": "TimeAccount",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
    ]
}

# =============================================================================
# Pipeline Execution
# =============================================================================

# Register source and run ingestion
register_lakeflow_source = get_register_function(source_name)
register_lakeflow_source(spark)
ingest(spark, pipeline_spec)
