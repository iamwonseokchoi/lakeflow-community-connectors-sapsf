# SAP SuccessFactors API Documentation - REST Extended APIs

## Segment Overview
- **Segment**: 11 - REST Extended APIs
- **Files Processed**: 8
- **Entities Documented**: 32
- **Endpoints Documented**: 12

## Files Processed
1. sap-sf-customTasks-v2.json - Onboarding and Offboarding Custom Tasks
2. sap-sf-newhirejourney-v1.json - Onboarding New Hire Journey
3. sap-sf-FMLARequest-v1.json - Family and Medical Leave Act Request
4. sap-sf-employeeCompensation-v1.json - Compensation Management
5. sap-sf-PLTRBPGenAI-v1.json - Role-Based Permissions Generative AI Troubleshooting
6. sap-sf-PositionBudgetingControl-v1.json - Position Budgeting Control for Cloud
7. UserManagementSCIM.json - User Management (SCIM) for Employee Central Payroll
8. i9audittrail.json - Form I-9 Audit Trail

---

## Objects

### customTasks
**Source File**: sap-sf-customTasks-v2.json
**API Type**: REST
**Base Path**: /rest/onboarding/customtasks/v2

#### Description
Custom Tasks Object for Onboarding and Offboarding custom tasks management. Enables extraction of data from custom tasks and completion via third-party integration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | Id of Custom Task |
| title | string | No | Title of Custom Task |
| config | string | No | Config id |
| status | string | No | Status of Task |
| user | object (user) | No | Associated user object |
| processId | string | No | Onboarding Process ID |
| dueDate | string (date) | No | Due Date |
| optional | boolean | No | Optional Task indicator |
| responsibleUsers | array (user) | No | Responsible Users |
| completedDate | string (date-time) | No | Completed Date |
| completedBy | object (user) | No | User who completed the task |
| customResource | object (customResource) | No | Custom MDF resource reference |

#### Primary Keys
- `id` (string) - Custom Task ID

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No timestamp filter parameters available. Tasks are retrieved by ID or process ID without modification tracking support.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/onboarding/customtasks/v2/customTasks/{taskDataId} | Gets custom task information by task ID | None |
| GET | /rest/onboarding/customtasks/v2/customTasks?$filter=processId eq '{processId}' | Gets custom task information for process ID | None |

---

### user (Custom Tasks)
**Source File**: sap-sf-customTasks-v2.json
**API Type**: REST

#### Description
User type properties within custom tasks.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | User ID |
| displayName | string | No | Display Name |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within customTasks. No direct endpoint or modification tracking.

---

### customResource
**Source File**: sap-sf-customTasks-v2.json
**API Type**: REST

#### Description
Custom MDF resource reference within custom tasks.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | Custom MDF Internal Id |
| type | string | No | Custom MDF Type |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within customTasks. No direct endpoint or modification tracking.

---

### journeyDetails
**Source File**: sap-sf-newhirejourney-v1.json
**API Type**: REST
**Base Path**: /onboarding/newhire/v1

#### Description
Onboarding journey details for new hires including status, manager, and hire information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| journeyId | string | No | Onboarding Journey Id for the Onboardee (x-key: true) |
| status | string | No | Status of the Journey (e.g., INITIATED) |
| userId | string | No | Onboarding user ID |
| startDate | string (date) | No | Start Date |
| manager | string | No | Manager user id |
| journeyType | string | No | Type of Journey |
| journeySubType | string | No | Sub type of journey |
| hireStatus | string | No | Hire status of journey |
| userFullName | string | No | Full name of new hire |
| managerFullName | string | No | Full name of the manager |

#### Primary Keys
- `journeyId` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No timestamp-based filtering available. Journeys are retrieved by ID without modification tracking.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /onboarding/newhire/v1/journeys/{journeyId} | Get the Onboarding journey by journey id | None |

---

### newHireCreateJourneyRequest
**Source File**: sap-sf-newhirejourney-v1.json
**API Type**: REST

