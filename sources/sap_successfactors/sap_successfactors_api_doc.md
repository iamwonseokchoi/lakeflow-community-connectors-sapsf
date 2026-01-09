# SAP SuccessFactors API Documentation

## Authorization

### Authentication Methods

SAP SuccessFactors APIs support multiple authentication methods:

#### 1. Basic Authentication (Recommended for Connectors)
- **Username Format**: `{userId}@{companyId}`
- **Password**: API Key or user password
- **Header**: `Authorization: Basic <base64(username:password)>`

```http
GET /odata/v2/EmpEmployment HTTP/1.1
Host: api17.sapsf.com
Authorization: Basic dXNlckBjb21wYW55OnBhc3N3b3Jk
Content-Type: application/json
```

#### 2. OAuth 2.0 SAML Bearer Assertion
- **Grant Type**: `urn:ietf:params:oauth:grant-type:saml2-bearer`
- **Token Endpoint**: `https://{api-server}/oauth/token`
- Used for programmatic access with SAML assertions

#### 3. OAuth 2.0 Client Credentials
- **Grant Type**: `client_credentials`
- **Token Endpoint**: `https://{api-server}/oauth/token`
- Used for REST APIs (Time Management, Onboarding)

### API Server Endpoints

| Data Center | API Server URL |
|-------------|----------------|
| US (DC2) | `https://api2.successfactors.com` |
| US (DC4) | `https://api4.successfactors.com` |
| US (DC8) | `https://api8.successfactors.com` |
| US (DC10) | `https://api10.successfactors.com` |
| US (DC12) | `https://api12.successfactors.com` |
| EU (DC15) | `https://api15.sapsf.eu` |
| EU (DC17) | `https://api17.sapsf.com` |
| EU (DC18) | `https://api18.sapsf.eu` |
| APAC (DC19) | `https://api19.sapsf.com` |

### URL Patterns by API Type

| Protocol | URL Pattern | Example |
|----------|-------------|---------|
| OData v2 | `/odata/v2/{EntitySet}` | `https://api17.sapsf.com/odata/v2/EmpEmployment` |
| OData v4 | `/odatav4/{service}/v1/{EntitySet}` | `https://api17.sapsf.com/odatav4/onboarding/AdditionalServices.svc/v1` |
| REST | `/rest/{module}/{version}/{resource}` | `https://api17.sapsf.com/rest/timemanagement/absence/v1/events` |
| SCIM 2.0 | `/rest/iam/scim/v2/{resource}` | `https://api17.sapsf.com/rest/iam/scim/v2/Users` |

---

## Object List

### Summary Statistics

| API Type | Files | Entities | Endpoints |
|----------|-------|----------|-----------|
| OData v2 | 41 | ~450 | ~900 |
| OData v4 | 6 | ~25 | ~31 |
| REST | 20 | ~75 | ~50 |
| **Total** | **67** | **~550** | **~981** |

### Master Object Index

#### Employee Central Core (Segment 1)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| EmpEmployment | OData v2 | personIdExternal, userId | cdc | lastModifiedDateTime |
| EmpEmploymentTermination | OData v2 | endDate, personIdExternal, userId | cdc | lastModifiedDateTime |
| EmpJob | OData v2 | seqNumber, startDate, userId | cdc | lastModifiedDateTime |
| EmpWorkPermit | OData v2 | country, documentNumber, documentType, userId | cdc | lastModifiedDateTime |
| EmpJobRelationships | OData v2 | relationshipType, startDate, userId | cdc | lastModifiedDateTime |
| EmpBeneficiary | OData v2 | userId | cdc | lastModifiedDateTime |
| EmpPensionPayout | OData v2 | userId | cdc | lastModifiedDateTime |
| PersonEmpTerminationInfo | OData v2 | personIdExternal | snapshot | N/A |
| HireDateChange | OData v2 | code | cdc | lastModifiedDateTime |
| EmployeePayrollRunResults | OData v2 | externalCode, mdfSystemEffectiveStartDate | cdc | lastModifiedDateTime |
| EmployeePayrollRunResultsItems | OData v2 | Parent keys + externalCode | cdc | lastModifiedDateTime |
| EmployeeDismissalProtection | OData v2 | workerId | cdc | lastModifiedDateTime |
| EmployeeDismissalProtectionDetail | OData v2 | workerId, externalCode | cdc | lastModifiedDateTime |
| EmpCostAssignment | OData v2 | effectiveStartDate, worker | cdc_with_deletes | lastModifiedDateTime |
| FODepartment | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FODivision | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOBusinessUnit | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOCompany | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOCostCenter | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOJobCode | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOLocation | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| FOPayGrade | OData v2 | externalCode, startDate | cdc | lastModifiedDateTime |
| Territory | OData v2 | territoryCode | snapshot | N/A |

