# SAP SuccessFactors API Documentation - Succession & Development

## Segment Overview
- **Segment**: 8 - Succession & Development
- **Files Processed**: 5
- **Entities Documented**: 25
- **Endpoints Documented**: 40

## Source Files Summary

| File | API Type | Description |
|------|----------|-------------|
| SuccessionandDevelopmentSD.json | OData v2 | Career development and learning data |
| SDSuccessionManagement.json | OData v2 | Talent pool, successor, and nomination management |
| SDCalibration.json | OData v2 | Calibration session data including ratings and rankings |
| CalSession.json | OData v4 | Calibration session service (enhanced) |
| SCMNominationService.json | OData v4 | Nomination management service (write operations) |

---

## OData v2 Objects

### DevLearningCertifications
**Source File**: SuccessionandDevelopmentSD.json
**API Type**: OData v2
**Base Path**: /odata/v2/DevLearningCertifications

#### Description
Employee learning certifications linked to development activities.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| certificateId | int64 | Yes | Certificate unique identifier |
| learningId | int64 | Yes | Associated learning activity ID |
| certificateName | string | No | Name of the certificate |
| certificateCreatedBy | string | No | User who created the certificate |
| certificateCreatedDate | DateTimeOffset | No | Date certificate was created |
| certificateIssueDate | DateTimeOffset | No | Date certificate was issued |
| certificateExpiredDate | DateTimeOffset | No | Certificate expiration date |
| certificateLastModifiedBy | string | No | Last modifier of certificate record |
| certificateLastModifiedDate | DateTimeOffset | No | Last modification timestamp |

#### Primary Keys
- `certificateId` (int64)
- `learningId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: certificateLastModifiedDate
- **Rationale**: Has certificateLastModifiedDate for incremental tracking and composite key fields

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /DevLearningCertifications | Get all learning certifications | $skip, $top, $inlinecount=allpages |
| GET | /DevLearningCertifications(certificateId={certificateId},learningId={learningId}) | Get single certification by key | N/A |

---

### DevLearning_4201
**Source File**: SuccessionandDevelopmentSD.json
**API Type**: OData v2
**Base Path**: /odata/v2/DevLearning_4201

#### Description
Employee development learning activities.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| learningId | int64 | Yes | Learning activity unique identifier |
| userId | string | No | User associated with the learning |
| assignee | string | No | Assigned person for the learning |
| name | string | No | Name of the learning activity |
| description | string | No | Description of the learning |
| guid | string | No | Global unique identifier |
| sourceType | string | No | Source type of learning |
| status | string | No | Current status of learning |
| startDate | DateTimeOffset | No | Start date of learning activity |
| completedDate | DateTimeOffset | No | Completion date |
| learningCertNavigation | Collection(DevLearningCertifications) | No | Navigation to certificates |

#### Primary Keys
- `learningId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field available; requires full refresh

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /DevLearning_4201 | Get all learning activities | $skip, $top, $inlinecount=allpages |
| GET | /DevLearning_4201({learningId}) | Get single learning by key | N/A |

---

### NomineeHistory
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/NomineeHistory

#### Description
Historical record of changes to nominee information in succession planning.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | History record unique identifier |
| nomineeId | int64 | Yes | Associated nominee ID |
| changeType | int32 | Yes | Type of change made |
| changeTypeLabel | string | No | Label for change type |
| modifiedBy | string | Yes | User who made the modification |
| modifiedDateTime | DateTimeOffset | Yes | Timestamp of modification |
| note | string | No | Note about the change (max 4000 chars) |
| rank | int32 | No | Nominee rank |
| readiness | double | No | Readiness score |
| readinessLabel | string | No | Label for readiness level |
| status | int32 | Yes | Current status |
| statusLabel | string | No | Label for status |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: append
- **Cursor Field**: modifiedDateTime
- **Rationale**: History/audit table with modification timestamps; records are typically inserted, not updated

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /NomineeHistory | Get all nominee history records | $skip, $top, $inlinecount=allpages |
| GET | /NomineeHistory({id}) | Get single history record by key | N/A |

---

### TalentGraphicOption
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/TalentGraphicOption