#### Description
Onboarding Journey payload for creating new hire journeys.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| firstName | string | No | First Name of the new hire |
| lastName | string | No | Last Name of the new hire |
| email | string | No | Personal email of the new hire |
| userName | string | No | Preferred user name (x-key: true) |
| startDate | string (date) | No | Start date (floating date with no time part) |
| manager | string | No | Manager Id |
| company | string | No | Company Id |
| eventReason | string | No | Hire Event reason |
| status | string | No | Journey status |
| userId | string | No | Preferred User Id (x-key: true) |
| assignmentId | string | No | Assignment ID (nullable) |
| personId | string | No | Person Id (nullable) |
| journeyType | string | No | Only ONBOARDING is supported |
| journeySubType | string | No | NewHire or RehireWithNewEmployment |
| terminatedLegacyUserId | string | No | Terminated user id for Rehire case |
| initiatorKeys | object | No | Journey Initiator Business Keys |

#### Primary Keys
- `userName` (string)
- `userId` (string)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Request payload schema, not directly queryable.

---

### FMLARequest
**Source File**: sap-sf-FMLARequest-v1.json
**API Type**: REST
**Base Path**: /rest/workforce/localization/v1

#### Description
Family and Medical Leave Act (FMLA) request data including continuous/intermittent absence information for third-party provider integration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Assignment Id | string | No | Assignment Id (x-key: true) |
| Id | string | No | Request Id (x-key: true) |
| Provider Name | string | No | Third-party provider name |
| FMLA Start date | string | No | FMLA leave start date |
| FMLA End date | string | No | FMLA leave end date |
| FMLA reason | string | No | Reason for FMLA leave |
| Absence Type | string | No | Type of absence |
| Request Status | string | No | Status of the request |
| Return to work date | string | No | Expected return date |
| Absence Specific Information | array | No | Intermittent request details |

#### Primary Keys
- `Assignment Id` (string)
- `Id` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No GET endpoints defined in the API specification. Only POST and PATCH operations are available for creating and updating FMLA requests.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| (No GET endpoints) | /rest/workforce/localization/v1/fmlaRequests | POST/PATCH only - Create or update FMLA requests | N/A |

---

### IntermitentRequestDetail
**Source File**: sap-sf-FMLARequest-v1.json
**API Type**: REST

#### Description
Intermittent absence details within FMLA requests.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Absence Start date | string | No | Start date of absence |
| Absence End Date | string | No | End date of absence |
| Absence start time | string | No | Start time of absence |
| Absence end time | string | No | End time of absence |
| duration days | string | No | Duration in days |
| duration hours | string | No | Duration in hours |

#### Primary Keys
- None explicitly defined

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within FMLARequest. No direct endpoint.

---

### EmployeeCompEntryDTO (EmployeeCompensation)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST
**Base Path**: /rest/rewards/compensation/v1

#### Description
Compensation records from salary, stock, bonus, and variable pay worksheets including user data, salary-related data, performance rating, and force comments.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | Yes | Compensation entry ID |
| compPlanId | integer (int64) | Yes | Compensation plan ID |
| formDataId | integer (int64) | Yes | Compensation form data ID |
| compTemplateId | integer (int64) | No | Compensation template ID |
| entryUserId | string | No | Entry user ID |
| entryUserGroupName | string | No | Entry user group name |
| entryUserName | string | No | Entry username |
| entryUserFirstName | string | No | Entry user firstname |
| entryUserLastName | string | No | Entry user lastname |
| entryUserMiddleName | string | No | Entry user middle name |
| revieweeMgrUserId | string | No | Manager user ID |
| revieweeMgrUserName | string | No | Manager username |
| revieweeMgrUserFirstName | string | No | Manager user firstname |
| revieweeMgrUserLastName | string | No | Manager user lastname |
| revieweeMgrUserMiddleName | string | No | Manager user middle name |
| department | string | No | Department |
| division | string | No | Division |
| location | string | No | Location |
| localCurrencyCode | string | No | Entry local currency code |
| functionalCurrencyCode | string | No | Template functional currency code |
| isECUser | boolean | No | Indicates if the entry is an Employee Central user |
| isTotalComp | boolean | No | Indicates if the template is a total compensation plan |
| salary | object | No | Salary details |
| stock | object | No | Stock details |
| bonus | object | No | Bonus details |
| varpay | object | No | Variable pay details |
| ratingInfos | array | No | Rating information |
| commentList | array | No | Force comments |

