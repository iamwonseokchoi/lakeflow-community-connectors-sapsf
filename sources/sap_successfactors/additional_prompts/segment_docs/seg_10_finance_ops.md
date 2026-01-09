# SAP SuccessFactors API Documentation - Finance & Operations

## Segment Overview
- **Segment**: 10 - Finance & Operations
- **Files Processed**: 6
- **Entities Documented**: 6
- **Endpoints Documented**: 12

## Summary

This segment covers public sector management and financial accounting objects used for cost allocation and budget management in SAP SuccessFactors. All entities in this segment are effective-dated (time-dependent) with support for CDC-based incremental ingestion using `lastModifiedDateTime`.

| Entity | Primary Keys | Ingestion Type | Soft Delete Field |
|--------|--------------|----------------|-------------------|
| BudgetPeriodGO | budgetPeriodId, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |
| FunctionalAreaGO | functionalAreaID, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |
| FundCenterGO | externalCode, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |
| FundGO | externalCode, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |
| GrantGO | grantCode, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |
| ProjectControllingObject | externalCode, effectiveStartDate | cdc_with_deletes | mdfSystemRecordStatus |

---

## Objects

### BudgetPeriodGO
**Source File**: BudgetPeriodGO.json
**API Type**: OData v2
**Base Path**: /odata/v2/BudgetPeriodGO
**Description**: Budget period is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete budget period information.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| budgetPeriodId | string | Yes | 10 | Unique identifier for the budget period |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| budgetPeriodDescription_defaultValue | string | No | 255 | Default budget period description |
| budgetPeriodDescription_en_US | string | No | 255 | Budget period description (English US) |
| budgetPeriodDescription_localized | string | No | 255 | Localized budget period description |
| budgetPeriodExpirationDate | string (date) | No | - | Expiration date for the budget period |
| fbudgetPeriodPeriodicity | string | No | 10 | Budget period periodicity |
| reversalDate | string (date) | No | - | Reversal date |
| createdBy | string | No (readonly) | 100 | User who created the record |
| createdDateTime | string (date) | No (readonly) | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 70 | Entity object ID |
| entityUUID | string | No (readonly) | 70 | Entity UUID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `budgetPeriodId` (string)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /BudgetPeriodGO | Get all budget periods | $skip, $top, $count, $filter, $orderby, $select |
| GET | /BudgetPeriodGO(budgetPeriodId='{budgetPeriodId}',effectiveStartDate=datetime'{effectiveStartDate}') | Get budget period by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

### FunctionalAreaGO
**Source File**: FunctionalAreaGO.json
**API Type**: OData v2
**Base Path**: /odata/v2/FunctionalAreaGO
**Description**: Functional area is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete functional area information.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| functionalAreaID | string | Yes | 16 | Unique identifier for the functional area |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| functionalAreaDescription_defaultValue | string | No | 255 | Default functional area description |
| functionalAreaDescription_en_US | string | No | 255 | Functional area description (English US) |
| functionalAreaDescription_localized | string | No | 255 | Localized functional area description |
| expirationDate | string (date) | No | - | Expiration date |
| createdBy | string | No (readonly) | 100 | User who created the record |
| createdDateTime | string (date) | No (readonly) | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 70 | Entity object ID |
| entityUUID | string | No (readonly) | 70 | Entity UUID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `functionalAreaID` (string)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FunctionalAreaGO | Get all functional areas | $skip, $top, $count, $filter, $orderby, $select |
| GET | /FunctionalAreaGO(effectiveStartDate=datetime'{effectiveStartDate}',functionalAreaID='{functionalAreaID}') | Get functional area by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

