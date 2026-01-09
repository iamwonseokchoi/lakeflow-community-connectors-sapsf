# SAP SuccessFactors API Documentation - Recruitment Management

## Segment Overview
- **Segment**: 5 - Recruitment Management
- **Files Processed**: 5
- **Entities Documented**: 53
- **Endpoints Documented**: 112

## Files Processed
| File | API Title | Description |
|------|-----------|-------------|
| RCMCandidate.json | Candidate Profile | Manage candidate profiles, background information, and qualifications |
| RCMJobApplication.json | Job Application | Query and manage job applications and assess applicants |
| RCMJobRequisition.json | Job Requisition | Create and manage job requisitions and job postings |
| RCMOffer.json | Job Offer | Approve or decline job applications, manage offer letters |
| RecruitingRCM.json | Job Application Interview | View and edit job interview information and assessments |

---

## Objects from RCMCandidate.json

### CandidateBackground_InsideWorkExperience
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_InsideWorkExperience

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| department | string | No | Department name |
| endDate | DateTimeOffset | No | End date of work experience |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date of work experience |
| title | string | No | Job title |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime field for tracking changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_InsideWorkExperience | List all records | $skip, $top |
| GET | /CandidateBackground_InsideWorkExperience({backgroundElementId}) | Get by ID | N/A |

---

### CandidateLight
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateLight

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| candidateId | int64 | Yes | Primary key identifier |
| address | string | No | Address |
| address2 | string | No | Secondary address |
| cellPhone | string | No | Cell phone number |
| city | string | No | City |
| contactEmail | string | No | Contact email |
| country | string | No | Country |
| currentCompany | string | No | Current company |
| currentTitle | string | No | Current job title |
| dataSource | string | No | Data source |
| dateOfAvailability | DateTimeOffset | No | Availability date |
| externalCandidate | boolean | No | External candidate flag |
| firstName | string | No | First name |
| homePhone | string | No | Home phone |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| lastName | string | No | Last name |
| middleName | string | No | Middle name |
| partnerMemberId | string | No | Partner member ID |
| partnerSource | int64 | No | Partner source |
| primaryEmail | string | No | Primary email |
| state | string | No | State |
| zip | string | No | ZIP code |

#### Primary Keys
- `candidateId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateLight | List all candidates | $skip, $top |
| GET | /CandidateLight({candidateId}) | Get by ID | N/A |

---

### CandidateComments
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateComments

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| commentId | int64 | Yes | Primary key identifier |
| associatedCommentId | int64 | No | Associated comment reference |
| associatedId | string | No | Associated entity ID |
| candidateId | int64 | No | Reference to candidate |
| commentator | string | No | Person who made the comment |
| content | string | No | Comment content |
| refType | string | No | Reference type |

#### Primary Keys
- `commentId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateComments | List all comments | $skip, $top |
| GET | /CandidateComments({commentId}) | Get by ID | N/A |

---

### CandidateBackground_Education
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_Education

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| degree | string | No | Degree obtained |
| endDate | DateTimeOffset | No | End date |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| major | string | No | Major field of study |
| school | string | No | School name |
| startDate | DateTimeOffset | No | Start date |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_Education | List all records | $skip, $top |
| GET | /CandidateBackground_Education({backgroundElementId}) | Get by ID | N/A |

---

### Candidate
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/Candidate

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| candidateId | int64 | Yes | Primary key identifier |
| address | string | No | Address |
| address2 | string | No | Secondary address |
| agreeToPrivacyStatement | string | No | Privacy agreement status |
| anonymized | string | No | Anonymization status |
| anonymizedDateTime | DateTimeOffset | No | Anonymization timestamp |
| candidateLocale | string | No | Candidate locale |
| cellPhone | string | No | Cell phone |
| city | string | No | City |
| consentToMarketing | string | No | Marketing consent |
| contactEmail | string | No | Contact email |
| country | string | No | Country |
| creationDateTime | DateTimeOffset | No | Creation timestamp |
| currentCompany | string | No | Current company |
| currentTitle | string | No | Current title |
| dataSource | string | No | Data source |
| dateOfAvailability | DateTimeOffset | No | Availability date |
| externalCandidate | boolean | No | External candidate flag |
| firstName | string | No | First name |
| homePhone | string | No | Home phone |
| lastLoginDateTime | DateTimeOffset | No | Last login timestamp |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| lastName | string | No | Last name |
| middleName | string | No | Middle name |
| partnerMemberId | string | No | Partner member ID |
| partnerSource | int64 | No | Partner source |
| password | string | No | Password (encrypted) |
| primaryEmail | string | No | Primary email |
| privacyAcceptDateTime | DateTimeOffset | No | Privacy acceptance timestamp |
| publicIntranet | boolean | No | Public intranet flag |
| shareProfile | string | No | Share profile status |
| state | string | No | State |
| usersSysId | string | No | User system ID |
| visibilityOption | boolean | No | Visibility option |
| zip | string | No | ZIP code |

