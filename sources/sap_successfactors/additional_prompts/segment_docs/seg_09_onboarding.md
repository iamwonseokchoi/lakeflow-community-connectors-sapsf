# SAP SuccessFactors API Documentation - Onboarding

## Segment Overview
- **Segment**: 9 - Onboarding
- **Files Processed**: 2 (OnboardingONB.json, OnboardingOBX.json)
- **Entities Documented**: 27
- **Endpoints Documented**: 54 (GET endpoints)

## API Files Summary

### OnboardingONB.json (Onboarding 1.0)
- **Description**: API to query and maintain onboarding activities of a candidate
- **Base Path**: /odata/v2
- **Entities**: 12 entities for legacy Onboarding 1.0

### OnboardingOBX.json (Onboarding 2.0)
- **Description**: API to query and manage Onboarding process and integrations
- **Base Path**: /odata/v2
- **Entities**: 15 entities for modern Onboarding 2.0

---

## Objects - OnboardingONB.json (Onboarding 1.0)

### OnboardingMeetingActivity
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingMeetingActivity

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| activityId | Edm.Int64 | Yes | Activity ID (composite key) |
| activityStatus | Edm.String | No | Status of the meeting activity |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| eventTriggered | Edm.Boolean | No | Whether event was triggered |
| externalName | Edm.String | No | External display name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| optional | Edm.Boolean | No | Whether activity is optional |

#### Primary Keys
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `activityId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes and composite primary keys for unique identification

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingMeetingActivity | Get entities from OnboardingMeetingActivity | $skip, $top |
| GET | /OnboardingMeetingActivity(...) | Get entity by composite key | N/A |

---

### OnboardingEquipmentActivity
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingEquipmentActivity

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| activityId | Edm.Int64 | Yes | Activity ID (composite key) |
| activityStatus | Edm.String | No | Status of the equipment activity |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| eventTriggered | Edm.Boolean | No | Whether event was triggered |
| externalName | Edm.String | No | External display name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| optional | Edm.Boolean | No | Whether activity is optional |

#### Primary Keys
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `activityId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes and composite primary keys

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingEquipmentActivity | Get entities from OnboardingEquipmentActivity | $skip, $top |
| GET | /OnboardingEquipmentActivity(...) | Get entity by composite key | N/A |

---