#### Employee Central Extended (Segment 2)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| PaymentInformationV3 | OData v2 | effectiveStartDate, worker | cdc | lastModifiedDateTime |
| PaymentInformationDetailV3 | OData v2 | Parent keys + externalCode | cdc | lastModifiedDateTime |
| EmpCompensation | OData v2 | seqNumber, startDate, userId | cdc | lastModifiedDateTime |
| EmpCompensationCalculated | OData v2 | seqNumber, startDate, userId | cdc | lastModifiedDateTime |
| EmpPayCompRecurring | OData v2 | payComponent, seqNumber, startDate, userId | cdc | lastModifiedDateTime |
| EmpPayCompNonRecurring | OData v2 | payComponent, payDate, seqNumber, userId | cdc | lastModifiedDateTime |
| BenefitsProgramDetail | OData v2 | externalCode, effectiveStartDate | cdc | lastModifiedDateTime |
| SkillProfile | OData v2 | externalCode | cdc | lastModifiedDateTime |
| SkillEntity | OData v2 | externalCode | cdc | lastModifiedDateTime |
| EmpEmploymentHigherDuty | OData v2 | effectiveStartDate, userId | cdc_with_deletes | lastModifiedDateTime |

#### Platform Services Core (Segment 3)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| User | OData v2 | userId | cdc | lastModifiedDateTime |
| PerPerson | OData v2 | personIdExternal | cdc | lastModifiedDateTime |
| PerPersonal | OData v2 | personIdExternal, startDate | cdc | lastModifiedDateTime |
| PerEmail | OData v2 | emailType, personIdExternal | cdc | lastModifiedDateTime |
| PerPhone | OData v2 | personIdExternal, phoneType | cdc | lastModifiedDateTime |
| PerAddressDeflt | OData v2 | addressType, personIdExternal | cdc | lastModifiedDateTime |
| PerNationalId | OData v2 | cardType, country, personIdExternal | cdc | lastModifiedDateTime |
| PickList | OData v2 | picklistId | snapshot | N/A |
| PickListValueV2 | OData v2 | externalCode | cdc | lastModifiedDateTime |
| DynamicGroup | OData v2 | groupId | cdc | lastModifiedDateTime |
| Photo | OData v2 | photoType, userId | cdc | lastModified |
| Attachment | OData v2 | attachmentId | cdc | lastModifiedDateTime |

#### Platform Services Extended (Segment 4)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| Todo | OData v2 | categoryId | snapshot | N/A |
| TodoEntryV2 | OData v2 | todoEntryId | cdc | lastModifiedDateTime |
| SuccessStoreContent | OData v2 | contentId | snapshot | N/A |
| EMMonitoredProcess | OData v2 | processDefinitionId, processInstanceId, processType | cdc | lastEventTime |
| EMEvent | OData v2 | id | append | eventTime |
| ThemeInfo | OData v2 | id | cdc | lastModifiedDate |
| ThemeConfig | OData v2 | id | snapshot | N/A |
| CustomNav | OData v2 | title | snapshot | N/A |