#### Primary Keys
- `candidateId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Candidate | List all candidates | $skip, $top |
| GET | /Candidate({candidateId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_TalentPoolcorp
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_TalentPoolcorp

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date |
| talentPoolComments | string | No | Talent pool comments |
| talentPoolStatus | string | No | Talent pool status |
| talentPoolitem | string | No | Talent pool item |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_TalentPoolcorp | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_TalentPoolcorp({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_Education
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_Education

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| degree | string | No | Degree obtained |
| endDate | DateTimeOffset | No | End date |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| major | string | No | Major field of study |
| school | string | No | School name |
| startDate | DateTimeOffset | No | Start date |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_Education | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_Education({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_TalentPool
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_TalentPool

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date |
| talentPoolComments | string | No | Talent pool comments |
| talentPoolStatus | string | No | Talent pool status |
| talentPoolitem | string | No | Talent pool item |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_TalentPool | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_TalentPool({backgroundElementId}) | Get by ID | N/A |

---

### CandidateBackground_OutsideWorkExperience
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_OutsideWorkExperience

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| employer | string | No | Employer name |
| endDate | DateTimeOffset | No | End date |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| presentEmployer | string | No | Present employer flag |
| startDate | DateTimeOffset | No | Start date |
| startTitle | string | No | Starting title |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_OutsideWorkExperience | List all records | $skip, $top |
| GET | /CandidateBackground_OutsideWorkExperience({backgroundElementId}) | Get by ID | N/A |

---

### CandidateBackground_Certificates
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_Certificates

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| description | string | No | Certificate description |
| endDate | DateTimeOffset | No | End date |
| institution | string | No | Issuing institution |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| name | string | No | Certificate name |
| startDate | DateTimeOffset | No | Start date |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_Certificates | List all records | $skip, $top |
| GET | /CandidateBackground_Certificates({backgroundElementId}) | Get by ID | N/A |

---

### CandidateBackground_Languages
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_Languages

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| language | string | No | Language name |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| readingProf | string | No | Reading proficiency |
| speakingProf | string | No | Speaking proficiency |
| writingProf | string | No | Writing proficiency |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_Languages | List all records | $skip, $top |
| GET | /CandidateBackground_Languages({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_InsideWorkExperience
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_InsideWorkExperience

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| department | string | No | Department |
| endDate | DateTimeOffset | No | End date |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date |
| title | string | No | Job title |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_InsideWorkExperience | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_InsideWorkExperience({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_Certificates
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_Certificates

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| description | string | No | Certificate description |
| endDate | DateTimeOffset | No | End date |
| institution | string | No | Issuing institution |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| name | string | No | Certificate name |
| startDate | DateTimeOffset | No | Start date |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_Certificates | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_Certificates({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_OutsideWorkExperience
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_OutsideWorkExperience

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| employer | string | No | Employer name |
| endDate | DateTimeOffset | No | End date |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| presentEmployer | string | No | Present employer flag |
| startDate | DateTimeOffset | No | Start date |
| startTitle | string | No | Starting title |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_OutsideWorkExperience | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_OutsideWorkExperience({backgroundElementId}) | Get by ID | N/A |

---

### JobApplicationSnapshot_Languages
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationSnapshot_Languages

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Application reference |
| bgOrderPos | int64 | No | Background order position |
| language | string | No | Language name |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| readingProf | string | No | Reading proficiency |
| speakingProf | string | No | Speaking proficiency |
| writingProf | string | No | Writing proficiency |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationSnapshot_Languages | List all records | $skip, $top |
| GET | /JobApplicationSnapshot_Languages({backgroundElementId}) | Get by ID | N/A |

---

### CandidateBackground_TalentPool
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_TalentPool

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date |
| talentPoolComments | string | No | Talent pool comments |
| talentPoolStatus | string | No | Talent pool status |
| talentPoolitem | string | No | Talent pool item |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_TalentPool | List all records | $skip, $top |
| GET | /CandidateBackground_TalentPool({backgroundElementId}) | Get by ID | N/A |

---

### CandidateProfileExtension
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateProfileExtension

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| candidateId | int64 | Yes | Primary key identifier |
| createdBy | string | No | Created by user |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |

#### Primary Keys
- `candidateId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateProfileExtension | List all records | $skip, $top |
| GET | /CandidateProfileExtension({candidateId}) | Get by ID | N/A |

---

### CandidateTags
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateTags

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| tagId | int64 | Yes | Primary key identifier |
| candidateId | int64 | No | Reference to candidate |
| label | string | No | Tag label |
| locale | string | No | Tag locale |

#### Primary Keys
- `tagId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateTags | List all tags | $skip, $top |
| GET | /CandidateTags({tagId}) | Get by ID | N/A |

---

### CandidateBackground_TalentPoolcorp
**Source File**: RCMCandidate.json
**API Type**: OData v2
**Base Path**: /odata/v2/CandidateBackground_TalentPoolcorp

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| backgroundElementId | int64 | Yes | Primary key identifier |
| bgOrderPos | int64 | No | Background order position |
| candidateId | int64 | No | Reference to candidate |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| startDate | DateTimeOffset | No | Start date |
| talentPoolComments | string | No | Talent pool comments |
| talentPoolStatus | string | No | Talent pool status |
| talentPoolitem | string | No | Talent pool item |

#### Primary Keys
- `backgroundElementId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CandidateBackground_TalentPoolcorp | List all records | $skip, $top |
| GET | /CandidateBackground_TalentPoolcorp({backgroundElementId}) | Get by ID | N/A |

---

## Objects from RCMJobApplication.json

### JobApplicationAssessmentReport
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationAssessmentReport

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Primary key identifier |
| orderId | int64 | No | Reference to assessment order |
| reportURL | string | No | URL to assessment report |
| status | int64 | No | Assessment status |
| statusDate | DateTimeOffset | No | Status date |
| statusDetails | string | No | Status details |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationAssessmentReport | List all reports | $skip, $top |
| GET | /JobApplicationAssessmentReport({id}) | Get by ID | N/A |