### FundCenterGO
**Source File**: FundCenterGO.json
**API Type**: OData v2
**Base Path**: /odata/v2/FundCenterGO
**Description**: Fund center is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete fund center information.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| externalCode | string | Yes | 128 | External code (format: fundCenterCode/financialManagementArea) |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| financialManagementArea | string | Yes | 4 | Financial management area code |
| fundCenterCode | string | Yes | 16 | Fund center code |
| fundCenterDescription_defaultValue | string | No | 255 | Default fund center description |
| fundCenterDescription_en_US | string | No | 255 | Fund center description (English US) |
| fundCenterDescription_localized | string | No | 255 | Localized fund center description |
| createdBy | string | No (readonly) | 100 | User who created the record |
| createdDateTime | string (date) | No (readonly) | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 70 | Entity object ID |
| entityUUID | string | No (readonly) | 70 | Entity UUID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `externalCode` (string, format: fundCenterCode/financialManagementArea)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FundCenterGO | Get all fund centers | $skip, $top, $count, $filter, $orderby, $select |
| GET | /FundCenterGO(effectiveStartDate=datetime'{effectiveStartDate}',externalCode='{externalCode}') | Get fund center by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

### FundGO
**Source File**: sap-sf-FundGO-v1.json
**API Type**: OData v2
**Base Path**: /odata/v2/FundGO
**Description**: Fund is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete fund information.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| externalCode | string | Yes | 128 | External code (format: fundCode/fmArea) |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| fmArea | string | Yes | 4 | Financial management area |
| fundCode | string | Yes | 10 | Fund code |
| fundDescription_defaultValue | string | No | 255 | Default fund description |
| fundDescription_en_US | string | No | 255 | Fund description (English US) |
| fundDescription_localized | string | No | 255 | Localized fund description |
| fundExpirationDate | string (date) | No | - | Fund expiration date |
| fundPeriodicity | string | No | 255 | Fund periodicity |
| createdBy | string | No (readonly) | 100 | User who created the record |
| createdDateTime | string (date) | No (readonly) | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 70 | Entity object ID |
| entityUUID | string | No (readonly) | 70 | Entity UUID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `externalCode` (string, format: fundCode/fmArea)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FundGO | Get all funds | $skip, $top, $count, $filter, $orderby, $select |
| GET | /FundGO(effectiveStartDate=datetime'{effectiveStartDate}',externalCode='{externalCode}') | Get fund by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

### GrantGO
**Source File**: sap-sf-GrantGO-v1.json
**API Type**: OData v2
**Base Path**: /odata/v2/GrantGO
**Description**: Grant is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete grant information.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| grantCode | string | Yes | 128 | Unique identifier for the grant |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| companyCode | string | No | 4 | Company code |
| grantDesc_defaultValue | string | No | 255 | Default grant description |
| grantDesc_en_US | string | No | 255 | Grant description (English US) |
| grantDesc_localized | string | No | 255 | Localized grant description |
| grantNotRelevent | boolean | No | - | Indicates if grant is not relevant |
| createdBy | string | No (readonly) | 100 | User who created the record |
| createdDateTime | string (date) | No (readonly) | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 70 | Entity object ID |
| entityUUID | string | No (readonly) | 70 | Entity UUID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `grantCode` (string)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /GrantGO | Get all grants | $skip, $top, $count, $filter, $orderby, $select |
| GET | /GrantGO(effectiveStartDate=datetime'{effectiveStartDate}',grantCode='{grantCode}') | Get grant by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

### ProjectControllingObject
**Source File**: ProjectControllingObject.json
**API Type**: OData v2
**Base Path**: /odata/v2/ProjectControllingObject
**Description**: Project controlling object is one of the standard accounting objects supported for employees in an organization. You can use this API to create, update, read, and delete project controlling object information. Currently only WBS element (PRN) type is supported.