#### Recruitment Management (Segment 5)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| Candidate | OData v2 | candidateId | cdc | lastModifiedDateTime |
| CandidateLight | OData v2 | candidateId | cdc | lastModifiedDateTime |
| JobApplication | OData v2 | applicationId | cdc | lastModifiedDateTime |
| JobApplicationAudit | OData v2 | auditId | append | createdDateTime |
| JobRequisition | OData v2 | jobReqId | cdc_with_deletes | lastModifiedDateTime |
| JobRequisitionOperator | OData v2 | operatorRole, recruiterId, jobReqId | cdc | lastModifiedDateTime |
| JobOffer | OData v2 | offerApprovalId | cdc | lastModifiedDateTime |
| InterviewOverallAssessment | OData v2 | interviewOverallAssessmentId | cdc | lastModifiedDateTime |
| JobApplicationInterview | OData v2 | applicationInterviewId | cdc | lastModifiedDateTime |

#### Performance Management (Segment 6)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| Goal_1 through Goal_1000 | OData v2 | id | cdc/snapshot | lastModified |
| GoalPlanTemplate | OData v2 | id | cdc | lastModified |
| Form360Participant | OData v2 | formContentId, formDataId, participantId | cdc | lastModifiedDateTime |
| FormContent | OData v2 | formContentId, formDataId | cdc | lastModifiedDateTime |
| FormHeader | OData v2 | formDataId | cdc | lastModifiedDateTime |
| FormReviewFeedbackList | OData v2 | formContentId, formDataId | cdc | lastModified |
| PMActivity | OData v2 | activityId | cdc | lastModifiedDateTime |
| PMReviewContentDetail | OData v2 | reviewContentDetailId | cdc | lastModified |
| AchievementDevGoalDetail | OData v2 | achievementDevGoalDetailId | cdc | lastModifiedDateTime |
| ContinuousFeedbackRequest | OData v2 | feedbackRequestId | cdc | lastModifiedDateTime |
| ContinuousFeedback | OData v2 | feedbackId | cdc | lastModifiedDateTime |

#### Time & Attendance (Segment 7)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| ClockInClockOutGroups | OData v4 | code | cdc | lastChangedAt |
| TimeEventTypes | OData v4 | code | snapshot | N/A |
| timeevents | OData v4 | externalId | append | lastChangedAt |
| TimeAccountBalanceResponse | REST | timeAccount.externalCode | snapshot | N/A |
| TimeTypeBalanceResponse | REST | timeType.externalCode | snapshot | N/A |
| TimeOffEventResponse | REST | externalCode | snapshot | N/A |
| AvailableTimeType | REST | externalCode | snapshot | N/A |

#### Succession & Development (Segment 8)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| TalentPool | OData v2 | poolId | cdc | lastModifiedDateTime |
| Successor | OData v2 | nomineeId, nomineeType, positionId | cdc | lastModifiedDateTime |
| Position | OData v2 | code, effectiveStartDate | cdc | lastModifiedDateTime |
| CalibrationSession | OData v4 | sessionId | cdc | lastModifiedDateTime |
| CalibrationSessionOwner | OData v4 | sessionId, ownerId | cdc | lastModifiedDateTime |
| SCMNominationApprovalWorkflow | OData v4 | approvalId | cdc | lastModifiedDateTime |

#### Onboarding (Segment 9)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| OnboardingProcess | OData v2 | onboardingProcessId | cdc | lastModifiedDateTime |
| OnboardingCandidateInfo | OData v2 | applicantId | cdc | lastModifiedDateTime |
| OnboardingNewHireActivitiesStep | OData v2 | processStepId, onboardingProcessId | cdc | lastModifiedDateTime |
| OnboardingMeetingActivity | OData v2 | activityId, processStepId, onboardingProcessId | cdc | lastModifiedDateTime |
| OnboardingEquipmentActivity | OData v2 | activityId, processStepId, onboardingProcessId | cdc | lastModifiedDateTime |
| ONB2Process | OData v2 | processId | cdc | lastModifiedDateTime |
| ONB2ProcessTask | OData v2 | ONB2Process_processId, taskId | cdc | lastModifiedDateTime |
| ONB2ProcessTrigger | OData v2 | triggerId | cdc | lastModifiedDateTime |
| ComplianceProcess | OData v2 | processId | cdc | lastModifiedDateTime |
| ComplianceFormData | OData v2 | externalCode | cdc | lastModifiedDateTime |
| ComplianceFormDataFieldValue | OData v2 | id | snapshot | N/A |