---

### JobApplicationOnboardingData
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationOnboardingData

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| onboardingId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| status | string | No | Onboarding status |
| submittedBy | string | No | Submitted by user |
| submittedOn | DateTimeOffset | No | Submission timestamp |

#### Primary Keys
- `onboardingId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationOnboardingData | List all records | $skip, $top |
| GET | /JobApplicationOnboardingData({onboardingId}) | Get by ID | N/A |

---

### JobApplicationStatusLabel
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationStatusLabel

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| appStatusId | int64 | Yes | Primary key identifier |
| candidateLabel | string | No | Label shown to candidate |
| locale | string | No | Locale code |
| statusLabel | string | No | Status label text |

#### Primary Keys
- `appStatusId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationStatusLabel | List all labels | $skip, $top |
| GET | /JobApplicationStatusLabel({appStatusId}) | Get by ID | N/A |

---

### JobApplicationOnboardingStatus
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationOnboardingStatus

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| onboardingStatusId | int64 | Yes | Primary key identifier |
| createdDate | DateTimeOffset | No | Creation timestamp |
| lastModifiedDate | DateTimeOffset | No | Last modification timestamp |
| message | string | No | Status message |
| name | string | No | Status name |
| onboardingId | int64 | No | Reference to onboarding |
| status | string | No | Status value |
| statusType | string | No | Status type |
| type | string | No | Type |
| url | string | No | Related URL |

#### Primary Keys
- `onboardingStatusId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationOnboardingStatus | List all statuses | $skip, $top |
| GET | /JobApplicationOnboardingStatus({onboardingStatusId}) | Get by ID | N/A |

---

### JobApplicationQuestionResponse
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationQuestionResponse

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| applicationId | int64 | Yes | Application ID (composite key) |
| order | int64 | Yes | Question order (composite key) |
| answer | string | No | Answer provided |
| expectedAnswer | string | No | Expected answer |
| expectedAnswerValue | double | No | Expected answer value |
| highLow | string | No | High/low indicator |
| maxLength | double | No | Maximum answer length |
| question | string | No | Question text |
| questionResponse | string | No | Question response |
| type | string | No | Question type |

#### Primary Keys
- `applicationId` (int64)
- `order` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationQuestionResponse | List all responses | $skip, $top |
| GET | /JobApplicationQuestionResponse(applicationId={applicationId},order={order}) | Get by composite key | N/A |

---

### JobApplicationStatusAuditTrail
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationStatusAuditTrail

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| revNumber | int64 | Yes | Revision number (primary key) |
| createdBy | string | No | Created by user |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| lastModifiedProxyUser | string | No | Proxy user |
| revType | int32 | No | Revision type |
| skippedStatus | int32 | No | Skipped status flag |
| statusComments | string | No | Status comments |

#### Primary Keys
- `revNumber` (int64)

#### Ingestion Type
- **Type**: append
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Audit trail table with revision numbers - new records are appended

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationStatusAuditTrail | List all audit records | $skip, $top |
| GET | /JobApplicationStatusAuditTrail({revNumber}) | Get by revision number | N/A |

---

### JobApplicationAssessmentOrder
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationAssessmentOrder

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| createdBy | string | No | Created by user |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| vendorCode | string | No | Assessment vendor code |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationAssessmentOrder | List all orders | $skip, $top |
| GET | /JobApplicationAssessmentOrder({id}) | Get by ID | N/A |

---

### JobApplicationAssessmentReportDetail
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationAssessmentReportDetail

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | int64 | Yes | Primary key identifier |
| scoreComponent | string | No | Score component name |
| scoreValue | string | No | Score value |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationAssessmentReportDetail | List all details | $skip, $top |
| GET | /JobApplicationAssessmentReportDetail({id}) | Get by ID | N/A |

---

### JobApplicationBackgroundCheckResult
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationBackgroundCheckResult

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| statusId | int64 | Yes | Primary key identifier |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| finalStep | boolean | No | Final step flag |
| reportUrl | string | No | Report URL |
| stepMessage | string | No | Step message |
| stepName | string | No | Step name |
| stepStatus | string | No | Step status |
| vendorCode | string | No | Vendor code |
| vendorOrderNo | string | No | Vendor order number |

#### Primary Keys
- `statusId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationBackgroundCheckResult | List all results | $skip, $top |
| GET | /JobApplicationBackgroundCheckResult({statusId}) | Get by ID | N/A |

---

### JobApplicationStatus
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationStatus

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| appStatusSetId | int64 | Yes | Primary key identifier |
| appStatusId | int64 | No | Application status ID |
| appStatusName | string | No | Application status name |

#### Primary Keys
- `appStatusSetId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationStatus | List all statuses | $skip, $top |
| GET | /JobApplicationStatus({appStatusSetId}) | Get by ID | N/A |

---

### JobApplicationBackgroundCheckRequest
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationBackgroundCheckRequest

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| requestId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| createdByUser | string | No | Created by user |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| orderStatus | string | No | Order status |
| responseCode | string | No | Response code |
| responseDetail | string | No | Response detail |
| vendorCode | string | No | Vendor code |
| vendorOrderNo | string | No | Vendor order number |

#### Primary Keys
- `requestId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationBackgroundCheckRequest | List all requests | $skip, $top |
| GET | /JobApplicationBackgroundCheckRequest({requestId}) | Get by ID | N/A |