### OnboardingGoal
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingGoal

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingGoalActivity_activityId | Edm.Int64 | Yes | Goal activity ID (composite key) |
| OnboardingGoalCategory_externalCode | Edm.Int64 | Yes | Goal category code (composite key) |
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| goalId | Edm.Int64 | Yes | Goal ID (composite key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| text | Edm.String | No | Goal text (max 1000 chars) |

#### Primary Keys
- `OnboardingGoalActivity_activityId` (Edm.Int64)
- `OnboardingGoalCategory_externalCode` (Edm.Int64)
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `goalId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes with composite keys

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingGoal | Get entities from OnboardingGoal | $skip, $top |
| GET | /OnboardingGoal(...) | Get entity by composite key | N/A |

---

### OnboardingGoalCategory
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingGoalCategory

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingGoalActivity_activityId | Edm.Int64 | Yes | Goal activity ID (composite key) |
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| externalCode | Edm.Int64 | Yes | External code (composite key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| dueDaysAfterStart | Edm.Int64 | No | Days after start when goal is due |
| goalCategoryId | Edm.String | No | Goal category identifier |
| goalCategoryName | Edm.String | No | Goal category name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |

#### Primary Keys
- `OnboardingGoalActivity_activityId` (Edm.Int64)
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `externalCode` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingGoalCategory | Get entities from OnboardingGoalCategory | $skip, $top |
| GET | /OnboardingGoalCategory(...) | Get entity by composite key | N/A |

---

### OnboardingNewHireActivitiesStep
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingNewHireActivitiesStep

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| externalName | Edm.String | No | External display name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| processStepStatus | Edm.String | No | Status of the process step |

#### Primary Keys
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `processStepId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes with composite primary keys

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingNewHireActivitiesStep | Get entities from OnboardingNewHireActivitiesStep | $skip, $top |
| GET | /OnboardingNewHireActivitiesStep(...) | Get entity by composite key | N/A |

---

### OnboardingEquipmentTypeValue
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingEquipmentTypeValue

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | Edm.String | Yes | Equipment type value code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| description_defaultValue | Edm.String | No | Default description |
| description_localized | Edm.String | No | Localized description |
| description_* | Edm.String | No | Locale-specific descriptions (de_DE, en_US, etc.) |
| equipmentNotRequired | Edm.Boolean | No | Whether equipment is not required |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| type | Edm.String | No | Equipment type reference |

#### Primary Keys
- `code` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingEquipmentTypeValue | Get entities from OnboardingEquipmentTypeValue | $skip, $top |
| GET | /OnboardingEquipmentTypeValue('{code}') | Get entity by code | N/A |

---

### OnboardingMeetingEvent
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingMeetingEvent

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingMeetingActivity_activityId | Edm.Int64 | Yes | Meeting activity ID (composite key) |
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| externalCode | Edm.String | Yes | External code (composite key) |
| agenda | Edm.String | No | Meeting agenda |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| endDateTime | Edm.DateTimeOffset | No | Meeting end time |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| location | Edm.String | No | Meeting location |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| onboardingProcessMeetingTypeConfig | Edm.String | No | Meeting type configuration |
| participantUserId1-5 | Edm.String | No | Meeting participants (up to 5) |
| send | Edm.Boolean | No | Whether to send invitations |
| startDateTime | Edm.DateTimeOffset | No | Meeting start time |
| subject | Edm.String | No | Meeting subject |

#### Primary Keys
- `OnboardingMeetingActivity_activityId` (Edm.Int64)
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `externalCode` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingMeetingEvent | Get entities from OnboardingMeetingEvent | $skip, $top |
| GET | /OnboardingMeetingEvent(...) | Get entity by composite key | N/A |

---

### OnboardingGoalActivity
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingGoalActivity

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| activityId | Edm.Int64 | Yes | Activity ID (composite key) |
| activityStatus | Edm.String | No | Status of the goal activity |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| eventTriggered | Edm.Boolean | No | Whether event was triggered |
| externalName | Edm.String | No | External display name |
| goalActivityStatusSetManually | Edm.Boolean | No | Whether status was set manually |
| goalsTransferStatus | Edm.String | No | Goals transfer status |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| optional | Edm.Boolean | No | Whether activity is optional |

#### Primary Keys
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `activityId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingGoalActivity | Get entities from OnboardingGoalActivity | $skip, $top |
| GET | /OnboardingGoalActivity(...) | Get entity by composite key | N/A |

---

### OnboardingCandidateInfo
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingCandidateInfo

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| applicantId | Edm.String | Yes | Applicant ID (primary key) |
| candidateId | Edm.String | No | Candidate identifier |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| crossboarded | Edm.Boolean | No | Whether candidate is crossboarded |
| department | Edm.String | No | Department |
| division | Edm.String | No | Division |
| email | Edm.String | No | Email address |
| externalName_* | Edm.String | No | Localized external names |
| fName | Edm.String | No | First name |
| failedSEBEventsOccured | Edm.Boolean | No | Whether SEB events failed |
| fromExternalATS | Edm.Boolean | No | Whether from external ATS |
| globalAssignment | Edm.Boolean | No | Global assignment flag |
| hireDate | Edm.DateTimeOffset | No | Hire date |
| hired | Edm.Boolean | No | Whether candidate is hired |
| hrManagerId | Edm.String | No | HR Manager ID |
| internalHire | Edm.Boolean | No | Whether internal hire |
| jobReqId | Edm.String | No | Job requisition ID |
| jobTitle | Edm.String | No | Job title |
| kmsUserId | Edm.String | No | KMS user ID |
| lName | Edm.String | No | Last name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| location | Edm.String | No | Location |
| managerId | Edm.String | No | Manager ID |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| onboardingLocale | Edm.String | No | Onboarding locale |
| payGrade | Edm.String | No | Pay grade |
| processorId | Edm.String | No | Processor ID |
| readyToHire | Edm.Boolean | No | Whether ready to hire |
| userId | Edm.String | No | User ID |
| workCountry | Edm.String | No | Work country |

#### Primary Keys
- `applicantId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking candidate information changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingCandidateInfo | Get entities from OnboardingCandidateInfo | $skip, $top |
| GET | /OnboardingCandidateInfo('{applicantId}') | Get entity by applicantId | N/A |

---

### OnboardingEquipmentType
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingEquipmentType

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | Edm.String | Yes | Equipment type code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| description_defaultValue | Edm.String | No | Default description |
| description_localized | Edm.String | No | Localized description |
| description_* | Edm.String | No | Locale-specific descriptions |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |

#### Primary Keys
- `code` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking configuration changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingEquipmentType | Get entities from OnboardingEquipmentType | $skip, $top |
| GET | /OnboardingEquipmentType('{code}') | Get entity by code | N/A |

---

### OnboardingProcess
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingProcess

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (primary key) |
| candidateInfo | Edm.String | No | Candidate info reference |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| externalName | Edm.String | No | External display name |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| processConfig | Edm.String | No | Process configuration |
| processStatus | Edm.String | No | Process status |

#### Primary Keys
- `onboardingProcessId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking process changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingProcess | Get entities from OnboardingProcess | $skip, $top |
| GET | /OnboardingProcess({onboardingProcessId}) | Get entity by ID | N/A |

---

### OnboardingEquipment
**Source File**: OnboardingONB.json
**API Type**: OData v2
**Base Path**: /odata/v2/OnboardingEquipment

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| OnboardingEquipmentActivity_activityId | Edm.Int64 | Yes | Equipment activity ID (composite key) |
| OnboardingNewHireActivitiesStep_processStepId | Edm.Int64 | Yes | Process step ID (composite key) |
| OnboardingProcess_onboardingProcessId | Edm.Int64 | Yes | Onboarding process ID (composite key) |
| equipmentId | Edm.Int64 | Yes | Equipment ID (composite key) |
| comment | Edm.String | No | Equipment comment |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| type | Edm.String | No | Equipment type |
| value | Edm.String | No | Equipment value |
| workflow | Edm.String | No | Workflow reference |

#### Primary Keys
- `OnboardingEquipmentActivity_activityId` (Edm.Int64)
- `OnboardingNewHireActivitiesStep_processStepId` (Edm.Int64)
- `OnboardingProcess_onboardingProcessId` (Edm.Int64)
- `equipmentId` (Edm.Int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking equipment changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OnboardingEquipment | Get entities from OnboardingEquipment | $skip, $top |
| GET | /OnboardingEquipment(...) | Get entity by composite key | N/A |

---

## Objects - OnboardingOBX.json (Onboarding 2.0)

### ONB2EquipmentTypeValue
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2EquipmentTypeValue

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | Edm.String | Yes | Equipment type value code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| description_defaultValue | Edm.String | No | Default description |
| description_localized | Edm.String | No | Localized description |
| description_* | Edm.String | No | Locale-specific descriptions (ar_SA, de_DE, en_US, etc.) |
| inUse | Edm.String | No | Whether value is in use |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| type | Edm.String | No | Equipment type reference |

#### Primary Keys
- `code` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking configuration changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2EquipmentTypeValue | Get entities from ONB2EquipmentTypeValue | $skip, $top |
| GET | /ONB2EquipmentTypeValue('{code}') | Get entity by code | N/A |

---

### ComplianceFormDataFieldValue
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceFormDataFieldValue

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Edm.String | Yes | Field value ID (primary key) |
| value | Edm.String | No | Field value |

#### Primary Keys
- `id` (Edm.String)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field; requires full snapshot for consistency

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceFormDataFieldValue | Get entities from ComplianceFormDataFieldValue | $skip, $top |
| GET | /ComplianceFormDataFieldValue('{id}') | Get entity by id | N/A |

---

### ONB2Process
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2Process

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| processId | Edm.String | Yes | Process ID (primary key) |
| activitiesConfig | Edm.String | No | Activities configuration |
| activitiesStatus | Edm.String | No | Activities status |
| bpeProcessInstanceId | Edm.String | No | BPE process instance ID |
| cancelEventReason | Edm.String | No | Cancel event reason |
| cancelOffboardingReason | Edm.String | No | Cancel offboarding reason |
| cancelOnboardingReason | Edm.String | No | Cancel onboarding reason |
| cancellationComment | Edm.String | No | Cancellation comment |
| cancellationDate | Edm.DateTimeOffset | No | Cancellation date |
| cancelledDueToRestart | Edm.Boolean | No | Whether cancelled due to restart |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| customDataCollectionConfig | Edm.String | No | Custom data collection config |
| employeePersonId | Edm.Int64 | No | Employee person ID |
| endDate | Edm.DateTimeOffset | No | Process end date |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| locale | Edm.String | No | Locale |
| manager | Edm.String | No | Manager user ID |
| managerPersonId | Edm.Int64 | No | Manager person ID |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| offboardingActivitiesConfig | Edm.String | No | Offboarding activities config |
| onb2MasterId | Edm.String | No | ONB2 master ID |
| onboardingHireStatus | Edm.String | No | Onboarding hire status |
| onboardingHiredDate | Edm.DateTimeOffset | No | Hire date |
| onboardingInternalHire | Edm.Boolean | No | Whether internal hire |
| processRestarted | Edm.Boolean | No | Whether process was restarted |
| processStatus | Edm.String | No | Process status |
| processTrigger | Edm.String | No | Process trigger reference |
| processType | Edm.String | No | Process type |
| processVariant | Edm.String | No | Process variant |
| startDate | Edm.DateTimeOffset | No | Process start date |
| targetDate | Edm.DateTimeOffset | No | Target date |
| targetSystem | Edm.String | No | Target system |
| user | Edm.String | No | Subject user ID |

#### Primary Keys
- `processId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking process changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2Process | Get entities from ONB2Process | $skip, $top |
| GET | /ONB2Process('{processId}') | Get entity by processId | N/A |

---

### ONB2DataCollectionUserConfig
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2DataCollectionUserConfig

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Edm.String | Yes | Configuration ID (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| process | Edm.String | No | Process reference |
| subjectUser | Edm.String | No | Subject user ID |

#### Primary Keys
- `id` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking configuration changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2DataCollectionUserConfig | Get entities from ONB2DataCollectionUserConfig | $skip, $top |
| GET | /ONB2DataCollectionUserConfig('{id}') | Get entity by id | N/A |

---

### ONB2ProcessTask
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2ProcessTask

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ONB2Process_processId | Edm.String | Yes | Process ID (composite key) |
| taskId | Edm.String | Yes | Task ID (composite key) |
| completedBy | Edm.String | No | User who completed the task |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| endDate | Edm.DateTimeOffset | No | Task end date |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| responsibilityConfig | Edm.String | No | Responsibility configuration |
| startDate | Edm.DateTimeOffset | No | Task start date |
| status | Edm.String | No | Task status |
| type | Edm.String | No | Task type |

#### Primary Keys
- `ONB2Process_processId` (Edm.String)
- `taskId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking task changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2ProcessTask | Get entities from ONB2ProcessTask | $skip, $top |
| GET | /ONB2ProcessTask(ONB2Process_processId='{...}',taskId='{...}') | Get entity by composite key | N/A |

---

### ONB2EquipmentType
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2EquipmentType

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | Edm.String | Yes | Equipment type code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| description_defaultValue | Edm.String | No | Default description |
| description_localized | Edm.String | No | Localized description |
| description_* | Edm.String | No | Locale-specific descriptions |
| inUse | Edm.Boolean | No | Whether type is in use |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| ui5StandardIconId | Edm.String | No | UI5 standard icon ID |

#### Primary Keys
- `code` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking configuration changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2EquipmentType | Get entities from ONB2EquipmentType | $skip, $top |
| GET | /ONB2EquipmentType('{code}') | Get entity by code | N/A |

---

### ONB2ProcessTrigger
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2ProcessTrigger

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| triggerId | Edm.String | Yes | Trigger ID (primary key) |
| atsApplicationId | Edm.String | No | ATS application ID |
| atsUserId | Edm.String | No | ATS user ID |
| bpeProcessInstanceId | Edm.String | No | BPE process instance ID |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| hireType | Edm.String | No | Hire type |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| rcmApplicationId | Edm.String | No | RCM application ID |
| rcmCandidateId | Edm.String | No | RCM candidate ID |
| rcmCompany | Edm.String | No | RCM company |
| rcmHiringMgr | Edm.String | No | RCM hiring manager |
| rcmJobReqId | Edm.String | No | RCM job requisition ID |
| rcmOfferId | Edm.String | No | RCM offer ID |
| rcmPrimaryEmail | Edm.String | No | RCM primary email |
| rcmStartDate | Edm.DateTimeOffset | No | RCM start date |
| rehireUser | Edm.String | No | Rehire user ID |
| triggerStatus | Edm.String | No | Trigger status |
| triggerType | Edm.String | No | Trigger type |

#### Primary Keys
- `triggerId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking trigger changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2ProcessTrigger | Get entities from ONB2ProcessTrigger | $skip, $top |
| GET | /ONB2ProcessTrigger('{triggerId}') | Get entity by triggerId | N/A |

---

### ComplianceUserFormData
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceUserFormData

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Edm.String | Yes | Form data ID (primary key) |
| country | Edm.String | No | Country |
| createdDate | Edm.DateTimeOffset | No | Creation date |
| dataLastModifiedBy | Edm.String | No | User who last modified data |
| dataLastModifiedDate | Edm.DateTimeOffset | No | Data last modified date |
| documentFlowStatus | Edm.String | No | Document flow status |
| formId | Edm.String | No | Form ID |
| formVersion | Edm.String | No | Form version |
| initiatorId | Edm.String | No | Initiator ID |
| initiatorType | Edm.String | No | Initiator type |
| name | Edm.String | No | Form name |
| processId | Edm.String | No | Process ID |
| processStatus | Edm.String | No | Process status |
| state | Edm.String | No | State |
| user | Edm.String | No | User ID |
| year | Edm.String | No | Year |

#### Primary Keys
- `id` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: dataLastModifiedDate
- **Rationale**: Entity has dataLastModifiedDate for tracking form data changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceUserFormData | Get entities - compliance forms and compliance-related user data | $skip, $top |
| GET | /ComplianceUserFormData('{id}') | Get entity by id | N/A |

---

### ONB2EquipmentActivity
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ONB2EquipmentActivity

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| activityId | Edm.String | Yes | Activity ID (primary key) |
| activityStatus | Edm.String | No | Activity status |
| activityStatusDate | Edm.DateTimeOffset | No | Activity status date |
| activityTitle | Edm.String | No | Activity title |
| activityType | Edm.String | No | Activity type |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| dueDate | Edm.DateTimeOffset | No | Due date |
| equipmentComment | Edm.String | No | Equipment comment |
| equipmentStatus | Edm.String | No | Equipment status |
| equipmentType | Edm.String | No | Equipment type reference |
| equipmentValue | Edm.String | No | Equipment value reference |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| lastNudgedBy | Edm.String | No | User who last nudged |
| lastNudgedDate | Edm.DateTimeOffset | No | Last nudge date |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| notNeededComment | Edm.String | No | Not needed comment |
| optional | Edm.Boolean | No | Whether optional |
| process | Edm.String | No | Process reference |
| responsibleUsers | Edm.String | No | Responsible users |
| subjectUser | Edm.String | No | Subject user |

#### Primary Keys
- `activityId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking activity changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ONB2EquipmentActivity | Get entities from ONB2EquipmentActivity | $skip, $top |
| GET | /ONB2EquipmentActivity('{activityId}') | Get entity by activityId | N/A |

---

### ComplianceProcess
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceProcess

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| processId | Edm.String | Yes | Process ID (primary key) |
| complianceMasterId | Edm.String | No | Compliance master ID |
| correctDataTriggered | Edm.Boolean | No | Whether correct data was triggered |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| eVerifyData | Edm.String | No | E-Verify data |
| i9UserData | Edm.String | No | I-9 user data |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| onboardingProcess | Edm.String | No | Onboarding process reference |
| processInitiatorId | Edm.String | No | Process initiator ID |
| processInitiatorType | Edm.String | No | Process initiator type |
| processStatus | Edm.String | No | Process status |
| processType | Edm.String | No | Process type |
| startDate | Edm.DateTimeOffset | No | Start date |
| user | Edm.String | No | User ID |

#### Primary Keys
- `processId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking compliance workflow changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceProcess | Get entities - compliance workflow assigned to new hire | $skip, $top |
| GET | /ComplianceProcess('{processId}') | Get entity by processId | N/A |

---

### ComplianceProcessTask
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceProcessTask

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| taskId | Edm.String | Yes | Task ID (primary key) |
| category | Edm.String | No | Task category |
| completedBy | Edm.String | No | User who completed the task |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| dueDate | Edm.DateTimeOffset | No | Due date |
| endDate | Edm.DateTimeOffset | No | End date |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| process | Edm.String | No | Process reference |
| startDate | Edm.DateTimeOffset | No | Start date |
| status | Edm.String | No | Task status |
| subjectUser | Edm.String | No | Subject user |
| type | Edm.String | No | Task type |

#### Primary Keys
- `taskId` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking compliance task changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceProcessTask | Get entities - store start time, end time, and status of compliance task | $skip, $top |
| GET | /ComplianceProcessTask('{taskId}') | Get entity by taskId | N/A |

---

### AssignedComplianceForm
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/AssignedComplianceForm

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Edm.String | Yes | Assignment ID (primary key) |
| bpeUserTaskId | Edm.String | No | BPE user task ID |
| complianceFormName | Edm.String | No | Compliance form name |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| dueDate | Edm.DateTimeOffset | No | Due date |
| form | Edm.String | No | Form reference |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| order | Edm.Int32 | No | Form order |
| participantType | Edm.String | No | Participant type |
| preRequisiteFormNames | Edm.String | No | Pre-requisite form names |
| process | Edm.String | No | Process reference |
| rank | Edm.Int32 | No | Rank |
| responsibleUser | Edm.String | No | Responsible user |
| status | Edm.String | No | Form status |
| subjectUser | Edm.String | No | Subject user |

#### Primary Keys
- `id` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking compliance form assignment changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /AssignedComplianceForm | Get entities - compliance forms assigned to new hires | $skip, $top |
| GET | /AssignedComplianceForm('{id}') | Get entity by id | N/A |

---

### ComplianceFormData
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceFormData

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | Edm.String | Yes | External code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| documentAttachmentId | Edm.String | No | Document attachment ID |
| documentFlow | Edm.String | No | Document flow reference |
| envelopeId | Edm.String | No | Envelope ID |
| form | Edm.String | No | Form reference |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| pdfId | Edm.String | No | PDF ID |
| pdfLocaleMetadata | Edm.String | No | PDF locale metadata |
| process | Edm.String | No | Process reference |
| sensitiveDataIncluded | Edm.Boolean | No | Whether sensitive data is included |
| subjectUser | Edm.String | No | Subject user |

#### Primary Keys
- `externalCode` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking compliance form data changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceFormData | Get entities - stores compliance form data for new hire | $skip, $top |
| GET | /ComplianceFormData('{externalCode}') | Get entity by externalCode | N/A |

---

### ComplianceDocumentFlow
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceDocumentFlow

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| documentFlowCode | Edm.String | Yes | Document flow code (primary key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| declinedBy | Edm.String | No | User who declined |
| declinedDocuments | Edm.String | No | Declined documents |
| declinedReason | Edm.String | No | Decline reason |
| docFlowBpeUserTaskId | Edm.String | No | Doc flow BPE user task ID |
| documentFlowStatus | Edm.String | No | Document flow status |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| process | Edm.String | No | Process reference |
| subjectUser | Edm.String | No | Subject user |

#### Primary Keys
- `documentFlowCode` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking document flow changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceDocumentFlow | Get entities - stores compliance document flow assigned to new hire | $skip, $top |
| GET | /ComplianceDocumentFlow('{documentFlowCode}') | Get entity by documentFlowCode | N/A |

---

### ComplianceFormSignature
**Source File**: OnboardingOBX.json
**API Type**: OData v2
**Base Path**: /odata/v2/ComplianceFormSignature

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ComplianceFormData_externalCode | Edm.String | Yes | Compliance form data external code (composite key) |
| externalCode | Edm.String | Yes | External code (composite key) |
| createdBy | Edm.String | No | User who created the record |
| createdDateTime | Edm.DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | Edm.String | No | User who last modified the record |
| lastModifiedDateTime | Edm.DateTimeOffset | No | Last modification timestamp |
| mdfSystemRecordStatus | Edm.String | No | MDF system record status |
| signatureStatus | Edm.String | No | Signature status |
| signatureUser | Edm.String | No | Signature user |
| signatureUserFullName | Edm.String | No | Signature user full name |
| signatureUserRole | Edm.String | No | Signature user role |

#### Primary Keys
- `ComplianceFormData_externalCode` (Edm.String)
- `externalCode` (Edm.String)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Entity has lastModifiedDateTime for tracking signature changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ComplianceFormSignature | Get entities - stores compliance form signature assigned to new hire | $skip, $top |
| GET | /ComplianceFormSignature(ComplianceFormData_externalCode='{...}',externalCode='{...}') | Get entity by composite key | N/A |

---

## Service Operations (Function Imports)

### initiateOnboardingForUser
**Source File**: OnboardingOBX.json
**Method**: POST
**Description**: After an external user record is created and Employee Central data is added to the record, you can use this function import to initiate onboarding process from an external Application Tracking System. It modifies the ONB2Process and ONB2ProcessTrigger MDF objects. All Employee Central entities (PerPerson, EmpJob, EmpEmployment) should be upserted prior to this call.

### createOnboardee
**Source File**: OnboardingOBX.json
**Method**: POST
**Description**: This function import enables you to create an onboarding external user record in the system with information collected from your external Applicant Tracking System (ATS). It also enables you to perform preliminary checks to understand if the onboardee is a new hire or a rehire and take actions as necessary.

### updateFromExternalHrisONB
**Source File**: OnboardingOBX.json
**Method**: POST
**Description**: After a candidate is hired in the external Human Resources Information System (HRIS), you can use this function import to update the hiring data from the External HRIS system.

---

## Pagination

All collection endpoints support standard OData v2 pagination parameters:
- `$top`: Limit the number of results (default: 20 for ONB, 5 for OBX)
- `$skip`: Skip a number of results for pagination
- `$count`: Include total count of results
- `$filter`: Filter results based on field values
- `$search`: Search items by search phrases
- `$orderby`: Order results by property values
- `$select`: Select specific properties to return
- `$expand`: Expand related entities

---

## Summary by Ingestion Type

| Ingestion Type | Count | Entities |
|----------------|-------|----------|
| cdc | 26 | Most entities with lastModifiedDateTime |
| snapshot | 1 | ComplianceFormDataFieldValue (no modification tracking) |

---

## Key Relationships

### Onboarding 1.0 (OnboardingONB)
- `OnboardingProcess` -> `OnboardingNewHireActivitiesStep` -> Activities (Meeting, Equipment, Goal)
- `OnboardingCandidateInfo` is linked to `OnboardingProcess`
- Equipment types and values are reference data

### Onboarding 2.0 (OnboardingOBX)
- `ONB2Process` -> `ONB2ProcessTask` (tasks within process)
- `ONB2Process` -> `ONB2EquipmentActivity` (equipment activities)
- `ONB2ProcessTrigger` initiates `ONB2Process`
- `ComplianceProcess` -> `ComplianceProcessTask`, `AssignedComplianceForm`, `ComplianceFormData`, `ComplianceDocumentFlow`
- `ComplianceFormData` -> `ComplianceFormSignature`