#### Primary Keys
- `compEntryId` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No timestamp-based filtering available. Uses templateId as required parameter with standard OData-style pagination ($skip, $top).

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /employeeCompensations | Retrieves compensation records on worksheets for a template ID | $skip, $top |

---

### EmployeeCompSalaryEntryDTO (Salary)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Salary details within employee compensation records.

#### Schema (Key Fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | Yes | Compensation entry ID |
| startDate | string (date-time) | No | Date of current position |
| curSalary | number (double) | No | Current salary |
| curSalaryLocal | number (double) | No | Current salary in local currency |
| finalSalary | number (double) | No | Final salary |
| finalSalaryLocal | number (double) | No | Final salary in local currency |
| merit | number (double) | No | Merit |
| promo | number (double) | No | Promotion |
| extra | number (double) | No | Adjustment |
| extra2 | number (double) | No | Adjustment2 |
| raise | number (double) | No | Total raise |
| lumpSum | number (double) | No | Lump sum |
| totalIncrease | number (double) | No | Total increase |
| totalComp | number (double) | No | Total compensation |
| jobLevel | string | No | Job level |
| jobTitle | string | No | Title |
| payGrade | string | No | Current pay grade |
| finalPayGrade | string | No | Final pay grade |
| jobFamily | string | No | Current job family |
| jobRole | string | No | Current job role |
| jobCode | string | No | Current job code |
| customFields | object | No | Reportable custom fields in salary tab |

#### Primary Keys
- `compEntryId` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within EmployeeCompEntryDTO. Expanded via $expand parameter.

---

### EmployeeCompBonusEntryDTO (Bonus)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Bonus details within employee compensation records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | Yes | Compensation entry ID |
| target | number (double) | No | Target |
| extraPercent | number (double) | No | User modifier percent |
| extra | number (double) | No | Adjustment |
| total | number (double) | No | Total |
| isIneligible | boolean | No | Indicates if the entry is ineligible |
| bonusNotes | string | No | Bonus notes |
| customFields | object | No | Reportable custom fields in bonus tab |

#### Primary Keys
- `compEntryId` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within EmployeeCompEntryDTO. Expanded via $expand parameter.

---

### EmployeeCompStockEntryDTO (Stock)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Stock details within employee compensation records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | Yes | Compensation entry ID |
| stock | number (double) | No | Stock |
| grantDate | string (date-time) | No | Date of grant |
| option | number (double) | No | Options |
| units | number (double) | No | Units |
| other1 | number (double) | No | Other1 |
| other2 | number (double) | No | Other2 |
| other3 | number (double) | No | Other3 |
| isIneligible | boolean | No | Indicates if the entry is ineligible |
| stockNotes | string | No | Stock notes |
| customFields | object | No | Reportable custom fields in stock tab |

#### Primary Keys
- `compEntryId` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within EmployeeCompEntryDTO. Expanded via $expand parameter.

---

### EmployeeCompVarpayEntryDTO (VariablePay)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Variable pay details within employee compensation records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | Yes | Compensation entry ID |
| performancePer | number (double) | No | Ind percent |
| teamPerformancePer | number (double) | No | Team percent |
| varpayTeamRating | number (double) | No | Team rating |
| varpayIndividualRating | number (double) | No | Ind rating |
| overwriteAmt | number (double) | No | Override |
| overwriteDesc | string | No | Override description |
| overwriteLastModified | string (date-time) | No | Last modified date of override |
| notes | string | No | Variable pay notes |
| teamPayoutAmt | number (double) | No | Team amt |
| finalPayoutAmt | number (double) | No | Final payout |
| customFields | object | No | Reportable custom fields in variable pay tab |

#### Primary Keys
- `compEntryId` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within EmployeeCompEntryDTO. Expanded via $expand parameter.

---

### EmployeeCompRatingInfoDTO (RatingInformation)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Rating information within employee compensation records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compEntryId | integer (int64) | No | Compensation entry ID |
| ratingSource | string (enum) | No | Rating source (PM, EmployeeProfile) |
| ratingType | string | No | Rating type |
| rating | number (double) | No | Rating |
| ratingDesc | string | No | Rating description |
| compRating | number (double) | No | Comp rating |
| pmFormTemplateId | integer (int64) | No | Performance form template ID |
| pmFormDataId | integer (int64) | No | Performance form data ID |
| feedbackId | integer (int64) | No | Feedback ID |