---

### JobApplicationComments
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationComments

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| commentId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| associatedCommentId | int64 | No | Associated comment reference |
| associatedId | string | No | Associated entity ID |
| commentator | string | No | Person who made the comment |
| content | string | No | Comment content |
| hasAssociatedComment | string | No | Has associated comment flag |
| migratedCommentatorUserName | string | No | Migrated commentator username |
| refType | string | No | Reference type |

#### Primary Keys
- `commentId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationComments | List all comments | $skip, $top |
| GET | /JobApplicationComments({commentId}) | Get by ID | N/A |

---

### JobApplication
**Source File**: RCMJobApplication.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplication

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| applicationId | int64 | Yes | Primary key identifier |
| address | string | No | Address |
| address2 | string | No | Secondary address |
| agencyInfo | string | No | Agency information |
| anonymizedDate | DateTimeOffset | No | Anonymization date |
| anonymizedFlag | string | No | Anonymization flag |
| appLocale | string | No | Application locale |
| appStatusSetItemId | int64 | No | Status set item ID |
| applicationTemplateId | int64 | No | Application template ID |
| averageRating | decimal | No | Average rating |
| baseSalary | decimal | No | Base salary |
| candidateId | int64 | No | Reference to candidate |
| cellPhone | string | No | Cell phone |
| city | string | No | City |
| contactEmail | string | No | Contact email |
| country | string | No | Country |
| countryCode | string | No | Country code |
| currentLocation | string | No | Current location |
| currentTitle | string | No | Current title |
| dataSource | string | No | Data source |
| dateOfBirth | DateTimeOffset | No | Date of birth |
| firstName | string | No | First name |
| formerEmployee | boolean | No | Former employee flag |
| gender | string | No | Gender |
| hireDate | DateTimeOffset | No | Hire date |
| hiredOn | DateTimeOffset | No | Hired on timestamp |
| homePhone | string | No | Home phone |
| jobCode | string | No | Job code |
| jobReqId | int64 | No | Reference to job requisition |
| jobStartDate | DateTimeOffset | No | Job start date |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedByProxy | string | No | Last modified by proxy |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| lastName | string | No | Last name |
| middleName | string | No | Middle name |
| owner | string | No | Owner |
| rating | string | No | Rating |
| referredBy | string | No | Referred by |
| source | string | No | Source |
| sourceLabel | string | No | Source label |
| status | string | No | Status |
| statusComments | string | No | Status comments |
| timeToHire | double | No | Time to hire |
| zip | string | No | ZIP code |

#### Primary Keys
- `applicationId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplication | List all applications | $skip, $top |
| GET | /JobApplication({applicationId}) | Get by ID | N/A |

---

## Objects from RCMJobRequisition.json

### JobRequisitionLocale
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobRequisitionLocale

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqLocalId | int64 | Yes | Primary key identifier |
| extJobDescFooter | string | No | External job description footer |
| extJobDescHeader | string | No | External job description header |
| externalJobDescription | string | No | External job description |
| externalTitle | string | No | External title |
| intJobDescFooter | string | No | Internal job description footer |
| intJobDescHeader | string | No | Internal job description header |
| jobDescription | string | No | Job description |
| jobReqId | int64 | No | Reference to job requisition |
| jobTitle | string | No | Job title |
| locale | string | No | Locale code |
| status | string | No | Status |
| templateHeaderFooter | string | No | Template header/footer |

#### Primary Keys
- `jobReqLocalId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobRequisitionLocale | List all locales | $skip, $top |
| GET | /JobRequisitionLocale({jobReqLocalId}) | Get by ID | N/A |

---

### JobReqQuestion
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobReqQuestion

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| questionId | int64 | Yes | Primary key identifier |
| questionCategory | string | No | Question category |
| questionName | string | No | Question name |
| questionSource | string | No | Question source |
| questionType | string | No | Question type |

#### Primary Keys
- `questionId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobReqQuestion | List all questions | $skip, $top |
| GET | /JobReqQuestion({questionId}) | Get by ID | N/A |

---

### JobRequisitionGroupOperator
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobRequisitionGroupOperator

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqId | int64 | Yes | Job requisition ID (composite key) |
| operatorRole | string | Yes | Operator role (composite key) |
| userGroupId | int64 | Yes | User group ID (composite key) |
| adminSelectedGroupToBeRemoved | boolean | No | Admin selected group to be removed |
| isAdminSelected | boolean | No | Is admin selected |
| isDisabled | boolean | No | Is disabled |
| userGroupName | string | No | User group name |

#### Primary Keys
- `jobReqId` (int64)
- `operatorRole` (string)
- `userGroupId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobRequisitionGroupOperator | List all operators | $skip, $top |
| GET | /JobRequisitionGroupOperator(jobReqId={jobReqId},operatorRole='{operatorRole}',userGroupId={userGroupId}) | Get by composite key | N/A |

---

### JobRequisitionPosting
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobRequisitionPosting

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobPostingId | int64 | Yes | Job posting ID (composite key) |
| jobReqId | int64 | Yes | Job requisition ID (composite key) |
| agencyComments | string | No | Agency comments |
| boardId | string | No | Board ID |
| boardName | string | No | Board name |
| channelId | string | No | Channel ID |
| extPartnerAccountId | int64 | No | External partner account ID |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| postEndDate | DateTimeOffset | No | Post end date |
| postEndDateOffset | DateTimeOffset | No | Post end date offset |
| postStartDate | DateTimeOffset | No | Post start date |
| postStartDateOffset | DateTimeOffset | No | Post start date offset |
| postedBy | string | No | Posted by user |
| postingStatus | string | No | Posting status |

#### Primary Keys
- `jobPostingId` (int64)
- `jobReqId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobRequisitionPosting | List all postings | $skip, $top |
| GET | /JobRequisitionPosting(jobPostingId={jobPostingId},jobReqId={jobReqId}) | Get by composite key | N/A |