#### Description
Configuration options for talent graphics and visualizations.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| dataIndex | string | Yes | Data index key |
| optionKey | string | Yes | Option key |
| dataImage | string | Yes | Image data |
| dataLabel | string | Yes | Display label for data |
| dataShortLabel | string | Yes | Short label |
| dataValue | string | Yes | Data value |
| gradientBackgroundColor | string | Yes | Background color gradient |
| optionIndex | int32 | Yes | Option display order |
| optionLabel | string | Yes | Option label |
| optionName | string | Yes | Option name |
| optionScaleId | string | Yes | Associated scale identifier |
| optionTarget | string | Yes | Target for the option |
| optionType | string | Yes | Type of option |

#### Primary Keys
- `dataIndex` (string)
- `optionKey` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Configuration/reference data without modification tracking; full refresh recommended

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /TalentGraphicOption | Get all talent graphic options | $skip, $top, $inlinecount=allpages |
| GET | /TalentGraphicOption(dataIndex='{dataIndex}',optionKey='{optionKey}') | Get single option by key | N/A |

---

### TalentPool
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/TalentPool

#### Description
Talent pools for succession planning and talent management.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | string | Yes | Talent pool code (max 128 chars) |
| effectiveStartDate | DateTimeOffset | Yes | Effective start date |
| effectiveEndDate | DateTimeOffset | No | Effective end date |
| effectiveStatus | string | No | Effective status |
| createdBy | string | No | Creator user ID |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier user ID |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| name_defaultValue | string | No | Default name value |
| name_localized | string | No | Localized name |
| name_en_US | string | No | English (US) name |
| name_de_DE | string | No | German name |
| name_fr_FR | string | No | French name |
| name_ja_JP | string | No | Japanese name |
| name_zh_CN | string | No | Chinese (Simplified) name |
| description_defaultValue | string | No | Default description |
| description_localized | string | No | Localized description |
| owner | string | No | Pool owner (max 100 chars) |
| type | string | No | Pool type |
| enableReadiness | boolean | No | Whether readiness is enabled |
| mdfSystemCreatedBy | string | No | MDF system creator |
| mdfSystemCreatedDate | DateTimeOffset | No | MDF creation date |
| mdfSystemLastModifiedBy | string | No | MDF last modifier |
| mdfSystemLastModifiedDate | DateTimeOffset | No | MDF last modification date |
| mdfSystemLastModifiedDateWithTZ | DateTimeOffset | No | MDF last modification with timezone |
| mdfSystemEntityId | string | No | MDF entity ID |
| mdfSystemObjectType | string | No | MDF object type |
| mdfSystemRecordId | string | No | MDF record ID |
| mdfSystemRecordStatus | string | No | MDF record status |
| mdfSystemVersionId | int64 | No | MDF version ID |
| transactionSequence | int64 | No | Transaction sequence |
| successorNav | Collection(Successor) | No | Navigation to successors |

#### Primary Keys
- `code` (string)
- `effectiveStartDate` (DateTimeOffset)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental change tracking; effective-dated entity

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /TalentPool | Get all talent pools | $skip, $top, $inlinecount=allpages |
| GET | /TalentPool(code='{code}',effectiveStartDate={effectiveStartDate}) | Get single talent pool by key | N/A |

---

### Successor
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/Successor

#### Description
Successor nominations for positions or talent pools.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Successor record unique identifier |
| nomineeUserId | string | No | User ID of the nominee (max 100 chars) |
| lastModifiedBy | string | No | Last modifier user ID |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| note | string | No | Notes about the successor (max 4000 chars) |
| rank | int32 | No | Rank/priority of successor |
| readiness | double | No | Readiness score |
| readinessLabel | string | No | Label for readiness level |
| status | int32 | No | Current status |
| statusLabel | string | No | Label for status |
| nomineeHistoryNav | Collection(NomineeHistory) | No | Navigation to nominee history |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental updates

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Successor | Get all successor records | $skip, $top, $inlinecount=allpages |
| GET | /Successor({id}) | Get single successor by key | N/A |

---

### NominationTarget
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/NominationTarget

#### Description
Targets for nominations (positions or talent pools).

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| nominationId | int64 | Yes | Nomination target unique identifier |
| nominationType | int32 | Yes | Type of nomination target |
| successorNav | Collection(Successor) | No | Navigation to successors |
| talentPoolNav | TalentPool | No | Navigation to talent pool |

