# SAP SuccessFactors API Documentation - Remaining APIs (Misc)

## Segment Overview
- **Segment**: 12 - Remaining APIs (Misc)
- **Files Processed**: 6
- **Entities Documented**: 15
- **Endpoints Documented**: 12

## API Files Summary

| File | API Type | Domain | Key Entities |
|------|----------|--------|--------------|
| PLTScim.json | REST (SCIM 2.0) | Identity Management | User, Group |
| PLTDPCS.json | REST | Data Privacy | DPCS Statement, Acknowledgement |
| ExtensionPoint.json | REST | Onboarding | Extension Task |
| InstructionalText.json | REST | Time Management | Instructional Text |
| UploadAttachment.json | REST | Time Management | Attachment |
| AdditionalServices.json | OData v4 | Onboarding | Username Service |

---

## Objects

### ScimUser
**Source File**: PLTScim.json
**API Type**: REST (SCIM 2.0)
**Base Path**: /rest/iam/scim/v2

#### Description
SCIM 2.0 compliant User resource for cross-domain identity management in SAP SuccessFactors. Manages user identities with support for multiple extension schemas including SAP-specific, Enterprise, and Workforce extensions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No (auto-generated) | Unique identifier for the user as defined by the service provider |
| externalId | string | No | Identifier for the user as defined by the provisioning client |
| userName | string | Yes | Unique identifier for the user |
| name | object | No | Components of the user's name (formatted, familyName, givenName, middleName, honorificPrefix, honorificSuffix) |
| displayName | string | No | Name suitable for display to end users |
| nickName | string | No | Nickname of the user |
| title | string | No | Title of the user |
| userType | string | No | Relationship between user and organization (EMPLOYEE, ONBOARDEE) |
| preferredLanguage | string | No | User's preferred language |
| locale | string | No | User's default location for localization |
| active | boolean | No | Whether the user has an active status |
| emails | array | No | Email addresses of the user (value, type, primary) |
| phoneNumbers | array | No | Phone numbers of the user (value, type, primary) |
| groups | array | No (read-only) | Groups to which the user belongs |
| meta | object | No (read-only) | Resource metadata (resourceType, created, lastModified, location, version) |
| schemas | array | Yes | URIs indicating SCIM schemas for the resource |

**Extension Schemas:**
- `urn:ietf:params:scim:schemas:extension:successfactors:2.0:User`: perPersonUuid, loginMethod, personIdExternal, customFields
- `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`: department, division, manager, employeeNumber
- `urn:ietf:params:scim:schemas:extension:sap:2.0:User`: userUuid, groupDomains, sourceSystem
- `urn:ietf:params:scim:schemas:extension:sap.workforce:2.0:User`: lastDeactivated
- `urn:ietf:params:scim:schemas:extension:sap.odm:2.0:User`: workforcePersonId

#### Primary Keys
- `id` (string) - UUID format

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: `meta.lastModified`
- **Rationale**: Has lastModified timestamp in meta object for tracking changes. Supports filtering by lastModified for incremental reads.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/iam/scim/v2/Users | Get Users by Criteria | startIndex/count (index-based) or startId/count/nextId (ID-based) |
| GET | /rest/iam/scim/v2/Users/{id} | Get a User by ID | None |
| POST | /rest/iam/scim/v2/Users | Create a User | N/A |
| PUT | /rest/iam/scim/v2/Users/{id} | Replace a User | N/A |
| PATCH | /rest/iam/scim/v2/Users/{id} | Modify a User | N/A |
| DELETE | /rest/iam/scim/v2/Users/{id} | Delete a User | N/A |
| POST | /rest/iam/scim/v2/Users/.search | Get Users by Search (POST) | startIndex/count or startId/count/nextId |

#### Pagination Details
- **Index-based**: Use `startIndex` (1-based) and `count` (default 100)
- **ID-based**: Use `startId=initial` or `startId=<user-id>` with `count`; response includes `nextId` for next page (`end` indicates last page)
- **Response fields**: `totalResults`, `itemsPerPage`, `startIndex` or `startId/nextId`, `Resources`

#### Filter Support
Supported operators: `eq`, `ne`, `gt`, `co`, `sw`, `ew`, `and`, `or`
Filterable attributes: `id`, `userName`, `userType`, `active`, `meta.lastModified`, `urn:ietf:params:scim:schemas:extension:sap:2.0:User:userUuid`, `urn:ietf:params:scim:schemas:extension:sap:2.0:User:groupDomains`, `urn:ietf:params:scim:schemas:extension:successfactors:2.0:User:perPersonUuid`, `urn:ietf:params:scim:schemas:extension:sap.workforce:2.0:User:lastDeactivated`