---

### JobRequisition
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobRequisition

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqId | int64 | Yes | Primary key identifier |
| age | int64 | No | Age |
| appTemplateId | int64 | No | Application template ID |
| candidateProgress | int64 | No | Candidate progress |
| city | string | No | City |
| classificationTime | string | No | Classification time |
| classificationType | string | No | Classification type |
| closedDateTime | DateTimeOffset | No | Closed date/time |
| comment | string | No | Comment |
| corporatePosting | boolean | No | Corporate posting flag |
| costCenterId | string | No | Cost center ID |
| country | string | No | Country |
| createdDateTime | DateTimeOffset | No | Creation timestamp |
| currency | string | No | Currency |
| defaultLanguage | string | No | Default language |
| deleted | string | No | Deleted flag |
| department | string | No | Department |
| division | string | No | Division |
| formDataId | int64 | No | Form data ID |
| formDueDate | DateTimeOffset | No | Form due date |
| function | string | No | Function |
| industry | string | No | Industry |
| internalStatus | string | No | Internal status |
| intranetPosting | boolean | No | Intranet posting flag |
| isDraft | boolean | No | Is draft flag |
| jobCode | string | No | Job code |
| jobReqGUId | string | No | Job requisition GUID |
| jobRole | string | No | Job role |
| jobStartDate | DateTimeOffset | No | Job start date |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDateTime | DateTimeOffset | No | Last modification timestamp |
| lastModifiedProxyUserId | string | No | Last modified proxy user ID |
| location | string | No | Location |
| numberOpenings | decimal | No | Number of openings |
| openingsFilled | int64 | No | Openings filled |
| positionNumber | string | No | Position number |
| postalcode | string | No | Postal code |
| ratedApplicantCount | int64 | No | Rated applicant count |
| salaryBase | decimal | No | Base salary |
| salaryMax | decimal | No | Maximum salary |
| salaryMin | decimal | No | Minimum salary |
| stateProvince | string | No | State/Province |
| statusSetId | int64 | No | Status set ID |
| templateId | int64 | No | Template ID |
| templateType | string | No | Template type |
| timeToFill | int64 | No | Time to fill |

#### Primary Keys
- `jobReqId` (int64)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Delete Field**: deleted
- **Rationale**: Has lastModifiedDateTime for tracking and 'deleted' field for soft deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobRequisition | List all requisitions | $skip, $top |
| GET | /JobRequisition({jobReqId}) | Get by ID | N/A |

---

### JobReqScreeningQuestionChoice
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobReqScreeningQuestionChoice

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| locale | string | Yes | Locale (composite key) |
| optionId | int64 | Yes | Option ID (composite key) |
| optionValue | double | Yes | Option value (composite key) |
| optionLabel | string | No | Option label |

#### Primary Keys
- `locale` (string)
- `optionId` (int64)
- `optionValue` (double)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobReqScreeningQuestionChoice | List all choices | $skip, $top |
| GET | /JobReqScreeningQuestionChoice(locale='{locale}',optionId={optionId},optionValue={optionValue}) | Get by composite key | N/A |

---

### JobRequisitionOperator
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobRequisitionOperator

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqId | int64 | Yes | Job requisition ID (composite key) |
| operatorRole | string | Yes | Operator role (composite key) |
| usersSysId | string | Yes | User system ID (composite key) |
| adminSelectedUserToBeRemoved | boolean | No | Admin selected user to be removed |
| email | string | No | Email |
| fax | string | No | Fax |
| firstName | string | No | First name |
| isAdminSelected | boolean | No | Is admin selected |
| isOwner | boolean | No | Is owner |
| lastName | string | No | Last name |
| phone | string | No | Phone |
| userName | string | No | User name |

#### Primary Keys
- `jobReqId` (int64)
- `operatorRole` (string)
- `usersSysId` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobRequisitionOperator | List all operators | $skip, $top |
| GET | /JobRequisitionOperator(jobReqId={jobReqId},operatorRole='{operatorRole}',usersSysId='{usersSysId}') | Get by composite key | N/A |

---

### JobReqScreeningQuestion
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobReqScreeningQuestion

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqId | int64 | Yes | Job requisition ID (composite key) |
| locale | string | Yes | Locale (composite key) |
| order | int64 | Yes | Question order (composite key) |
| disqualifier | boolean | No | Disqualifier flag |
| expectedAnswerValue | double | No | Expected answer value |
| expectedDir | string | No | Expected direction |
| jobReqContent | string | No | Job requisition content |
| maxLength | int64 | No | Maximum length |
| questionDescription | string | No | Question description |
| questionId | int64 | No | Question ID |
| questionName | string | No | Question name |
| questionParentId | int64 | No | Parent question ID |
| questionParentResponse | string | No | Parent question response |
| questionType | string | No | Question type |
| questionWeight | double | No | Question weight |
| ratingScale | string | No | Rating scale |
| required | boolean | No | Required flag |
| score | boolean | No | Score flag |