#### Finance & Operations (Segment 10)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field | Soft Delete |
|--------|----------|--------------|----------------|--------------|-------------|
| BudgetPeriodGO | OData v2 | budgetPeriodId, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |
| FunctionalAreaGO | OData v2 | functionalAreaID, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |
| FundCenterGO | OData v2 | externalCode, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |
| FundGO | OData v2 | externalCode, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |
| GrantGO | OData v2 | grantCode, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |
| ProjectControllingObject | OData v2 | externalCode, effectiveStartDate | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' |

#### REST Extended APIs (Segment 11)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| customTasks | REST | id | snapshot | N/A |
| journeyDetails | REST | journeyId | snapshot | N/A |
| FMLARequest | REST | Assignment Id, Id | snapshot | N/A |
| EmployeeCompEntryDTO | REST | compEntryId | snapshot | N/A |
| EmployeeCompForceCommentDTO | REST | compCommentId | cdc | lastModified |
| PBCReplicationData | REST | id, startDate, endDate | cdc | lastKnownReplicationTimeStamp |
| SymbolicAccountData | REST | id | cdc | lastModifiedTimestamp |
| EmployeeGroupingData | REST | id | cdc | lastModifiedTimestamp |
| User (SCIM) | REST | id | cdc | meta.lastModified |
| SCIM.Group | REST | id | cdc | meta.lastModified |
| i9AuditTrailRecord | REST | externalCode | append | seqNo |

#### Miscellaneous APIs (Segment 12)

| Entity | API Type | Primary Keys | Ingestion Type | Cursor Field |
|--------|----------|--------------|----------------|--------------|
| ScimUser | REST (SCIM 2.0) | id | cdc | meta.lastModified |
| ScimGroup | REST (SCIM 2.0) | id | cdc | meta.lastModified |
| DPCSVersion | REST | id | snapshot | N/A |
| DPCSStatus | REST | type + country + subjectId | snapshot | N/A |
| ExtensionPointTaskDetail | REST | taskId | snapshot | N/A |
| InstructionalTextEO | REST | N/A | snapshot | N/A |

---

## Object Schema

### Common MDF System Fields

Most OData v2 entities include these standard MDF system fields:

| Field | Type | Description |
|-------|------|-------------|
| createdBy | string | User who created the record |
| createdDateTime | DateTimeOffset | Timestamp of creation |
| lastModifiedBy | string | User who last modified the record |
| lastModifiedDateTime | DateTimeOffset | Timestamp of last modification |
| mdfSystemRecordStatus | string | Record status: N (Normal), D (Deleted), C (Correction), P (Pending) |
| mdfSystemEffectiveStartDate | Date | Start of effective period (for effective-dated entities) |
| mdfSystemEffectiveEndDate | Date | End of effective period (for effective-dated entities) |

### Schema Retrieval

SAP SuccessFactors provides schema information through OData metadata endpoints:

**OData v2 Metadata:**
```http
GET /odata/v2/$metadata HTTP/1.1
Host: {api-server}
Authorization: Basic <credentials>
```

**Entity-specific Schema:**
```http
GET /odata/v2/{EntitySet}?$select=* HTTP/1.1
Host: {api-server}
Authorization: Basic <credentials>
```

### Example Entity Schema: EmpJob