#### Primary Keys
- `compEntryId` (integer) - Composite with rating type

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within EmployeeCompEntryDTO. Expanded via $expand parameter.

---

### EmployeeCompForceCommentDTO (ForceComment)
**Source File**: sap-sf-employeeCompensation-v1.json
**API Type**: REST

#### Description
Force comments within employee compensation records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| compCommentId | integer (int64) | No | Force comment ID |
| compEntryId | integer (int64) | No | Compensation entry ID |
| compCommentType | integer (int32) | No | Force comment type |
| compCommentField | string | No | Force comment field |
| compCommentComment | string | No | Force comment content |
| createdDate | string (date-time) | No | Created date of force comment |
| createdBy | string | No | Author of force comment |
| lastModified | string (date-time) | No | Last modified date of force comment |
| lastModifiedBy | string | No | Author of the last modification on force comment |

#### Primary Keys
- `compCommentId` (integer)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModified
- **Rationale**: Has lastModified timestamp field that can be used for incremental tracking.

---

### RoleResponse (RBP GenAI Roles)
**Source File**: sap-sf-PLTRBPGenAI-v1.json
**API Type**: REST
**Base Path**: /rest/iam/authorization/genai/v1

#### Description
Role names associated with permission groups for Role-Based Permissions troubleshooting.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| value | array (string) | No | List of role names associated with the given group ID |

#### Primary Keys
- N/A (Response wrapper)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Query-based response without persistent identifiers or modification tracking.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/iam/authorization/genai/v1/roles?groupId={groupId} | Query all role names based on the access group | None |

---

### PermissionsResponse (RBP GenAI)
**Source File**: sap-sf-PLTRBPGenAI-v1.json
**API Type**: REST

#### Description
RBP permissions search results with granted status.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| permissions | array | No | List of permission details |
| permissions[].permissionId | integer | No | The RBP permission ID |
| permissions[].permissionLabel | string | No | The label of the permission |
| permissions[].granted | boolean | No | Indicates whether permission is granted |
| hasMore | boolean | No | Indicates whether there are more permissions available |

#### Primary Keys
- `permissionId` (integer) within permissions array

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Search/query response. POST-based query endpoint, not suitable for direct ingestion.

---

### GroupsResponse (RBP GenAI)
**Source File**: sap-sf-PLTRBPGenAI-v1.json
**API Type**: REST

#### Description
Permission groups (static and dynamic) for RBP troubleshooting.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| staticGroups | array | No | List of top 5 static groups |
| staticGroups[].groupId | integer | No | The ID of a permission group |
| staticGroups[].groupName | string | No | The name of the static group |
| dynamicGroups | array | No | List of top 5 dynamic groups |
| dynamicGroups[].groupId | integer | No | The unique identifier of the dynamic group |
| dynamicGroups[].groupName | string | No | The name of the dynamic group |

#### Primary Keys
- `groupId` (integer) within groups arrays

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Search/query response. POST-based query endpoint, not suitable for direct ingestion.

---

### PBCReplicationData (Employee Financing)
**Source File**: sap-sf-PositionBudgetingControl-v1.json
**API Type**: REST
**Base Path**: /rest/workforce/positionbudgetcontrol/v1

#### Description
Employee financing data for position budgeting control including HR reference documents, earmarked documents, and budget addresses.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | User ID |
| objectType | string | No | Object type (e.g., EMP) |
| startDate | string (date) | No | Financing period start date |
| endDate | string (date) | No | Financing period end date |
| companyCode | string | No | Company code |
| creationDate | string (date) | No | Run creation date |
| status | string | No | Financing status (e.g., ERR) |
| payLocked | string | No | Payroll lock |
| recalActive | string | No | Recalculation active |
| financingStatusEffectiveDate | string (date) | No | Financing status effective date |
| allDocsReleased | boolean | No | Overall commitment document completion indicator |
| replicationFinancingHeaders | array | No | Financing header records |