#### Primary Keys
- `jobReqId` (int64)
- `locale` (string)
- `order` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobReqScreeningQuestion | List all questions | $skip, $top |
| GET | /JobReqScreeningQuestion(jobReqId={jobReqId},locale='{locale}',order={order}) | Get by composite key | N/A |

---

### JobReqGOPosition
**Source File**: RCMJobRequisition.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobReqGOPosition

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| jobReqMultiSelectId | int64 | Yes | Primary key identifier |
| externalCode | string | No | External code |
| fieldName | string | No | Field name |
| isPrimary | boolean | No | Is primary flag |
| jobReqId | int64 | No | Reference to job requisition |
| parentFieldValue | int64 | No | Parent field value |

#### Primary Keys
- `jobReqMultiSelectId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobReqGOPosition | List all positions | $skip, $top |
| GET | /JobReqGOPosition({jobReqMultiSelectId}) | Get by ID | N/A |
| GET | /JobRequisition({jobReqId})/std_position_objlist | Get positions for requisition | $skip, $top |
| GET | /JobReqGOPosition({jobReqMultiSelectId})/value | Get position value | N/A |

---

## Objects from RCMOffer.json

### RCMAdminReassignOfferApprover
**Source File**: RCMOffer.json
**API Type**: OData v2
**Base Path**: /odata/v2/RCMAdminReassignOfferApprover

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| applicationId | int64 | Yes | Application ID (composite key) |
| currUserId | string | Yes | Current user ID (composite key) |
| offerDetailId | int64 | Yes | Offer detail ID (composite key) |
| candidateName | string | No | Candidate name |
| jobReqId | int64 | No | Reference to job requisition |
| jobReqTitle | string | No | Job requisition title |
| targetUserId | string | No | Target user ID |

#### Primary Keys
- `applicationId` (int64)
- `currUserId` (string)
- `offerDetailId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /RCMAdminReassignOfferApprover | List all records | $skip, $top |
| GET | /RCMAdminReassignOfferApprover(applicationId={applicationId},currUserId='{currUserId}',offerDetailId={offerDetailId}) | Get by composite key | N/A |

---

### OfferLetter
**Source File**: RCMOffer.json
**API Type**: OData v2
**Base Path**: /odata/v2/OfferLetter

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| offerLetterId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| body | string | No | Letter body |
| bodyLocale | string | No | Body locale |
| bodyTemplateId | int64 | No | Body template ID |
| bonusPayoutFreq | string | No | Bonus payout frequency |
| candResponseComments | string | No | Candidate response comments |
| candResponseDate | DateTimeOffset | No | Candidate response date |
| comments | string | No | Comments |
| countryCode | string | No | Country code |
| countryName | string | No | Country name |
| createDate | DateTimeOffset | No | Creation date |
| createdBy | string | No | Created by user |
| currencyCode | string | No | Currency code |
| jobStartDate | DateTimeOffset | No | Job start date |
| jobTitle | string | No | Job title |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDate | DateTimeOffset | No | Last modification date |
| locale | string | No | Locale |
| localeCode | string | No | Locale code |
| mailboxes | string | No | Mailboxes |
| offerExpirationDate | DateTimeOffset | No | Offer expiration date |
| offerLetter | base64 | No | Offer letter content |
| offerSentDate | DateTimeOffset | No | Offer sent date |
| overtimeRate | int64 | No | Overtime rate |
| salaryRate | int64 | No | Salary rate |
| salaryRateType | string | No | Salary rate type |
| sendMode | string | No | Send mode |
| status | string | No | Status |
| stockGrant | int64 | No | Stock grant |
| stockOption | int64 | No | Stock option |
| subject | string | No | Subject |
| targetBonusAmount | int64 | No | Target bonus amount |
| targetBonusPercent | int64 | No | Target bonus percent |
| templateId | int64 | No | Template ID |
| templateName | string | No | Template name |
| tokens | string | No | Tokens |

#### Primary Keys
- `offerLetterId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OfferLetter | List all offer letters | $skip, $top |
| GET | /OfferLetter({offerLetterId}) | Get by ID | N/A |

---

### JobOfferApprover
**Source File**: RCMOffer.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobOfferApprover

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| offerApproverId | int64 | Yes | Primary key identifier |
| approvalStepId | string | No | Approval step ID |
| approverAction | string | No | Approver action |
| approverActionDate | DateTimeOffset | No | Approver action date |
| approverFirstName | string | No | Approver first name |
| approverLastName | string | No | Approver last name |
| approverOrder | int64 | No | Approver order |
| comment | string | No | Comment |
| createdBy | string | No | Created by user |
| createdDate | DateTimeOffset | No | Creation date |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDate | DateTimeOffset | No | Last modification date |
| offerApprovalId | int64 | No | Reference to job offer |
| username | string | No | Username |

#### Primary Keys
- `offerApproverId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobOfferApprover | List all approvers | $skip, $top |
| GET | /JobOfferApprover({offerApproverId}) | Get by ID | N/A |

---