| Field | Type | Max Length | Required | Description |
|-------|------|------------|----------|-------------|
| seqNumber | Edm.Int64 | - | Yes | Sequence number |
| startDate | Edm.DateTime | - | Yes | Job start date |
| userId | Edm.String | 100 | Yes | User identifier |
| company | Edm.String | 32 | No | Company code |
| costCenter | Edm.String | 32 | No | Cost center |
| department | Edm.String | 32 | No | Department |
| division | Edm.String | 32 | No | Division |
| jobCode | Edm.String | 32 | No | Job code |
| jobTitle | Edm.String | 256 | No | Job title |
| location | Edm.String | 128 | No | Location |
| managerId | Edm.String | 256 | No | Manager user ID |
| position | Edm.String | 128 | No | Position code |
| emplStatus | Edm.String | 32 | No | Employment status |
| employeeClass | Edm.String | 256 | No | Employee class |
| fte | Edm.Double | - | No | Full-time equivalent |
| standardHours | Edm.Double | - | No | Standard weekly hours |
| lastModifiedDateTime | Edm.DateTimeOffset | - | No | Last modification timestamp |
| event | Edm.String | 32 | No | Event type |
| eventReason | Edm.String | - | No | Event reason |

---

## Get Object Primary Keys

### Key Pattern Categories

#### 1. Single Key Entities
Entities with a single primary key field:
- `User` - `userId`
- `Candidate` - `candidateId`
- `TalentPool` - `poolId`
- `OnboardingProcess` - `onboardingProcessId`

#### 2. Composite Key Entities
Entities with multiple key fields:
- `EmpJob` - (`seqNumber`, `startDate`, `userId`)
- `EmpEmployment` - (`personIdExternal`, `userId`)
- `FODepartment` - (`externalCode`, `startDate`)

#### 3. Effective-Dated Entities
Entities with time-based versioning:
- Include `effectiveStartDate` in composite key
- Support history tracking through date ranges
- Examples: `FOCompany`, `Position`, `PaymentInformationV3`

### Key Field Identification Methods

1. **OData $metadata**: Key fields marked with `<PropertyRef Name="fieldName"/>`
2. **Swagger/OpenAPI**: Fields marked with `x-sap-filterable: true` and `required: true`
3. **API Documentation**: Keys indicated in entity descriptions

---

## Object's Ingestion Type

### Ingestion Type Definitions

| Type | Description | Use Case |
|------|-------------|----------|
| `cdc` | Incremental with upserts only | Entities with `lastModifiedDateTime` cursor field |
| `cdc_with_deletes` | Incremental with upserts AND delete detection | Entities with `mdfSystemRecordStatus='D'` for soft deletes |
| `snapshot` | Full table read each sync | Entities without modification tracking |
| `append` | Incremental append-only | Log/event entities that are immutable after creation |

### Ingestion Type Distribution

| Ingestion Type | Count | Percentage |
|----------------|-------|------------|
| cdc | ~380 | 69% |
| cdc_with_deletes | ~30 | 5% |
| snapshot | ~120 | 22% |
| append | ~20 | 4% |

### Soft Delete Detection

For `cdc_with_deletes` entities, detect deleted records by filtering on:

```
$filter=mdfSystemRecordStatus eq 'D' and lastModifiedDateTime gt datetime'{last_sync}'
```

**mdfSystemRecordStatus Values:**
- `N` - Normal record
- `D` - Soft deleted record
- `C` - Correction record
- `P` - Pending record
- `PH` - Pending history record

---

## Read API for Data Retrieval

### OData v2 Query Operations

#### Basic Read
```http
GET /odata/v2/EmpEmployment HTTP/1.1
Host: {api-server}
Authorization: Basic <credentials>
Accept: application/json
```

#### Incremental Read (CDC)
```http
GET /odata/v2/EmpEmployment?$filter=lastModifiedDateTime gt datetime'2024-01-01T00:00:00Z'&$orderby=lastModifiedDateTime asc&$top=1000 HTTP/1.1
```

#### Read with Field Selection
```http
GET /odata/v2/EmpJob?$select=userId,jobCode,jobTitle,department,lastModifiedDateTime HTTP/1.1
```