#### Primary Keys
- `nominationId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field; requires full refresh

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /NominationTarget | Get all nomination targets | $skip, $top, $inlinecount=allpages |
| GET | /NominationTarget({nominationId}) | Get single nomination target by key | N/A |

---

### LegacyPositionEntity
**Source File**: SDSuccessionManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/LegacyPositionEntity

#### Description
Legacy position data for succession planning.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| positionId | int64 | Yes | Position unique identifier |
| positionCode | string | No | Position code (max 4000 chars) |
| title | string | No | Position title (max 256 chars) |
| incumbent | string | No | Current incumbent (max 100 chars) |
| createDate | DateTimeOffset | No | Position creation date |
| parentNav | LegacyPositionEntity | No | Navigation to parent position |
| successorNav | Collection(Successor) | No | Navigation to successors |

#### Primary Keys
- `positionId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Legacy entity without lastModifiedDateTime; full refresh recommended

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /LegacyPositionEntity | Get all legacy positions | $skip, $top, $inlinecount=allpages |
| GET | /LegacyPositionEntity({positionId}) | Get single position by key | N/A |

---

### TalentRatings
**Source File**: SDCalibration.json
**API Type**: OData v2
**Base Path**: /odata/v2/TalentRatings

#### Description
Talent ratings and feedback data from performance and calibration processes.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| feedbackId | int64 | Yes | Feedback record unique identifier |
| employeeId | string | No | Employee user ID |
| feedbackName | string | No | Name of the feedback |
| feedbackModule | int32 | No | Feedback module type |
| feedbackType | int32 | No | Type of feedback |
| feedbackSource | int32 | No | Source of feedback |
| feedbackRating | double | No | Rating value |
| feedbackRatingLabel | string | No | Rating label |
| feedbackWeight | double | No | Weight of feedback |
| feedbackScaleId | int64 | Yes | Scale identifier |
| feedbackScaleMinimum | double | No | Minimum scale value |
| feedbackScaleMaximum | double | No | Maximum scale value |
| formContentId | int64 | No | Form content ID |
| formDataId | int64 | No | Form data ID |
| calSession | CalibrationSession | No | Navigation to calibration session |

#### Primary Keys
- `feedbackId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification timestamp; requires full refresh

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /TalentRatings | Get all talent ratings | $skip, $top, $inlinecount=allpages |
| GET | /TalentRatings({feedbackId}) | Get single talent rating by key | N/A |

---

### CalibrationSession (v2)
**Source File**: SDCalibration.json
**API Type**: OData v2
**Base Path**: /odata/v2/CalibrationSession

#### Description
Calibration sessions for talent and performance calibration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| sessionId | int64 | Yes | Session unique identifier |
| sessionName | string | Yes | Name of the calibration session |
| sessionDate | DateTimeOffset | No | Date of the session |
| sessionLocation | string | No | Location of the session |
| activationDate | DateTimeOffset | No | Session activation date |
| status | int32 | Yes | Session status |
| lastModifiedBy | string | Yes | Last modifier user ID |
| lastModifiedDateTime | DateTimeOffset | Yes | Last modification timestamp |
| calTemplate | CalibrationTemplate | No | Navigation to calibration template |
| subjectList | Collection(CalibrationSessionSubject) | No | Navigation to session subjects |

#### Primary Keys
- `sessionId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CalibrationSession | Get all calibration sessions | $skip, $top, $inlinecount=allpages |
| GET | /CalibrationSession({sessionId}) | Get single session by key | N/A |

---

### CalibrationSessionSubject
**Source File**: SDCalibration.json
**API Type**: OData v2
**Base Path**: /odata/v2/CalibrationSessionSubject

#### Description
Subjects (employees) included in calibration sessions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| sessionSubjectId | int64 | Yes | Subject record unique identifier |
| calSessionId | int64 | Yes | Associated calibration session ID |
| userId | string | Yes | Subject's user ID |
| status | int32 | Yes | Subject status |
| calibratedFlag | boolean | No | Whether subject has been calibrated |
| comments | string | No | Internal comments |
| externalComments | string | No | External comments |
| reason | string | Yes | Reason for inclusion |
| reasonId | int64 | No | Reason identifier |
| authorizedBy | string | No | Authorization user |
| pmFolderMapId | int64 | No | Performance folder map ID |
| pmFormDataId | int64 | No | Performance form data ID |
| pmFormOwnerId | string | No | Performance form owner |
| createdBy | string | Yes | Creator user ID |
| createdDateTime | DateTimeOffset | Yes | Creation timestamp |
| lastModifiedBy | string | Yes | Last modifier user ID |
| lastModifiedDateTime | DateTimeOffset | Yes | Last modification timestamp |
| calSession | CalibrationSession | No | Navigation to calibration session |
| pmRatingList | Collection(TalentRatings) | No | Navigation to ratings |
| rankList | Collection(CalibrationSubjectRank) | No | Navigation to rankings |