### JobOffer
**Source File**: RCMOffer.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobOffer

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| offerApprovalId | int64 | Yes | Primary key identifier |
| annual_FB | decimal | No | Annual flexible budget |
| annual_PF | decimal | No | Annual provident fund |
| annual_SA | decimal | No | Annual special allowance |
| annual_cashPay | decimal | No | Annual cash pay |
| annual_gratuity | decimal | No | Annual gratuity |
| annual_retirals | decimal | No | Annual retirals |
| anonymizedDate | DateTimeOffset | No | Anonymization date |
| anonymizedFlag | string | No | Anonymization flag |
| applicationId | int64 | No | Reference to job application |
| candJust | string | No | Candidate justification |
| candidateName | string | No | Candidate name |
| commission | decimal | No | Commission |
| createdBy | string | No | Created by user |
| createdDate | DateTimeOffset | No | Creation date |
| currency | string | No | Currency |
| currentLocation | string | No | Current location |
| formDataId | int64 | No | Form data ID |
| formTemplateId | int64 | No | Form template ID |
| initialComment | string | No | Initial comment |
| internalStatus | string | No | Internal status |
| jobRateOfPay | decimal | No | Job rate of pay |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDate | DateTimeOffset | No | Last modification date |
| location | string | No | Location |
| monthly_FB | decimal | No | Monthly flexible budget |
| monthly_PF | decimal | No | Monthly provident fund |
| monthly_SA | decimal | No | Monthly special allowance |
| monthly_cashPay | decimal | No | Monthly cash pay |
| monthly_gratuity | decimal | No | Monthly gratuity |
| monthly_retirals | decimal | No | Monthly retirals |
| monthly_salary | decimal | No | Monthly salary |
| redefineTemplateApprovers | string | No | Redefine template approvers |
| salaryBase | decimal | No | Base salary |
| stockPackage | string | No | Stock package |
| targetBonusAmount | decimal | No | Target bonus amount |
| tempDate | string | No | Temporary date |
| templateId | int64 | No | Template ID |
| total_earnings | decimal | No | Total earnings |
| total_fixed_pay | decimal | No | Total fixed pay |
| version | int64 | No | Version |

#### Primary Keys
- `offerApprovalId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobOffer | List all offers | $skip, $top |
| GET | /JobOffer({offerApprovalId}) | Get by ID | N/A |

---

## Objects from RecruitingRCM.json

### JobApplicationInterview
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationInterview

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| applicationInterviewId | int64 | Yes | Primary key identifier |
| applicationId | int64 | No | Reference to job application |
| candSlotMapId | int64 | No | Candidate slot map ID |
| endDate | DateTimeOffset | No | End date |
| isTimeSet | int32 | No | Is time set flag |
| notes | string | No | Notes |
| recruitEventStaffId | int64 | No | Recruit event staff ID |
| source | string | No | Source |
| startDate | DateTimeOffset | No | Start date |
| status | string | No | Status |
| templateType | string | No | Template type |

#### Primary Keys
- `applicationInterviewId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationInterview | List all interviews | $skip, $top |
| GET | /JobApplicationInterview({applicationInterviewId}) | Get by ID | N/A |

---

### InterviewIndividualAssessment
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/InterviewIndividualAssessment

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| interviewIndividualAssessmentId | int64 | Yes | Primary key identifier |
| comments | string | No | Comments |
| interviewOverallAssessmentId | int64 | No | Reference to overall assessment |
| isDeleted | string | No | Is deleted flag |
| rating | string | No | Rating |
| refId | int64 | No | Reference ID |
| type | string | No | Type |

#### Primary Keys
- `interviewIndividualAssessmentId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /InterviewIndividualAssessment | List all assessments | $skip, $top |
| GET | /InterviewIndividualAssessment({interviewIndividualAssessmentId}) | Get by ID | N/A |

---

### JobReqFwdCandidates
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobReqFwdCandidates

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| candidateId | int64 | Yes | Candidate ID (composite key) |
| jobReqId | int64 | Yes | Job requisition ID (composite key) |
| candidateSiteid | int64 | No | Candidate site ID |
| createdDate | DateTimeOffset | No | Creation date |
| expirationDate | DateTimeOffset | No | Expiration date |
| extRecruiterId | int64 | No | External recruiter ID |
| jobBoardName | string | No | Job board name |
| lastModifiedDate | DateTimeOffset | No | Last modification date |
| rcmAppStatusSetItemId | int64 | No | Application status set item ID |
| referralId | int64 | No | Referral ID |
| referralKey | string | No | Referral key |
| referredBy | string | No | Referred by |
| status | string | No | Status |
| type | string | No | Type |

#### Primary Keys
- `candidateId` (int64)
- `jobReqId` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate for change tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobReqFwdCandidates | List all forwarded candidates | $skip, $top |
| GET | /JobReqFwdCandidates(candidateId={candidateId},jobReqId={jobReqId}) | Get by composite key | N/A |

---

### JobApplicationAudit
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobApplicationAudit

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| fieldOrderPos | int64 | Yes | Field order position (composite key) |
| revNumber | int64 | Yes | Revision number (composite key) |
| changedBy | string | No | Changed by user |
| clobFieldRef | string | No | CLOB field reference |
| clobNewValueXML | string | No | New value XML |
| clobOldValueXML | string | No | Old value XML |
| dateNewValue | DateTimeOffset | No | New date value |
| dateOldValue | DateTimeOffset | No | Old date value |
| fieldId | string | No | Field ID |
| fieldType | string | No | Field type |
| jobPostEndDate | DateTimeOffset | No | Job post end date |
| jobPostStartDate | DateTimeOffset | No | Job post start date |
| jobPostingId | int64 | No | Job posting ID |
| lastModifiedBy | string | No | Last modified by user |
| lastModifiedDate | DateTimeOffset | No | Last modification date |
| lastModifiedExtId | int64 | No | Last modified external ID |
| mergedFrom | string | No | Merged from |
| newValue | string | No | New value |
| oldValue | string | No | Old value |
| refType | string | No | Reference type |
| revType | int32 | No | Revision type |
| source | string | No | Source |

#### Primary Keys
- `fieldOrderPos` (int64)
- `revNumber` (int64)

#### Ingestion Type
- **Type**: append
- **Cursor Field**: lastModifiedDate
- **Rationale**: Audit trail table - new records are appended with revision numbers

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /JobApplicationAudit | List all audit records | $skip, $top |
| GET | /JobApplicationAudit(fieldOrderPos={fieldOrderPos},revNumber={revNumber}) | Get by composite key | N/A |

---

### InterviewOverallAssessment
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/InterviewOverallAssessment

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| interviewOverallAssessmentId | int64 | Yes | Primary key identifier |
| averageRating | double | No | Average rating |
| comments | string | No | Comments |
| interviewRefId | int64 | No | Interview reference ID |
| overallRating | string | No | Overall rating |
| type | string | No | Type |

#### Primary Keys
- `interviewOverallAssessmentId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking field available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /InterviewOverallAssessment | List all assessments | $skip, $top |
| GET | /InterviewOverallAssessment({interviewOverallAssessmentId}) | Get by ID | N/A |