---

### ScimGroup
**Source File**: PLTScim.json
**API Type**: REST (SCIM 2.0)
**Base Path**: /rest/iam/scim/v2

#### Description
SCIM 2.0 compliant Group resource representing permission groups in SAP SuccessFactors. Supports static and dynamic permission groups with read or read-write operations.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | No (auto-generated) | Unique identifier of the permission group |
| displayName | string | No | Name of the group (equals "Group Name" in admin page) |
| members | array | Yes | Members of the group (value, $ref, type) |
| meta | object | No (read-only) | Resource metadata including members.cnt and members.nextId |
| schemas | array | Yes | URIs indicating SCIM schemas for the resource |

**Extension Schema:**
- `urn:ietf:params:scim:schemas:extension:sap:2.0:Group`: type (userGroup, deepLinkActivationPermission, embeddedAnalyticsAccessPermission, mobileAccessPermission), supportedOperations (readOnly, readWrite)

#### Primary Keys
- `id` (string) - Numeric group ID

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: `meta.lastModified`
- **Rationale**: Has lastModified timestamp in meta object. Supports filtering by meta.lastModified.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/iam/scim/v2/Groups | Query Permission Groups | startIndex/count or startId/count/nextId |
| GET | /rest/iam/scim/v2/Groups/{id} | Retrieve a Known Permission Group | Member pagination via attributes parameter |
| PUT | /rest/iam/scim/v2/Groups/{id} | Replace members of a Known Permission Group | N/A |
| PATCH | /rest/iam/scim/v2/Groups/{id} | Modify Members of a Known Permission Group | N/A |

#### Pagination Details
- **Group pagination**: Similar to Users with startIndex/count or startId/count/nextId
- **Member pagination**: Use `attributes=members[startId=initial&count=100]` (max 100 for list, max 1000 for single group)
- **Response fields**: `meta.members.cnt` (total member count), `meta.members.nextId` (next member ID or "end")