#### Read with Expansion
```http
GET /odata/v2/User?$expand=directReports,manager,hr HTTP/1.1
```

### Pagination

#### OData v2 Pagination
| Parameter | Description | Default |
|-----------|-------------|---------|
| `$top` | Maximum records to return | 20 |
| `$skip` | Records to skip | 0 |
| `$inlinecount=allpages` | Include total count | N/A |

**Example:**
```http
GET /odata/v2/EmpJob?$top=1000&$skip=0&$inlinecount=allpages&$orderby=lastModifiedDateTime asc HTTP/1.1
```

**Response with Count:**
```json
{
  "d": {
    "__count": "15000",
    "results": [...]
  }
}
```

#### OData v4 Pagination
| Parameter | Description |
|-----------|-------------|
| `$top` | Maximum records |
| `$skip` | Records to skip |
| `$count=true` | Include count |
| `@odata.nextLink` | URL for next page |

#### REST API Pagination
| API Type | Parameters |
|----------|------------|
| Standard REST | `$skip`, `$top` |
| SCIM 2.0 | `startIndex`, `count` (1-based) |
| SCIM 2.0 (ID-based) | `startId`, `count`, `nextId` |

### SCIM 2.0 Pagination Example

**Index-based:**
```http
GET /rest/iam/scim/v2/Users?startIndex=1&count=100 HTTP/1.1
```

**ID-based (recommended for large datasets):**
```http
GET /rest/iam/scim/v2/Users?startId=initial&count=100 HTTP/1.1
```

Response includes `nextId` for next page; `"end"` indicates last page.

### Rate Limits

| API | Rate Limit |
|-----|------------|
| OData v2/v4 | Varies by data center; typically 100-300 req/min |
| SCIM 2.0 | 20 calls per second per user account |
| REST APIs | Varies by endpoint |

**Best Practices:**
- Implement exponential backoff for 429 responses
- Use batching where available ($batch endpoint)
- Request only necessary fields using $select

---

## Field Type Mapping

### OData EDM Types to Spark Types

| EDM Type | Spark Type | Notes |
|----------|------------|-------|
| Edm.String | StringType | |
| Edm.Int16 | ShortType | |
| Edm.Int32 | IntegerType | |
| Edm.Int64 | LongType | |
| Edm.Decimal | DecimalType(38, 18) | Precision may vary |
| Edm.Double | DoubleType | |
| Edm.Single | FloatType | |
| Edm.Boolean | BooleanType | |
| Edm.DateTime | TimestampType | ISO 8601 format |
| Edm.DateTimeOffset | TimestampType | With timezone |
| Edm.Date | DateType | OData v4 only |
| Edm.Time | StringType | Store as string |
| Edm.Binary | BinaryType | Base64 encoded |
| Edm.Guid | StringType | UUID format |

### SCIM Types to Spark Types

| SCIM Type | Spark Type |
|-----------|------------|
| string | StringType |
| integer | IntegerType |
| boolean | BooleanType |
| dateTime | TimestampType |
| reference | StringType |
| complex | StructType |

### REST API Types to Spark Types

| REST Type | Spark Type |
|-----------|------------|
| string | StringType |
| integer/int32 | IntegerType |
| int64 | LongType |
| number/double | DoubleType |
| boolean | BooleanType |
| date | DateType |
| date-time | TimestampType |
| array | ArrayType |
| object | StructType |

### Special Field Handling

#### Localized Fields
Fields with `_localized` suffix return values in user's locale:
- `description_localized`, `name_localized`
- Map to StringType

#### Navigation Properties
OData navigation properties representing relationships:
- Use $expand to include in response
- Map to ArrayType or StructType based on cardinality

#### Base64 Binary Fields
Fields containing binary data (attachments, photos):
- Encoded as Base64 strings
- Map to BinaryType after decoding

---

## Sources and References