#### Primary Keys
- `sessionSubjectId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental updates

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CalibrationSessionSubject | Get all session subjects | $skip, $top, $inlinecount=allpages |
| GET | /CalibrationSessionSubject({sessionSubjectId}) | Get single subject by key | N/A |

---

### CalibrationTemplate
**Source File**: SDCalibration.json
**API Type**: OData v2
**Base Path**: /odata/v2/CalibrationTemplate

#### Description
Templates for calibration sessions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| templateId | int64 | Yes | Template unique identifier |
| templateName | string | Yes | Template name |
| startDate | DateTimeOffset | Yes | Template validity start |
| endDate | DateTimeOffset | Yes | Template validity end |
| status | int32 | Yes | Template status |
| createdBy | string | Yes | Creator user ID |
| createdDateTime | DateTimeOffset | Yes | Creation timestamp |
| lastModifiedBy | string | Yes | Last modifier user ID |
| lastModifiedDateTime | DateTimeOffset | Yes | Last modification timestamp |

#### Primary Keys
- `templateId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CalibrationTemplate | Get all calibration templates | $skip, $top, $inlinecount=allpages |
| GET | /CalibrationTemplate({templateId}) | Get single template by key | N/A |

---

### CalibrationSubjectRank
**Source File**: SDCalibration.json
**API Type**: OData v2
**Base Path**: /odata/v2/CalibrationSubjectRank

#### Description
Ranking data for calibration session subjects.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| subjectRankId | int64 | Yes | Rank record unique identifier |
| dataType | int32 | Yes | Type of ranking data |
| rank | int32 | Yes | Rank position |
| ratingValue | double | Yes | Rating value |
| calSessionSubject | CalibrationSessionSubject | No | Navigation to session subject |

#### Primary Keys
- `subjectRankId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking; requires full refresh

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CalibrationSubjectRank | Get all subject rankings | $skip, $top, $inlinecount=allpages |
| GET | /CalibrationSubjectRank({subjectRankId}) | Get single ranking by key | N/A |

---

## OData v4 Objects

### CalibrationSession (v4)
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: /odatav4/talent/calibration/CalSession.svc/v1/CalibrationSession

#### Description
Enhanced calibration session service with support for sessions, subjects, and ratings.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Session unique identifier |
| sessionName | string | Yes | Name of the calibration session |
| sessionDate | date | No | Date of the session |
| sessionLocation | string | No | Location of the session |
| activationDate | date | No | Session activation date |
| approvalDateTime | datetime | No | Approval timestamp |
| status | int32 | Yes | Session status |
| createdByWorkAssignmentLegacyId | string | Yes | Creator work assignment ID |
| lastModifiedDateTime | datetime | Yes | Last modification timestamp |
| executiveReviewerList | Collection(CalibrationExecutiveReviewer) | No | Executive reviewers |
| reviewerList | Collection(CalibrationSessionReviewer) | No | Session reviewers |
| subjectList | Collection(CalibrationSubject) | No | Session subjects |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CalibrationSession | Get all calibration sessions | $skip, $top, @odata.nextLink |
| GET | /CalibrationSession({id}) | Get single session by key | N/A |
| GET | /CalibrationSession({id})/executiveReviewerList | Get executive reviewers for session | $skip, $top, @odata.nextLink |
| GET | /CalibrationSession({id})/executiveReviewerList({id-1}) | Get single executive reviewer | N/A |
| GET | /CalibrationSession({id})/reviewerList | Get reviewers for session | $skip, $top, @odata.nextLink |
| GET | /CalibrationSession({id})/reviewerList({id-1}) | Get single reviewer | N/A |
| GET | /CalibrationSession({id})/subjectList | Get subjects for session | $skip, $top, @odata.nextLink |
| GET | /CalibrationSession({id})/subjectList({id-1}) | Get single subject | N/A |

---

### CalibrationSubject (v4)
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: /odatav4/talent/calibration/CalSession.svc/v1/CalibrationSession({id})/subjectList

#### Description
Subjects (employees) included in v4 calibration sessions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Subject unique identifier |
| workAssignmentLegacyId | string | Yes | Work assignment legacy ID |
| calibrated | boolean | No | Whether subject has been calibrated |
| pmFormDataId | int64 | No | Performance form data ID |
| pmuDeeplink | string | No | PMU deep link |
| commentList | Collection(CalibrationSubjectComment) | No | Subject comments |
| competencyRatingList | Collection(CalibrationCompetencyRating) | No | Competency ratings |
| ratingList | Collection(CalibrationRating) | No | Ratings |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Nested entity accessed via parent; no direct modification tracking

---

### CalibrationSubjectComment
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: Nested under CalibrationSubject

#### Description
Comments on calibration session subjects.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Comment unique identifier |
| comment | string | No | Comment text |
| createdByWorkAssignmentLegacyId | string | Yes | Creator work assignment ID |
| createdDateTime | datetime | Yes | Creation timestamp |
| lastModifiedDateTime | datetime | No | Last modification timestamp |
| modified | boolean | Yes | Whether comment was modified |
| reasonId | int64 | No | Reason identifier |
| reasonLabel | string | No | Reason label |
| authorizedByWorkAssignmentLegacyId | string | No | Authorizer work assignment ID |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for tracking changes

---

### CalibrationCompetencyRating
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: Nested under CalibrationSubject

#### Description
Competency ratings for calibration subjects.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| competencyId | int64 | Yes | Competency unique identifier |
| competencyName | string | No | Competency name |
| competencySectionId | int64 | No | Section identifier |
| competencySectionName | string | No | Section name |
| rating | decimal | No | Rating value |
| ratingLabel | string | No | Rating label |
| ratingOptions | Collection(CalibrationRatingOption) | No | Available rating options |

#### Primary Keys
- `competencyId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Nested entity without modification tracking