#### Primary Keys
- `id` (string) + `startDate` + `endDate` (composite)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastKnownReplicationTimeStamp (query parameter)
- **Rationale**: Supports timestamp-based incremental queries via lastKnownReplicationTimeStamp parameter.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /employeeFinancingData | Get employee financing data | $skip, $top |

---

### SymbolicAccountData
**Source File**: sap-sf-PositionBudgetingControl-v1.json
**API Type**: REST

#### Description
Symbolic account mappings for Position Budgeting Control pay component configuration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | Unique identifier |
| countryCode | string | No | Country code |
| payComponentId | string | No | Pay component ID |
| accountAssignmentType | string | No | Account assignment type |
| validFrom | string (date) | No | Valid from date |
| validTo | string (date) | No | Valid to date |
| symbolicAccount | string | No | Symbolic account identifier |
| lastModifiedTimestamp | string (date-time) | No | Last modified timestamp |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedTimestamp
- **Rationale**: Has lastModifiedTimestamp field for tracking modifications.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /symbolicAccounts | Get list of symbolic accounts | None (query params for filtering) |

---

### EmployeeGroupingData
**Source File**: sap-sf-PositionBudgetingControl-v1.json
**API Type**: REST

#### Description
Employee grouping mappings for Position Budgeting Control configuration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | Unique identifier |
| countryCode | string | No | Country code |
| employeeClass | string | No | Employee class |
| employmentType | string | No | Employment type |
| validFrom | string (date) | No | Valid from date |
| validTo | string (date) | No | Valid to date |
| employeeGroup | string | No | Employee grouping identifier |
| lastModifiedTimestamp | string (date-time) | No | Last modified timestamp |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedTimestamp
- **Rationale**: Has lastModifiedTimestamp field for tracking modifications.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /employeeGroupings | Get list of employee groupings | None (query params for filtering) |

---

### User (SCIM)
**Source File**: UserManagementSCIM.json
**API Type**: REST (SCIM 2.0)
**Base Path**: /sap/payroll/ecp/scim/v1

#### Description
SCIM 2.0 User representation for Employee Central Payroll identity provisioning.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | User identifier (filterable) |
| userUuid | string | No | User UUID (nullable) |
| userName | string | Yes | User name (filterable) |
| name | object (Name) | No | User name components |
| displayName | string | No | Display name (nullable) |
| nickName | string | No | Nickname (nullable) |
| title | string | No | Title (nullable) |
| userType | string | No | User type (filterable) |
| active | boolean | Yes | Active status (filterable) |
| meta | object | No | Metadata (resourceType, created, lastModified, location, version) |
| Schemas | array (string) | Yes | SCIM schema URIs |
| emails | array | No | Email addresses |
| phoneNumbers | array | No | Phone numbers |
| groups | object | No | Group memberships |
| externalId | string | No | External identifier |
| type | string | No | Type |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: meta.lastModified
- **Rationale**: SCIM metadata includes lastModified timestamp. Filter parameter supports meta.lastModified comparisons (gt, lt, ge, le).

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /payroll/ecp/scim/v1/Users | Returns all users | startIndex, count |
| GET | /payroll/ecp/scim/v1/Users/{id} | Returns a specific user | None |

---

### SCIM.Group
**Source File**: UserManagementSCIM.json
**API Type**: REST (SCIM 2.0)

#### Description
SCIM 2.0 Group representation for Employee Central Payroll.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No | Group identifier (x-key: true, filterable) |
| displayName | string | No | Display name (filterable) |
| members | array (Member) | No | Group members |
| meta | object | No | Metadata (resourceType, created, lastModified, location, version) |
| schemas | array (string) | No | SCIM schema URIs |
| GroupExtensionVersion2 | object | No | Group extension data |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: meta.lastModified
- **Rationale**: SCIM metadata includes lastModified timestamp. Filter parameter supports meta.lastModified comparisons.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /payroll/ecp/scim/v1/Groups | Returns all groups | startIndex, count |
| GET | /payroll/ecp/scim/v1/Groups/{id} | Returns a specific group | None |

---

### Member (SCIM)
**Source File**: UserManagementSCIM.json
**API Type**: REST (SCIM 2.0)

#### Description
SCIM group member reference.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| value | any | No | Id of a SCIM User (x-key: true) |
| type | string | No | Type of the member - here only type User (x-key: true) |
| display | string | No | Display name of a user |
| $ref | string | No | Reference to the member |