### Official API Documentation
- **SAP SuccessFactors API Reference**: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM
- **OData v2 API Guide**: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b
- **SCIM 2.0 API**: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/568fdf1f14f14fd089a3cd15194d19cc
- **API Business Hub**: https://api.sap.com/package/SuccessFactorsHXM

### JSON API Specification Files Processed

| Category | Files | Source Path |
|----------|-------|-------------|
| OData v2 | 41 | `api_spec_docs/odatav2/` |
| OData v4 | 6 | `api_spec_docs/odatav4/` |
| REST | 20 | `api_spec_docs/rest/` |

### Detailed File Inventory

**Employee Central:**
- ECEmploymentInformation.json
- ECFoundationOrganization.json
- ECEmployeeCentralPayroll.json
- ECDismissalProtection.json
- EmpCostAssignment.json
- ECPaymentInformation.json
- ECCompensationInformation.json
- ECGlobalBenefits.json
- ECAdvances.json
- ECSkillsManagement.json

**Platform Services:**
- FoundationPlatformPLT.json
- PLTGenericObjects.json
- PLTUserManagement.json
- PLTSSO.json
- PLTRoleBasedPermissions.json
- PLTTodo.json
- PLTSuccessStore.json
- PLTExecutionManager.json
- PLTUserInterfaceThemes.json
- PLTCustomNavigation.json

**Talent Management:**
- RCMCandidate.json
- RCMJobApplication.json
- RCMJobRequisition.json
- RCMOffer.json
- PerformanceandGoalsPMGM.json
- PMFormsManagement.json
- SuccessionandDevelopmentSD.json
- SDSuccessionManagement.json
- SDCalibration.json

**Time & Onboarding:**
- OnboardingONB.json
- OnboardingOBX.json
- ClockInClockOutIntegration.json (OData v4)
- ClockInClockOutExternal.json (OData v4)
- TimeOffEvents.json (REST)
- Balances.json (REST)

**Finance & Operations:**
- BudgetPeriodGO.json
- FunctionalAreaGO.json
- FundCenterGO.json
- FundGO.json
- GrantGO.json
- ProjectControllingObject.json

**REST/SCIM:**
- PLTScim.json
- UserManagementSCIM.json
- i9audittrail.json
- sap-sf-customTasks-v2.json
- sap-sf-employeeCompensation-v1.json
- sap-sf-PositionBudgetingControl-v1.json

### Confidence Levels
- **Official SAP API Documentation**: Highest confidence
- **SAP API Business Hub OpenAPI Specs**: Highest confidence
- **JSON API Specification Files**: High confidence (67 files analyzed)
- **Segment Documentation**: High confidence (derived from JSON specs)

---

## Appendix: Implementation Notes

### Connector Best Practices

1. **Use lastModifiedDateTime for CDC**: Filter and order by this field for incremental sync
2. **Handle Composite Keys**: Many entities use multi-field keys; construct properly for updates
3. **Check mdfSystemRecordStatus**: For cdc_with_deletes entities, detect soft deletes via 'D' status
4. **Respect Rate Limits**: Implement backoff strategies for throttling
5. **Use $select**: Retrieve only needed fields to improve performance
6. **Batch Operations**: Use $batch endpoint for bulk reads where available

### Common Query Patterns

**Initial Full Load:**
```
/odata/v2/{Entity}?$top=1000&$skip=0&$orderby=lastModifiedDateTime asc
```

**Incremental Sync:**
```
/odata/v2/{Entity}?$filter=lastModifiedDateTime gt datetime'{cursor}'&$orderby=lastModifiedDateTime asc&$top=1000
```

**Deleted Records (cdc_with_deletes):**
```
/odata/v2/{Entity}?$filter=mdfSystemRecordStatus eq 'D' and lastModifiedDateTime gt datetime'{cursor}'
```

**Effective-Dated Current Records:**
```
/odata/v2/{Entity}?$filter=effectiveStartDate le datetime'{today}' and effectiveEndDate ge datetime'{today}'
```