---

### CalibrationRating
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: Nested under CalibrationSubject

#### Description
General ratings for calibration subjects.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ratingType | int32 | Yes | Rating type identifier |
| rating | decimal | No | Rating value |
| ratingLabel | string | No | Rating label |
| ratingTypeLabel | string | No | Rating type label |

#### Primary Keys
- `ratingType` (int32)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Nested entity without modification tracking

---

### CalibrationRatingOption
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: Nested under CalibrationCompetencyRating

#### Description
Available rating options for competency ratings.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| value | double | Yes | Rating option value |
| label | string | No | Rating option label |

#### Primary Keys
- `value` (double)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

---

### CalibrationExecutiveReviewer
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: /odatav4/talent/calibration/CalSession.svc/v1/CalibrationSession({id})/executiveReviewerList

#### Description
Executive reviewers assigned to calibration sessions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Reviewer unique identifier |
| workAssignmentLegacyId | string | Yes | Work assignment legacy ID |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Nested entity without modification tracking

---

### CalibrationSessionReviewer
**Source File**: CalSession.json
**API Type**: OData v4
**Base Path**: /odatav4/talent/calibration/CalSession.svc/v1/CalibrationSession({id})/reviewerList

#### Description
Reviewers (facilitators, participants, owners) assigned to calibration sessions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Reviewer unique identifier |
| reviewerType | string | Yes | Type of reviewer (facilitator, participant, owner) |
| workAssignmentLegacyId | string | Yes | Work assignment legacy ID |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Nested entity without modification tracking

---

### NominationActionResponse
**Source File**: SCMNominationService.json
**API Type**: OData v4
**Base Path**: /odatav4/talent/succession/NominationService.svc/v1

#### Description
Response object for nomination actions (create, update, delete).

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| action | string | No | Action performed |
| value | boolean | No | Success indicator |

#### Primary Keys
- N/A (response object)

#### Ingestion Type
- **Type**: N/A
- **Cursor Field**: N/A
- **Rationale**: Response object, not a data entity for ingestion

---

## Service Operations (OData v4)

### CalSession.svc Service Operations

| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| approveSession | POST | /CalibrationSession({id})/CalSession.svc.approveSession | Finalize a calibration session |
| refreshMetadata | POST | /refreshMetadata | Refresh metadata for the Calibration Session Service |
| $batch | POST | /$batch | Send batch requests |

### NominationService.svc Service Operations

| Operation | Method | Path | Description |
|-----------|--------|------|-------------|
| upsertNomination | POST | /upsertNomination | Create or update a nomination for position or talent pool |
| deleteNomination | POST | /deleteNomination | Delete a nomination for position or talent pool |
| refreshMetadata | POST | /refreshMetadata | Refresh metadata for the Nomination Service |
| $batch | POST | /$batch | Send batch requests |