#### Filter Support
Supported operators: `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `co`, `sw`, `ew`, `and`, `or`
Filterable attributes: `displayName`, `meta.lastModified`, `urn:ietf:params:scim:schemas:extension:sap:2.0:Group:type`

---

### DPCSVersion (Data Privacy Consent Statement)
**Source File**: PLTDPCS.json
**API Type**: REST
**Base Path**: /rest/security/privacy/v1

#### Description
Data Privacy Consent Statement (DPCS) API for managing data privacy consent statements and user acknowledgements. Supports RECRUITING_EXTERNAL and PROFILE_PHOTO statement types.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | integer (int64) | Yes (key) | Identifier of the DPCS |
| version | integer (int32) | No | Version number of the DPCS |
| customFieldType | string | No | Type of customized fields (max 200 chars) |
| template | object | No | DPCS template (id, name, type, status, forceAccept) |
| contents | array | No | List of DPCS content objects |
| attributes | array | No | List of DPCS attribute objects |

**Template Schema:**
| Field | Type | Description |
|-------|------|-------------|
| id | integer (int64) | Identifier of DPCS template |
| name | string | Name of template (max 100 chars) |
| type | integer (int32) | Type of DPCS (0-8; 2=Recruiting external, 8=Profile photo) |
| status | integer (int32) | Status (0=disabled, 1=enabled, 2=deleted) |
| forceAccept | integer (int32) | Whether to force display (0=false, 1=true) |

**Content Schema:**
| Field | Type | Description |
|-------|------|-------------|
| id | integer (int64) | Identifier of DPCS content |
| statementId | integer (int64) | Version ID of the DPCS |
| locale | string | Language of the content (max 32 chars) |
| title | string | Title of the content (max 100 chars) |
| content | string | Content of the DPCS (max 50000 chars) |

**Attribute Schema:**
| Field | Type | Description |
|-------|------|-------------|
| id | integer (int64) | Identifier of the attribute |
| statementId | integer (int64) | Version ID of the DPCS |
| attributeName | string | Name of the attribute (max 100 chars) |
| attributeValue | string | Value of the attribute (max 100 chars) |

#### Primary Keys
- `id` (integer)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: No modification tracking fields available. Statements are versioned but no timestamp-based change tracking.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/security/privacy/v1/statements | View details of data privacy consent statements | None |

#### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | string | Yes | DPCS type (RECRUITING_EXTERNAL, PROFILE_PHOTO) |
| country | string | Yes | Alpha 3 country code (e.g., CHN, USA) |
| customFieldValue | string | No | Custom field value |
| language | string | No | Locale to filter contents (e.g., en_US, zh_CN_SF) |

---

### DPCSStatus (Data Privacy Consent Acknowledgement)
**Source File**: PLTDPCS.json
**API Type**: REST
**Base Path**: /rest/security/privacy/v1

#### Description
Represents the acknowledgement status of a data privacy consent statement for a specific user/subject.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | integer (int32) | No | Status of the DPCS (0=DECLINE, 1=ACCEPT, 2=REVOKE, 3=NOT PRESENTED) |
| statement | object | No | The associated DPCSVersion object |

#### Primary Keys
- Composite: `type` + `country` + `subjectId` (query parameters)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Status can be queried per subject but no change tracking mechanism is exposed.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/security/privacy/v1/acknowledgements | Gets the status of a data privacy consent statement | None |
| POST | /rest/security/privacy/v1/acknowledgements | Updates the status of a data privacy consent statement | N/A |

#### Query Parameters (GET)
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | string | Yes | DPCS type (RECRUITING_EXTERNAL, PROFILE_PHOTO) |
| country | string | Conditional | Alpha 3 country code (required for RECRUITING_EXTERNAL) |
| subjectId | string | Yes | Subject identifier (userId, assignmentId, or candidateId) |
| customFieldValue | string | No | Custom field value |
| language | string | No | Locale (e.g., en_US) |

---

### ExtensionPointTaskDetail
**Source File**: ExtensionPoint.json
**API Type**: REST
**Base Path**: /rest/onboarding/processes/v1

#### Description
Represents an extension task in the onboarding process. Allows retrieval and processing of extension tasks for new hires, including completing or canceling tasks.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| taskId | string | No | Extension task ID |
| taskType | string (enum) | No | Type of task: HIRING_MANAGER_REVIEW_EXTENSION, PERSONAL_DATA_COLLECTION_EXTENSION |
| processStatus | string (enum) | No | Status: SCHEDULED, IN_PROGRESS, COMPLETED, CANCELLED_POST_COMPLETION, CANCELLED, SKIPPED, DECLINED, CLOSED |
| comments | string | No (write-only) | Comments for the task |
| eventReason | string | No (write-only) | Event reason for the task |
| status | string (enum) | No (write-only) | Action status: RESUME, CANCEL |

#### Primary Keys
- `taskId` (string) - within the context of a processId

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Task status can change but no timestamp-based tracking. Must query by processId.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/onboarding/processes/v1/processes/{processId}/tasks | Retrieve Extension Tasks for a process | None |
| PATCH | /rest/onboarding/processes/v1/processes/{processId}/tasks/{taskId} | Update Extension Task Status | N/A |

#### Query Parameters (GET)
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| processId | string (path) | Yes | Process ID |
| $filter | string | No | Task type filter |

---

### InstructionalTextEO
**Source File**: InstructionalText.json
**API Type**: REST
**Base Path**: /rest/timemanagement/absence/v1

#### Description
Instructional text defined in the time profile object to help employees correctly request absences. Returns localized text based on the employee's configuration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| instructionalText | string | No | Localized instructional text content |

#### Primary Keys
- None (query-based retrieval by date)

#### Ingestion Type
- **Type**: snapshot
- **Rationale**: Configuration data retrieved based on date. No modification tracking.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /rest/timemanagement/absence/v1/instructionalTextsForEmployeeSelfService | Gets localized instructional text for employee self-service | None |

#### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| $at | string | Yes | Date for which instructional text is requested (YYYY-MM-DD format) |

---

### AttachmentUploadRequest
**Source File**: UploadAttachment.json
**API Type**: REST
**Base Path**: /rest/timemanagement/absence/v1

#### Description
Request object for uploading files that can be used as content for custom fields on absence requests. Supports both JSON (base64) and multipart/form-data upload methods.

#### Schema (JSON Upload)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| fileName | string | No | Name of file to be uploaded |
| attachmentContent | string (byte) | No | Attachment content as base64 string |

#### Schema (Multipart Upload)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| attachment | string (binary) | No | The file to be uploaded |

#### Response Schema (SuccessfulUploadResponse)
| Field | Type | Description |
|-------|------|-------------|
| attachmentId | integer | ID of the uploaded attachment |

#### Primary Keys
- `attachmentId` (integer) - returned after upload

#### Ingestion Type
- **Type**: N/A (Write-only API)
- **Rationale**: This is an upload-only endpoint. No GET method available for retrieving attachments.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| POST | /rest/timemanagement/absence/v1/attachment/upload | Uploads a file and returns attachment ID | N/A |

---

### AdditionalServices (Username Service)
**Source File**: AdditionalServices.json
**API Type**: OData v4
**Base Path**: /odatav4/onboarding/AdditionalServices.svc/v1

#### Description
Service for fetching or updating the internal username of new hires after the hiring process is completed. Used after the Manage Pending Hires process.

#### Service Operations

**getUserNameOfNewlyHiredEmployee (Function)**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| userId | string | Yes | User ID of the newly hired employee |

**Response**: string (username)

**updateUserNamePostHiring (Action)**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| userId | string | No | User ID |
| userName | string | No | New username to set |

**Response**: string

#### Primary Keys
- N/A (Service operations, not entity sets)

#### Ingestion Type
- **Type**: N/A (Service operations only)
- **Rationale**: These are unbound functions/actions, not entity sets. The API is used for username management operations, not bulk data retrieval.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /getUserNameOfNewlyHiredEmployee(userId='{userId}') | Fetch username of onboarding new hire | None |
| POST | /updateUserNamePostHiring | Update internal username of new hire | N/A |
| POST | /$batch | Send batch requests | N/A |

#### OData Parameters
Standard OData v4 parameters available:
- `$top`: Limit number of items
- `$skip`: Skip first n items
- `$count`: Include count of items
- `$search`: Search items by phrases

---

## Error Response Schemas

### SCIM Error Response
**Used by**: PLTScim.json

| Field | Type | Description |
|-------|------|-------------|
| schemas | array | Contains "urn:ietf:params:scim:api:messages:2.0:Error" |
| scimType | string | Error type (e.g., invalidValue, invalidFilter, uniqueness) |
| detail | string | Error message |
| status | integer | HTTP status code |

### Standard REST Error Response
**Used by**: PLTDPCS.json, ExtensionPoint.json, InstructionalText.json, UploadAttachment.json

| Field | Type | Description |
|-------|------|-------------|
| error.code | string | Error code |
| error.message | string | Error message |
| error.details | array | Additional error details (optional) |

### OData v4 Error Response
**Used by**: AdditionalServices.json

| Field | Type | Description |
|-------|------|-------------|
| error.code | string | Error code (e.g., NotFound) |
| error.message | string | Error message |
| error.details | array | Additional error details with code and message |

---

## Authentication Summary

| API | Authentication Method |
|-----|----------------------|
| PLTScim | Basic Auth or X.509 Certificate |
| PLTDPCS | Basic Auth |
| ExtensionPoint | Bearer Token (OAuth 2.0) |
| InstructionalText | OAuth 2.0 Client Credentials |
| UploadAttachment | OAuth 2.0 Client Credentials |
| AdditionalServices | Basic Auth |

---

## Rate Limiting

| API | Rate Limit |
|-----|------------|
| PLTScim | 20 calls per second per user account |
| Others | Not explicitly documented |

---

## Ingestion Recommendations Summary

| Entity | Ingestion Type | Cursor Field | Notes |
|--------|---------------|--------------|-------|
| ScimUser | cdc | meta.lastModified | Use ID-based pagination with startId for large datasets |
| ScimGroup | cdc | meta.lastModified | Use ID-based pagination; member pagination separate |
| DPCSVersion | snapshot | N/A | Query by type and country |
| DPCSStatus | snapshot | N/A | Query by type, country, and subjectId |
| ExtensionPointTaskDetail | snapshot | N/A | Query by processId |
| InstructionalTextEO | snapshot | N/A | Query by date |
| AttachmentUploadRequest | N/A | N/A | Write-only API |
| AdditionalServices | N/A | N/A | Service operations only |

---

## Key Implementation Notes

1. **SCIM APIs**: Follow SCIM 2.0 RFC 7643/7644 standards. Content-Type should be `application/scim+json`.

2. **Pagination Strategy for SCIM**:
   - For large datasets (>10K records), use ID-based pagination (`startId`) instead of index-based (`startIndex`)
   - ID-based pagination is more reliable for concurrent modifications
   - Check `nextId` value - "end" indicates last page

3. **User Extension Schemas**: The SuccessFactors extension schema is being deprecated in favor of SAP Workforce schema. Plan for migration.

4. **Group Operations**: Only static permission groups support write operations (readWrite). Dynamic groups are read-only.

5. **DPCS Types**: Currently only supports RECRUITING_EXTERNAL (type=2) and PROFILE_PHOTO (type=8).

6. **Extension Point API**: Requires specific process context. Cannot query across all processes.

7. **Attachment Upload**: Returns only attachmentId. The attachment must be associated with absence requests via separate APIs.