---

### RcmCompetency
**Source File**: RecruitingRCM.json
**API Type**: OData v2
**Base Path**: /odata/v2/RcmCompetency

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| rcmCompetencyId | int64 | Yes | Primary key identifier |
| category | string | No | Category |
| commonCompetencyId | int64 | No | Common competency ID |
| desc | string | No | Description |
| locale | string | No | Locale |
| name | string | No | Name |
| source | string | No | Source |
| type | string | No | Type |

#### Primary Keys
- `rcmCompetencyId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Reference/configuration data

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /RcmCompetency | List all competencies | $skip, $top |
| GET | /RcmCompetency({rcmCompetencyId}) | Get by ID | N/A |

---

## Service Operations (Function Imports)

### RCMOffer.json Service Operations

| Operation | Method | Description | Parameters |
|-----------|--------|-------------|------------|
| /approveOffer | GET | Approve a job offer | applicationId (int64), comment (string) |
| /declineOffer | GET | Decline a job offer | applicationId (int64), comment (string) |
| /sendOfferForApproval | GET | Send offer for approval | applicationId (int64) |
| /sendMailOfferLetter | GET | Send offer letter by mail | offerLetterId (int64), sendMode (string), bodyTemplateId (int64), bodyLocale (string) |

### RecruitingRCM.json Service Operations

| Operation | Method | Description | Parameters |
|-----------|--------|-------------|------------|
| /fwdCandidateToColleague | GET | Forward candidate to colleague | candidateId (int64), referredTo (string) |
| /initiateOnboarding | GET | Initiate onboarding process | applicationId (int64) |
| /getRecruitingTemplate | GET | Get recruiting template | templateName (string), templateType (string) |
| /getOfferLetterTemplate | GET | Get offer letter template | templateName (string), templateType (string) |
| /inviteToApply | POST | Invite candidates to apply | jobReqId (int64), candidateIds (string) |

### RCMJobRequisition.json Service Operations

| Operation | Method | Description | Parameters |
|-----------|--------|-------------|------------|
| /reassignJobReq | GET | Reassign job requisition | Various parameters |
| /sendJobReqToPreviousStep | GET | Send job requisition to previous step | Various parameters |
| /addModifierToJobReq | GET | Add modifier to job requisition | Various parameters |
| /refreshInterviewAssessments | POST | Refresh interview assessments | Various parameters |

---

## Pagination

All entity collection endpoints support OData v2 pagination:

| Parameter | Description |
|-----------|-------------|
| $top | Limit number of returned entities (default: 20) |
| $skip | Skip specified number of entities |
| $count | Include total count in response |
| $inlinecount=allpages | Include total count inline |
| $filter | Filter entities by property values |
| $orderby | Order entities by property values |
| $select | Select specific properties to return |
| $expand | Expand related navigation properties |

---

## Ingestion Type Summary

| Ingestion Type | Count | Description |
|----------------|-------|-------------|
| cdc | 28 | Change data capture using lastModifiedDateTime/lastModifiedDate |
| cdc_with_deletes | 1 | CDC with soft delete tracking (JobRequisition) |
| snapshot | 22 | Full snapshot load, no change tracking |
| append | 2 | Append-only audit trail tables |

---

## Entity Relationships

### Key Relationships

1. **Candidate -> CandidateBackground_***: One-to-many relationship for candidate background information
2. **JobApplication -> Candidate**: Many-to-one relationship via candidateId
3. **JobApplication -> JobRequisition**: Many-to-one relationship via jobReqId
4. **JobApplication -> JobApplicationSnapshot_***: One-to-many for snapshot data
5. **JobRequisition -> JobRequisitionPosting**: One-to-many for job postings
6. **JobRequisition -> JobRequisitionOperator**: One-to-many for operators
7. **JobOffer -> JobApplication**: Many-to-one via applicationId
8. **JobOffer -> JobOfferApprover**: One-to-many for approvers
9. **JobApplicationInterview -> InterviewOverallAssessment**: One-to-one relationship
10. **InterviewOverallAssessment -> InterviewIndividualAssessment**: One-to-many relationship