**Note**: The NominationService.svc is primarily a write-oriented service for managing nominations. It does not expose GET endpoints for reading nomination data. For reading nomination data, use the SDSuccessionManagement OData v2 APIs (NominationTarget, Successor, TalentPool).

---

## Ingestion Summary by Entity

| Entity | API Version | Ingestion Type | Cursor Field | Notes |
|--------|-------------|----------------|--------------|-------|
| DevLearningCertifications | v2 | cdc | certificateLastModifiedDate | Composite key |
| DevLearning_4201 | v2 | snapshot | N/A | No modification tracking |
| NomineeHistory | v2 | append | modifiedDateTime | Audit/history table |
| TalentGraphicOption | v2 | snapshot | N/A | Configuration data |
| TalentPool | v2 | cdc | lastModifiedDateTime | Effective-dated |
| Successor | v2 | cdc | lastModifiedDateTime | - |
| NominationTarget | v2 | snapshot | N/A | No modification tracking |
| LegacyPositionEntity | v2 | snapshot | N/A | Legacy entity |
| TalentRatings | v2 | snapshot | N/A | No modification tracking |
| CalibrationSession (v2) | v2 | cdc | lastModifiedDateTime | - |
| CalibrationSessionSubject | v2 | cdc | lastModifiedDateTime | - |
| CalibrationTemplate | v2 | cdc | lastModifiedDateTime | - |
| CalibrationSubjectRank | v2 | snapshot | N/A | No modification tracking |
| CalibrationSession (v4) | v4 | cdc | lastModifiedDateTime | Enhanced API |
| CalibrationSubject (v4) | v4 | snapshot | N/A | Nested entity |
| CalibrationSubjectComment | v4 | cdc | lastModifiedDateTime | Nested entity |
| CalibrationCompetencyRating | v4 | snapshot | N/A | Nested entity |
| CalibrationRating | v4 | snapshot | N/A | Nested entity |
| CalibrationRatingOption | v4 | snapshot | N/A | Reference data |
| CalibrationExecutiveReviewer | v4 | snapshot | N/A | Nested entity |
| CalibrationSessionReviewer | v4 | snapshot | N/A | Nested entity |

---

## Relationships and Navigation Properties

### Succession Management Relationships
```
TalentPool
  └── successorNav → Successor[]
        └── nomineeHistoryNav → NomineeHistory[]

NominationTarget
  ├── successorNav → Successor[]
  └── talentPoolNav → TalentPool

LegacyPositionEntity
  ├── parentNav → LegacyPositionEntity
  └── successorNav → Successor[]
```

### Calibration Relationships (v2)
```
CalibrationSession
  ├── calTemplate → CalibrationTemplate
  └── subjectList → CalibrationSessionSubject[]
        ├── calSession → CalibrationSession
        ├── pmRatingList → TalentRatings[]
        └── rankList → CalibrationSubjectRank[]

TalentRatings
  └── calSession → CalibrationSession
```

### Calibration Relationships (v4)
```
CalibrationSession
  ├── executiveReviewerList → CalibrationExecutiveReviewer[]
  ├── reviewerList → CalibrationSessionReviewer[]
  └── subjectList → CalibrationSubject[]
        ├── commentList → CalibrationSubjectComment[]
        ├── competencyRatingList → CalibrationCompetencyRating[]
        │     └── ratingOptions → CalibrationRatingOption[]
        └── ratingList → CalibrationRating[]
```

### Development Learning Relationships
```
DevLearning_4201
  └── learningCertNavigation → DevLearningCertifications[]
```

---

## API Version Comparison

### CalibrationSession v2 vs v4

| Feature | OData v2 | OData v4 |
|---------|----------|----------|
| Base Path | /odata/v2/CalibrationSession | /odatav4/talent/calibration/CalSession.svc/v1/CalibrationSession |
| Pagination | $skip, $top, $inlinecount | $skip, $top, @odata.nextLink |
| Nested Access | Via $expand | Direct path access + $expand |
| Write Operations | Limited | approveSession action available |
| Competency Ratings | Via pmRatingList | Dedicated competencyRatingList |
| Executive Reviewers | Not available | executiveReviewerList |

### Recommended Usage
- **v2 APIs**: Use for bulk data extraction and comprehensive reporting
- **v4 CalSession**: Use for enhanced calibration session management with granular access to nested entities
- **v4 NominationService**: Use for write operations (create, update, delete nominations)