#### Primary Keys
- `value` + `type` (composite)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within SCIM.Group. Retrieved via group endpoints.

---

### Name (SCIM)
**Source File**: UserManagementSCIM.json
**API Type**: REST (SCIM 2.0)

#### Description
SCIM user name components.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| formatted | string | No | Formatted full name |
| familyName | string | No | Family name |
| givenName | string | No | Given name |
| middleName | string | No | Middle name |
| honorificPrefix | string | No | Honorific prefix |
| honorificSuffix | string | No | Honorific suffix |

#### Primary Keys
- None (embedded object)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Nested entity within User. Not directly queryable.

---

### i9AuditTrailRecord
**Source File**: i9audittrail.json
**API Type**: REST
**Base Path**: /rest/onboarding/compliance/i9audittrail/v1

#### Description
Form I-9 audit trail record for immigration compliance tracking. Includes Section 1 (employee info), Section 2 (employer verification), and Section 3 (reverification) data.

#### Schema (Key Fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| seqNo | integer (int64) | No | Sequence number |
| externalCode | string | No | External code (x-key: true) |
| userId | string | No | User id (e.g., 2011034567) |
| sourceOfRecord | string (enum) | No | Source of record (COMPLIANCE, IMPORT, API) |
| complianceProcess.processId | string | No | Compliance process id (nullable) |
| status | string (enum) | No | Status (SECTION1_INITIATED through VOIDED) |
| firstName | string | No | First name (Section 1) |
| lastName | string | No | Last name (Section 1) |
| ssn | string | No | Social Security Number (Section 1) |
| dateOfBirth | string (date) | No | Date of birth (Section 1) |
| citizenshipType | string (enum) | No | Citizenship type (US_CITIZEN, US_NATIONAL, etc.) |
| employerFirstName | string | No | Employer first name (Section 2) |
| employerLastName | string | No | Employer last name (Section 2) |
| listADocument1Number | string | No | List A Document 1 number (Section 2) |
| listBDocumentNumber | string | No | List B Document number (Section 2) |
| listCDocumentNumber | string | No | List C Document number (Section 2) |
| verificationDate | string | No | Verification date (Section 3) |
| verifierFirstName | string | No | Verifier first name (Section 3) |
| verifierLastName | string | No | Verifier last name (Section 3) |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: append
- **Cursor Field**: N/A (audit trail records are append-only)
- **Rationale**: Audit trail records are immutable once created. Each record represents a point-in-time snapshot of I-9 form status. Use seqNo for ordering.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /i9AuditTrailRecords/{externalCode} | Gets audit trail record by external code | $skip, $top |
| GET | /user/{assignmentId}/i9AuditTrailRecords | Gets audit trail records for selected user | $skip, $top |

---

### i9Section1
**Source File**: i9audittrail.json
**API Type**: REST

#### Description
Form I-9 Section 1 - Employee Information and Attestation.

#### Schema (Key Fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| firstName | string | No | First name |
| lastName | string | No | Last name |
| middleName | string | No | Middle name |
| otherName | string | No | Other names used |
| address | string | No | Street address |
| apartmentNumber | string | No | Apartment number |
| city | string | No | City |
| state | string (enum) | No | State (US state codes) |
| zipCode | string | No | ZIP code |
| dateOfBirth | string (date) | No | Date of birth |
| ssn | string | No | Social Security Number |
| emailAddress | string | No | Email address |
| phoneNumber | string | No | Phone number |
| citizenshipType | string (enum) | No | Citizenship type |
| alienRegistrationNumber | string | No | Alien registration number |
| uscisNumber | string | No | USCIS number |
| passportNumber | string | No | Passport number |
| visaType | string (enum) | No | Visa type |
| visaExpirationDate | string (date) | No | Visa expiration date |

#### Primary Keys
- None (embedded within i9AuditTrailRecord)

#### Ingestion Type
- **Type**: append
- **Rationale**: Embedded schema within i9AuditTrailRecord. Same ingestion pattern applies.

---

### i9Section2
**Source File**: i9audittrail.json
**API Type**: REST

#### Description
Form I-9 Section 2 - Employer or Authorized Representative Review and Verification.