#### Schema
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| externalCode | string | Yes | 50 | Unique external code for the project controlling object |
| effectiveStartDate | string (date) | Yes | - | Start date for the effective period |
| effectiveStatus | string (enum) | Yes | 128 | Status codes: A - Active, I - InActive |
| company | string | No | 128 | Company reference |
| description_defaultValue | string | No | 128 | Default description |
| description_en_US | string | No | 128 | Description (English US) |
| description_localized | string | No | 128 | Localized description |
| name_defaultValue | string | No | 60 | Default name |
| name_en_US | string | No | 60 | Name (English US) |
| name_localized | string | No | 32 | Localized name |
| isStatistical | boolean | No | - | Indicates if the object is statistical |
| projectControllingObjectType | string | No | 128 | Project controlling object type (only PRN/WBS element supported) |
| createdBy | string | No | 100 | User who created the record |
| createdDateTime | string (date) | No | - | Creation timestamp |
| effectiveEndDate | string (date) | No (readonly) | - | End date for the effective period |
| entityOID | string | No (readonly) | 32 | Entity object ID |
| lastModifiedBy | string | No (readonly) | 100 | User who last modified the record |
| lastModifiedDateTime | string (date) | No (readonly) | - | Last modification timestamp |
| mdfSystemRecordStatus | string (enum) | No (readonly) | 255 | Status codes: C - Correction, D - Soft deleted, F - Full Purge Import, N - Normal, P - Pending, PH - Pending history |

#### Primary Keys
- `externalCode` (string)
- `effectiveStartDate` (datetime)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus (value 'D' indicates soft deleted)
- **Rationale**: Entity has lastModifiedDateTime for change tracking and mdfSystemRecordStatus field with 'D' value for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ProjectControllingObject | Get all project controlling objects | $skip, $top, $count, $filter, $orderby, $select |
| GET | /ProjectControllingObject(effectiveStartDate=datetime'{effectiveStartDate}',externalCode='{externalCode}') | Get project controlling object by key | $select |

#### Query Parameters
- `$top`: Show only the first n items (default: 20)
- `$skip`: Skip the first n items
- `$filter`: Filter items by property values
- `$count`: Include count of items
- `$orderby`: Order items by property values
- `$select`: Select properties to be returned

---

## Common Patterns

### Effective Dating
All entities in this segment use effective dating with:
- `effectiveStartDate`: When the record becomes effective
- `effectiveEndDate`: When the record is no longer effective (readonly, system-managed)
- `effectiveStatus`: Active (A) or Inactive (I)

### Audit Fields
All entities include standard audit fields:
- `createdBy`: User who created the record
- `createdDateTime`: Timestamp of creation
- `lastModifiedBy`: User who last modified the record
- `lastModifiedDateTime`: Timestamp of last modification

### Soft Delete Pattern
The `mdfSystemRecordStatus` field indicates record status:
- `N`: Normal record
- `D`: Soft deleted record
- `C`: Correction
- `F`: Full Purge Import in Progress
- `P`: Pending record
- `PH`: Pending history record

### Localization
Description and name fields support localization:
- `*_defaultValue`: Default language value
- `*_en_US`: English (US) value
- `*_localized`: Current user's locale value

### Pagination
All collection endpoints support OData pagination:
- `$top`: Limit number of results (default: 20)
- `$skip`: Skip first n results
- `$count`: Include total count
- `$filter`: Apply filter expressions
- `$orderby`: Sort results
- `$select`: Choose specific fields

---

## Implementation Notes

### Connector Implementation Recommendations

1. **Primary Key Handling**: All entities use composite keys with `effectiveStartDate` as one component. The datetime format must be: `datetime'YYYY-MM-DDTHH:MM:SS'`

2. **Incremental Sync Strategy**:
   - Use `lastModifiedDateTime` for CDC cursor
   - Filter: `$filter=lastModifiedDateTime gt datetime'{last_sync_time}'`
   - Order by: `$orderby=lastModifiedDateTime asc`

3. **Soft Delete Detection**:
   - Filter for deleted records: `$filter=mdfSystemRecordStatus eq 'D'`
   - For full sync with deletes: Include mdfSystemRecordStatus in response to identify deleted records

4. **External Code Format**: Some entities (FundCenterGO, FundGO) use composite external codes with format `{code}/{area}`. URL encoding may be required.

5. **Pagination Best Practice**:
   - Use server-side pagination with `$skip` and `$top`
   - Default page size is 20; adjust based on performance needs
   - Check for `__next` link in response for additional pages

### API Authentication
All endpoints require Basic Authentication. See SAP SuccessFactors API documentation for OAuth alternatives.

### Rate Limiting
Follow SAP SuccessFactors API rate limiting guidelines. Implement exponential backoff for 429 responses.
