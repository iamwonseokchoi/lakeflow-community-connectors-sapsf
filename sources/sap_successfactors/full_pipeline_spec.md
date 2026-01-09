# SAP SuccessFactors - Complete Pipeline Specification

## Overview

- **Total entities**: 690
- **Organized by**: Module/functional area
- **Generated from**: `_ENTITY_REGISTRY` in `sap_successfactors.py`

## Usage

Copy the entire `pipeline_spec` below or select specific modules/entities as needed.
Modify `connection_name` to match your Unity Catalog connection.

## Pipeline Specification

```python
pipeline_spec = {
    "connection_name": "sap_successfactors_connection",
    "objects": [
        # =================================================================
        # Module: employee_central (111 entities)
        # =================================================================
        {
            "table": {
                "source_table": "Bank",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BankBranch",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Currency",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CustomPayType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CustomPayTypeAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpCompensation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpCostAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["effectiveStartDate", "worker"]',
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
                "source_table": "EmpEmploymentTermination",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpGlobalAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
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
                "source_table": "EmpJobRelationships",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpPayCompNonRecurring",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpPayCompRecurring",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpWorkPermit",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["seqNumber", "startDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOBusinessUnit",
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
                "source_table": "FOCorporateAddressDEFLT",
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
                "source_table": "FODivision",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOEventReason",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOFrequency",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOGeozoneMapping",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOGlobalOrganization",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOJobClassLocalDEFLT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOJobCode",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOJobFunction",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOLegalEntityLocalDEFLT",
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
        {
            "table": {
                "source_table": "FOPayComponent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOPayComponentGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOPayGrade",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOPayGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOPayRange",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOPayrollEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FOWfConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountry",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryAUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryBRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryCAN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryFRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryGBR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryITA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryUSA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationCountryZAF",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["JobClassificationCountry_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobClassificationMethod",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PayCalendar",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PayPeriod",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationV3_effectiveStartDate", "PaymentInformationV3_worker", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3ARG",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3AUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3AUT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3BEL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3BLR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3BOL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3BRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3CAN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3CHE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3CHL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3CHN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3COL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3CZE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3DEU",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3DNK",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3EGY",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3ESP",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3FIN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3FRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3GBR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3GRC",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3HKG",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3HUN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3IDN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3IND",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3IRL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3ISR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3ITA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3JPN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3KOR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3MEX",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3MYS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3NLD",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3NOR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3NZL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3PHL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3POL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3PRT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3RUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3SAU",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3SGP",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3SVK",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3SVN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3SWE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3THA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3TUN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3TUR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3TWN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3USA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3VEN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationDetailV3ZAF",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate", "PaymentInformationDetailV3_PaymentInformationV3_worker", "PaymentInformationDetailV3_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PaymentInformationV3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerAddressDEFLT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "addressType", "startDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerEmail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "emailType"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerEmergencyContacts",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "name"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerNationalId",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "country", "cardType"]',
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
        {
            "table": {
                "source_table": "PerPhone",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personIdExternal", "phoneType"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Position",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["code"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
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

        # =================================================================
        # Module: platform (56 entities)
        # =================================================================
        {
            "table": {
                "source_table": "Attachment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["attachmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CompanyProvisioner",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Country",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["code"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CurrencyConversion",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["fromCurrency", "toCurrency", "effectiveDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGExpression",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["expressionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGField",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["fieldId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGFieldOperator",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["operatorId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGFieldValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["fieldId", "valueId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGFilter",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["filterId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DGPeoplePool",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["poolId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DynamicGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["groupID"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DynamicGroupBean",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["beanID"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DynamicGroupDefinition",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["groupId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EMEvent",
                "table_configuration": {
                    "scd_type": "APPEND_ONLY",
                    "primary_keys": '["id"]',
                    "sequence_by": "eventTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EMEventAttribute",
                "table_configuration": {
                    "scd_type": "APPEND_ONLY",
                    "primary_keys": '["eventId", "attributeId"]',
                    "sequence_by": "eventTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EMEventPayload",
                "table_configuration": {
                    "scd_type": "APPEND_ONLY",
                    "primary_keys": '["eventId", "payloadId"]',
                    "sequence_by": "eventTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EMMonitoredProcess",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processDefinitionId", "processInstanceId", "processType"]',
                    "sequence_by": "lastEventTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExtAddressInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["addressId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExtEmailInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["emailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExtPersonalInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["personalInfoId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExtPhoneInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["phoneId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalLearner",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalLearnerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalLearnerAddressInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ExternalLearner_externalLearnerId", "itemId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalLearnerEmailInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ExternalLearner_externalLearnerId", "itemId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalLearnerPersonalInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ExternalLearner_externalLearnerId", "itemId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalLearnerPhoneInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ExternalLearner_externalLearnerId", "itemId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExternalUser",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalUserId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "InitiativeAlignmentBean",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["initiativeId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "MDFEnumValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "mdfSystemEffectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "MDFLocalizedValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "locale"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "MessageDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["code"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Photo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["photoType", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PickList",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["picklistId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PickListV2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["PickListV2_id"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PicklistLabel",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["locale", "optionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PicklistOption",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RBPBasicPermission",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["permissionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RBPRole",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RBPRule",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ruleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SecondaryAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["effectiveStartDate", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SecondaryAssignmentsItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["SecondaryAssignment_effectiveStartDate", "SecondaryAssignment_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SuccessStoreContentBlob",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["contentId", "blobId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ThemeExternalResource",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["themeId", "resourceId"]',
                    "sequence_by": "lastModifiedDate"
                }
            }
        },
        {
            "table": {
                "source_table": "ThemeTemplate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModifiedDate"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeZone",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TodoAction",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["actionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TodoEntryV3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["todoEntryId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "UserCapabilities",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "UserPermissions",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "VendorInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["vendorId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "WfRequest",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["wfRequestId"]',
                    "sequence_by": "lastModifiedOn"
                }
            }
        },
        {
            "table": {
                "source_table": "WfRequestComments",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["wfRequestCommentId"]',
                    "sequence_by": "lastModifiedOn"
                }
            }
        },
        {
            "table": {
                "source_table": "WfRequestParticipator",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["wfRequestParticipatorId"]',
                    "sequence_by": "lastModifiedOn"
                }
            }
        },
        {
            "table": {
                "source_table": "WfRequestStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["wfRequestStepId"]',
                    "sequence_by": "lastModifiedOn"
                }
            }
        },
        {
            "table": {
                "source_table": "WfRequestUIData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["wfRequestId"]',
                    "sequence_by": "lastModifiedOn"
                }
            }
        },
        {
            "table": {
                "source_table": "WorkOrder",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["workOrderId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: recruiting (60 entities)
        # =================================================================
        {
            "table": {
                "source_table": "Candidate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["candidateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_Certificates",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_Education",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_InsideWorkExperience",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_Languages",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_Mobility",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_OutsideWorkExperience",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_TalentPool",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateBackground_TalentPoolcorp",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateComments",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["commentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateLight",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["candidateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateProfileConversionInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["candidateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateProfileExtension",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["candidateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CandidateTags",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["tagId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "InterviewIndividualAssessment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["assessmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "InterviewOverallAssessment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["interviewOverallAssessmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplication",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationAssessmentOrder",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["assessmentOrderId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationAssessmentReport",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["reportId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationAssessmentReportDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["reportId", "detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationAudit",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["revNumber", "applicationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationBackgroundCheckRequest",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["requestId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationBackgroundCheckResult",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["resultId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationComments",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["commentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationInterview",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicationInterviewId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationInterviewFieldControls",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicationInterviewId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationOnboardingData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationOnboardingStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationQuestionResponse",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["responseId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_Certificates",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_Education",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_InsideWorkExperience",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_Languages",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_Mobility",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_OutsideWorkExperience",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_TalentPool",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationSnapshot_TalentPoolcorp",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["backgroundElementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["statusId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationStatusAuditTrail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["revNumber"]',
                    "sequence_by": "createdDate"
                }
            }
        },
        {
            "table": {
                "source_table": "JobApplicationStatusLabel",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["labelId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobOffer",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["offerApprovalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobOfferApprover",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["offerApprovalId", "offerApproverId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobOfferFieldControls",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["offerApprovalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobOfferTemplate_Offer_Detail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobOfferTemplate_Standard_Offer",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobReqFwdCandidates",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["candidateId", "jobReqId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobReqGOPosition",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId", "positionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobReqQuestion",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["questionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobReqScreeningQuestion",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["questionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobReqScreeningQuestionChoice",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["questionId", "choiceId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisition",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionAssessment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionFieldControls",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionGroupOperator",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId", "operatorRole", "recruiterId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionLocale",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqLocalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionOperator",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobReqId", "operatorRole"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobRequisitionPosting",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobPostingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OfferLetter",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["offerApprovalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RCMAdminReassignOfferApprover",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["offerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RCMCompetency",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["competencyId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: performance (160 entities)
        # =================================================================
        {
            "table": {
                "source_table": "Achievement",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["achievementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "AchievementDevGoalDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Achievement_achievementId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "AchievementGoalDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Achievement_achievementId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Activity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ActivityFeedback",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Activity_activityId", "feedbackId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ActivityStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSession",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSessionSubject",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionSubjectId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectRank",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["subjectRankId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationTemplate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalCompetency",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalEnum",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalPermission_2001",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalPermission_2002",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalPlanTemplate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoalTask",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoal_2001",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "DevGoal_2002",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Feedback",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["feedbackId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FeedbackFlag",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Feedback_feedbackId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360Participant",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "participantId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ParticipantCategory",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "categoryOrder"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ParticipantColumn",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "columnKey"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ParticipantConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ParticipantDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "participantId", "itemId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ParticipantSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "participantId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360Rater",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "participantId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360RaterSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "participantId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360ReviewContentDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Form360SummarySection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormAuditTrail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["auditTrailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormCustomElement",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["elementKey", "formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormFolder",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["folderId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormHeader",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formDataId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormIntroductionSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormJobRole",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormObjective",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "itemId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormObjectiveComment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "itemId", "sectionIndex", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormObjectiveOtherDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "itemId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormPerfPotSummary",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormRatingScale",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex", "scaleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormRatingScaleValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "scaleId", "scaleIndex", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormReviewFeedback",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "formReviewFeedbackId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormReviewFeedbackList",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormReviewerInfoSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormRouteMap",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formDataId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormRouteSubStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formDataId", "stepOrder"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSectionComment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSectionConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSignature",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formDataId", "signatureOrder"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSignatureSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSubject",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formSubjectId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormSummarySection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormTemplate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formTemplateId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FormUserInformationSection",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId", "sectionIndex"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsItem_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalAchievementsList_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalComment_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMetric_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestonePermission_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalMilestone_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPermission_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPlanState",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalPlanTemplate",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTarget_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTaskPermission_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalTask_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "GoalWeight",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_101",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_2",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_3",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_6",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Goal_8",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "PMAchievement",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["achievementId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PMActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PMActivityFeedback",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId", "feedbackId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PMReviewerInfoSectionConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formReviewerInfoSectionConfigId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerformanceReviewContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PerformanceReviewContentDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formContentId", "formDataId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SimpleGoal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "TeamGoal_1",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "TeamGoal_5",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "TeamGoal_7",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },

        # =================================================================
        # Module: time_attendance (36 entities)
        # =================================================================
        {
            "table": {
                "source_table": "AvailableTimeType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ClockInClockOutBreakTimes",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ClockInClockOutConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ClockInClockOutGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ClockInClockOutMessage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["messageId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTime",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeAUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["EmployeeTime_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeCalendar",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeGroupItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["EmployeeTimeGroup_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeMEX",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["EmployeeTime_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeSheet",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeSheetEntry",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["EmployeeTimeSheet_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeUSA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["EmployeeTime_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeTimeValuationResult",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Holiday",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["HolidayCalendar_externalCode", "holidayDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "HolidayAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Holiday_HolidayCalendar_externalCode", "Holiday_holidayDate", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "HolidayCalendar",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TemporaryTimeInformation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccount",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["TimeAccount_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountPostingRule",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountPurchaseProfile",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountPurchaseProfilePayComponentAssignment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["TimeAccountPurchaseProfile_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountSnapshot",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["accountSnapshotIdentifier"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountTypeAUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["TimeAccountType_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeEventType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["code"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeManagementAlert",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeManagementAlertMessage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["TimeManagementAlert_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeTypeProfile",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "WorkSchedule",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "WorkScheduleDay",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["WorkSchedule_externalCode", "day"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "WorkScheduleDayModel",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "WorkScheduleDayModelSegment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["WorkScheduleDayModel_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: succession (62 entities)
        # =================================================================
        {
            "table": {
                "source_table": "CalibrationCompetencyRating",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ratingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationExecutiveReviewer",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionId", "reviewerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationRating",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ratingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationRatingOption",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["optionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSessionOwner",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionId", "ownerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSessionReviewer",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionId", "reviewerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectObjectRanking",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["subjectId", "rankingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectRating",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ratingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectWeightage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["subjectId", "weightageId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationTemplateCommentFieldName",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId", "fieldNameId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationTemplateCommentType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId", "typeId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationTemplateRater",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["templateId", "raterId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CertificationContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CertificationEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Competency",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["competencyId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CompetencyContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CompetencyEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CompetencyRating",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["competencyRatingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CompetencyType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["GUID"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DevLearningCertifications",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["certificationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "DevLearning_4201",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["learningId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EducationDegreeContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EducationDegreeEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EducationMajorContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EducationMajorEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "InterviewQuestionContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "InterviewQuestionEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobProfile",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobResponsibilityContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "JobResponsibilityEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegacyPositionEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["positionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "Mentor",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["mentorId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "MentorNominee",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["nomineeId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "NominationTarget",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["nominationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "NomineeHistory",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["historyId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "NomineeRelationships",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["nomineeId", "nominationId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PhysicalReqContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PhysicalReqEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PositionCompetencyMappingEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Position_code", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PositionMatrixRelationship",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Position_code", "matrixRelationshipType", "relatedPosition"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PositionRightToReturn",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["Position_code", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RightToReturn",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["positionId", "returnToWorkDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RoleEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SkillContent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["jobProfileId", "roleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SkillEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SkillProfile",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAward",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardBudget",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardCategory",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardGuidelinesRule",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["SpotAwardProgram_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardLevel",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardProgram",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardRedemption",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardRedemptionOrder",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SpotAwardRedemptionProduct",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "SuccessionGoal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["goalId"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "SuccessionGoalDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["goalDetailId"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "SuccessionGoalPlan",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["goalPlanId"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "Successor",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TalentGraphicOption",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["optionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TalentPool",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["code"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TalentRatings",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ratingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: onboarding (40 entities)
        # =================================================================
        {
            "table": {
                "source_table": "AssignedComplianceForm",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["formId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceDocumentFlow",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["flowId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceFormData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceFormDataFieldValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceFormSignature",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["signatureId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceProcess",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceProcessTask",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processTaskId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ComplianceUserFormData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["userId", "formId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2BuddyActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2BuddyProfile",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2DataCollectionUserConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2Equipment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2EquipmentActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2EquipmentType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2EquipmentTypeValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2EquipmentType_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2ExternalHireData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalHireId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2NewHireActivitiesStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processStepId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2OffboardeeDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2OffboardingInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2OnboardeeDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2OnboardingInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2Process",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2ProcessTask",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processTaskId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2RecommendedActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2ResponsiblePartyConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2ProcessTask_processTaskId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2ReviewStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processStepId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2WelcomeActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ONB2Process_processId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ONB2WelcomeStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processStepId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingCandidateInfo",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["applicantId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingEquipment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["equipmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingEquipmentActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId", "processStepId", "onboardingProcessId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingEquipmentType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["typeId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingEquipmentTypeValue",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["valueId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingGoal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["goalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingGoalActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingGoalCategory",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["categoryId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingMeetingActivity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["activityId", "processStepId", "onboardingProcessId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingMeetingEvent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["eventId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingNewHireActivitiesStep",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["processStepId", "onboardingProcessId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "OnboardingProcess",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["onboardingProcessId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: finance (73 entities)
        # =================================================================
        {
            "table": {
                "source_table": "AdvancesInstallments",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["NonRecurringPayment_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEnrollmentConfirmation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["benefitEnrollmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitProgramGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitProgramGroupItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["BenefitProgramGroup_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BudgetPeriodGO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["budgetPeriodId", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CentralCompensation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["effectiveStartDate", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CentralCompensationItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["CentralCompensation_effectiveStartDate", "CentralCompensation_userId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CentralCompensationPayComponent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["CentralCompensationItem_CentralCompensation_effectiveStartDate", "CentralCompensationItem_CentralCompensation_userId", "CentralCompensationItem_externalCode", "payComponent"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExpenseItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ExpenseItemType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FunctionalAreaGO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["functionalAreaID", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FundCenterGO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "FundGO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "GLAccountMapping",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "GrantGO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["grantCode", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityARG",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityAUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityAUT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityBEL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityBLR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityBOL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityBRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCAN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCHE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCHL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCHN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCOL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityCZE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityDEU",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityDNK",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityEGY",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityESP",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityFIN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityFRA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityGBR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityGRC",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityHKG",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityHUN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityIDN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityIND",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityIRL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityISR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityITA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityJPN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityKOR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityMEX",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityMYS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityNLD",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityNOR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityNZL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityPHL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityPOL",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityPRT",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityRUS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntitySAU",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntitySGP",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntitySVK",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntitySVN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntitySWE",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityTHA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityTUN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityTUR",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityTWN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityUSA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityVEN",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "LegalEntityZAF",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["LegalEntity_externalCode", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "NonRecurringPayment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PayrollConfigurationCategory",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PayrollExternalHRIS",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "PayrollSystemConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ProjectControllingObject",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RecurringDeduction",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["effectiveStartDate", "userSysId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "RecurringDeductionItem",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["RecurringDeduction_effectiveStartDate", "RecurringDeduction_userSysId", "payComponentType"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: benefits (43 entities)
        # =================================================================
        {
            "table": {
                "source_table": "Benefit",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["benefitId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitClaimConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCompanyCar",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["carId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCompanyCarEnrollment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["enrollmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCompanyCarOrder",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["orderId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCompanyHousing",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["housingId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCompanyHousingEnrollment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["enrollmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitCost",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["costId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitDependentCoverage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["coverageId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitDependentDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["dependentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitDocuments",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["documentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEligibilityRule",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["ruleId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEmployeeClaim",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["claimId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEmployeeClaimDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["BenefitEmployeeClaim_claimId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEnrollment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["enrollmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEnrollmentDocument",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["documentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitEvent",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["eventId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitFSAConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitHSAEmployerContribution",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["contributionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsuranceCoverage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["coverageId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsuranceCoverageDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsuranceEnrollmentDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsurancePlan",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["planId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsurancePlanUSA",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["BenefitInsurancePlan_planId", "externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitInsuranceProvider",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["providerId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitLegalEntity",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["entityId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitLifeEventConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitPayComponentDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitPensionFund",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["fundId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitPensionPlan",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["planId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitPensionPlanContribution",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["contributionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitPlanCoverage",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["coverageId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitProgram",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["programId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitProgramConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitProgramOptions",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["optionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitSavingsPlan",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["planId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitSavingsPlanEnrollment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["enrollmentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitSavingsPlanSubType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["subTypeId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitsAvailableProgramOption",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitsCreditConfiguration",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["configId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "BenefitsProgramDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode", "effectiveStartDate"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpPensionAdditionalEmployeeContributionDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "EmpPensionAdditionalEmployerContributionDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["detailId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: learning (1 entities)
        # =================================================================
        {
            "table": {
                "source_table": "LearningHistoryData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["lmsId", "userId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: identity (5 entities)
        # =================================================================
        {
            "table": {
                "source_table": "ScimGroup",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },
        {
            "table": {
                "source_table": "ScimResourceType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ScimSchema",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ScimServiceProviderConfig",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ScimUser",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["id"]',
                    "sequence_by": "lastModified"
                }
            }
        },

        # =================================================================
        # Module: rest_api (21 entities)
        # =================================================================
        {
            "table": {
                "source_table": "DPCSStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["type", "country", "subjectId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "DPCSVersion",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompBonusEntryDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["entryId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompEntryDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["compEntryId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompForceCommentDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["commentId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompSalaryEntryDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["entryId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompStockEntryDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["entryId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeCompVarpayEntryDTO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["entryId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "EmployeeGroupingData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "ExtensionPointTaskDetail",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["taskId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "FMLARequest",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["assignmentId", "id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "InstructionalTextEO",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "PBCReplicationData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id", "startDate", "endDate"]'
                }
            }
        },
        {
            "table": {
                "source_table": "SymbolicAccountData",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "TerminationTimeAccountBalanceResponse",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["userId"]'
                }
            }
        },
        {
            "table": {
                "source_table": "TimeAccountBalanceResponse",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["userId", "timeAccountType"]'
                }
            }
        },
        {
            "table": {
                "source_table": "TimeOffEventResponse",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["externalCode"]'
                }
            }
        },
        {
            "table": {
                "source_table": "TimeTypeBalanceResponse",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["userId", "timeTypeCode"]'
                }
            }
        },
        {
            "table": {
                "source_table": "customTasks",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "i9AuditTrailRecord",
                "table_configuration": {
                    "scd_type": "APPEND_ONLY",
                    "primary_keys": '["externalCode"]'
                }
            }
        },
        {
            "table": {
                "source_table": "journeyDetails",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["journeyId"]'
                }
            }
        },

        # =================================================================
        # Module: custom (14 entities)
        # =================================================================
        {
            "table": {
                "source_table": "cust_CostCenter",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_Department",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_EmployeeClass",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_EmploymentType",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_JobClassificationMethod",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_Location",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_ManagerLevel",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_PayGrade",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_PayRange",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_RCMApplicantStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_RCMJobReqStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_RCMOfferStatus",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_RegularTemp",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "cust_WorkLocation",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalCode"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },

        # =================================================================
        # Module: odata_v4 (8 entities)
        # =================================================================
        {
            "table": {
                "source_table": "AdditionalServices",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["id"]'
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSessionV4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["sessionId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectComment",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["commentId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "CalibrationSubjectV4",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["subjectId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "ClockInClockOutExternal",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["externalId"]',
                    "sequence_by": "lastChangedAt"
                }
            }
        },
        {
            "table": {
                "source_table": "SCMNominationApprovalWorkflow",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_2",
                    "primary_keys": '["approvalId"]',
                    "sequence_by": "lastModifiedDateTime"
                }
            }
        },
        {
            "table": {
                "source_table": "TimeEventTypes",
                "table_configuration": {
                    "scd_type": "SCD_TYPE_1",
                    "primary_keys": '["code"]'
                }
            }
        },
        {
            "table": {
                "source_table": "timeevents",
                "table_configuration": {
                    "scd_type": "APPEND_ONLY",
                    "primary_keys": '["externalId"]',
                    "sequence_by": "lastChangedAt"
                }
            }
        },

    ]
}
```

## Module Summary

| Module | Entity Count |
|--------|--------------|
| `employee_central` | 111 |
| `platform` | 56 |
| `recruiting` | 60 |
| `performance` | 160 |
| `time_attendance` | 36 |
| `succession` | 62 |
| `onboarding` | 40 |
| `finance` | 73 |
| `benefits` | 43 |
| `learning` | 1 |
| `identity` | 5 |
| `rest_api` | 21 |
| `custom` | 14 |
| `odata_v4` | 8 |
| **Total** | **690** |