#### Schema (Key Fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employerTitle | string | No | Employer title |
| employerBusiness | string | No | Employer business name |
| employerFirstName | string | No | Employer first name |
| employerLastName | string | No | Employer last name |
| employerAddress | string | No | Employer address |
| employerCity | string | No | Employer city |
| employerState | string | No | Employer state |
| employerZipCode | string | No | Employer ZIP code |
| listADocument1Number | string | No | List A Document 1 number |
| listADocument1Name | string | No | List A Document 1 name |
| listADocument1Expiry | string | No | List A Document 1 expiry |
| listBDocumentNumber | string | No | List B Document number |
| listBDocumentName | string | No | List B Document name |
| listCDocumentNumber | string | No | List C Document number |
| listCDocumentName | string | No | List C Document name |
| remote | string | No | Remote verification indicator |
| reasonForRemote | string | No | Reason for remote verification |

#### Primary Keys
- None (embedded within i9AuditTrailRecord)

#### Ingestion Type
- **Type**: append
- **Rationale**: Embedded schema within i9AuditTrailRecord. Same ingestion pattern applies.

---

### i9Section3
**Source File**: i9audittrail.json
**API Type**: REST

#### Description
Form I-9 Section 3 - Reverification and Rehires.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| verificationDate | string | No | Verification date |
| verificationDocument | string | No | Verification document |
| verifierFirstName | string | No | Verifier first name |
| verifierLastName | string | No | Verifier last name |
| verifierMiddleName | string | No | Verifier middle name |
| dateOfRehire | string | No | Date of rehire |
| previousEmploymentGrantExpired | string | No | Previous employment grant expired |
| reverificationListADoc1 | string | No | Reverification List A Document 1 |
| reverificationListADoc2 | string | No | Reverification List A Document 2 |
| reverificationListADoc3 | string | No | Reverification List A Document 3 |
| reverificationListCDoc | string | No | Reverification List C Document |
| newFirstName | string | No | New first name |
| newLastName | string | No | New last name |
| newMiddleNamec | string | No | New middle name |

#### Primary Keys
- None (embedded within i9AuditTrailRecord)

#### Ingestion Type
- **Type**: append
- **Rationale**: Embedded schema within i9AuditTrailRecord. Same ingestion pattern applies.

---

## Summary

### Ingestion Types by Entity

| Entity | Ingestion Type | Cursor Field |
|--------|---------------|--------------|
| customTasks | snapshot | - |
| journeyDetails | snapshot | - |
| FMLARequest | snapshot | - |
| EmployeeCompEntryDTO | snapshot | - |
| EmployeeCompForceCommentDTO | cdc | lastModified |
| RoleResponse | snapshot | - |
| PBCReplicationData | cdc | lastKnownReplicationTimeStamp |
| SymbolicAccountData | cdc | lastModifiedTimestamp |
| EmployeeGroupingData | cdc | lastModifiedTimestamp |
| User (SCIM) | cdc | meta.lastModified |
| SCIM.Group | cdc | meta.lastModified |
| i9AuditTrailRecord | append | seqNo (ordering) |

### Pagination Methods

| API | Pagination Method |
|-----|-------------------|
| Custom Tasks | None |
| New Hire Journey | None |
| FMLA Request | None (no GET endpoint) |
| Employee Compensation | $skip, $top |
| RBP GenAI | None (limited result set) |
| Position Budgeting Control | $skip, $top |
| SCIM (Users/Groups) | startIndex, count |
| I-9 Audit Trail | $skip, $top |

### Notes

1. **FMLA Request**: No GET endpoints are defined. Only POST (create) and PATCH (update) operations are available.

2. **RBP GenAI**: POST-based query endpoints for permissions and groups. GET endpoint only for roles. Limited to top 5 results.

3. **SCIM API**: Follows SCIM 2.0 standard with filter support including meta.lastModified for incremental sync.

4. **I-9 Audit Trail**: Contains sensitive PII data (SSN, DOB). Audit records are append-only and immutable.

5. **Position Budgeting Control**: Supports incremental replication via lastKnownReplicationTimeStamp parameter.

6. **Employee Compensation**: Requires templateId as mandatory parameter. Uses $expand for nested entities.
