# SAP SuccessFactors API Documentation - Employee Central Core

## Segment Overview
- **Segment**: 1 - Employee Central Core
- **Files Processed**: 5
- **Entities Documented**: 22 (core entities documented, ECFoundationOrganization contains 50+ additional entities)
- **Endpoints Documented**: 44+ GET endpoints
- **Focus**: Employment records, job information, organizational structure, payroll integration

## Source Files Summary

| File | API Title | Description |
|------|-----------|-------------|
| ECEmploymentInformation.json | Employment Information | Employment-related information including job info, termination, work permits |
| ECFoundationOrganization.json | Foundation | Organization, job structure, and pay foundation objects |
| ECEmployeeCentralPayroll.json | Employee Central Payroll | Replicated payroll run results and items |
| ECDismissalProtection.json | Dismissal Protection | Employee dismissal protection data |
| EmpCostAssignment.json | Employee Cost Assignment | Cost center assignment for employees |

---

## Objects from ECEmploymentInformation.json

### EmpEmployment
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpEmployment

#### Description
Core employment record containing employee employment details including dates, stock eligibility, and status information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| personIdExternal | string (100) | Yes | External person identifier |
| userId | string (100) | Yes | User identifier |
| StockEndDate | string (date) | No | Stock end date |
| assignmentClass | string (128) | No | Assignment class |
| benefitsEligibilityStartDate | string (date) | No | Benefits eligibility start date |
| benefitsEndDate | string (date) | No | Benefits end date |
| bonusPayExpirationDate | string (date) | No | Bonus pay expiration date |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| eligibleForSalContinuation | boolean | No | Eligible for salary continuation |
| eligibleForStock | boolean | No | Eligible for stock |
| employeeFirstEmployment | boolean | No | First employment flag |
| endDate | string (date) | No | Employment end date |
| firstDateWorked | string (date) | No | First date worked |
| isContingentWorker | boolean | No | Contingent worker flag |
| isECRecord | boolean | No | Employee Central record flag |
| jobNumber | int64 | No | Job number |
| lastDateWorked | string (date) | No | Last date worked |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| okToRehire | boolean | No | OK to rehire flag |
| originalStartDate | string (date) | No | Original start date |
| payrollEndDate | string (date) | No | Payroll end date |
| prevEmployeeId | string (256) | No | Previous employee ID |
| regretTermination | boolean | No | Regret termination flag |
| salaryEndDate | string (date) | No | Salary end date |
| seniorityDate | string (date) | No | Seniority date |
| serviceDate | string (date) | No | Service date |
| startDate | string (date) | No | Employment start date |

#### Primary Keys
- `personIdExternal` (string)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime field for tracking changes; personIdExternal and userId form composite key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpEmployment | List all employment records | $skip, $top, $count |
| GET | /EmpEmployment(personIdExternal='{personIdExternal}',userId='{userId}') | Get by composite key | N/A |

---

### EmpEmploymentTermination
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpEmploymentTermination

#### Description
Employment termination records containing end dates, reasons, and termination-specific information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| endDate | string (date) | Yes | Termination end date |
| personIdExternal | string (100) | Yes | External person identifier |
| userId | string (100) | Yes | User identifier |
| StockEndDate | string (date) | No | Stock end date |
| attachmentId | string | No | Attachment identifier |
| benefitsEndDate | string (date) | No | Benefits end date |
| bonusPayExpirationDate | string (date) | No | Bonus pay expiration date |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| eligibleForSalContinuation | boolean | No | Salary continuation eligibility |
| eventReason | string | No | Event reason |
| lastDateWorked | string (date) | No | Last date worked |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| newMainEmploymentId | decimal | No | New main employment ID |
| notes | string (4000) | No | Notes |
| okToRehire | boolean | No | OK to rehire flag |
| payrollEndDate | string (date) | No | Payroll end date |
| regretTermination | boolean | No | Regret termination flag |
| salaryEndDate | string (date) | No | Salary end date |

#### Primary Keys
- `endDate` (date)
- `personIdExternal` (string)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with endDate, personIdExternal, userId

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpEmploymentTermination | List all terminations | $skip, $top, $count |
| GET | /EmpEmploymentTermination(endDate={endDate},personIdExternal='{personIdExternal}',userId='{userId}') | Get by key | N/A |

---

### EmpJob
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpJob

#### Description
Job information records containing position, compensation, organizational assignment, and work schedule details.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| seqNumber | int64 | Yes | Sequence number |
| startDate | string (date) | Yes | Job start date |
| userId | string (100) | Yes | User identifier |
| businessUnit | string (32) | No | Business unit |
| company | string (32) | No | Company |
| contractType | string (256) | No | Contract type |
| costCenter | string (32) | No | Cost center |
| countryOfCompany | string (256) | No | Country of company |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| department | string (32) | No | Department |
| division | string (32) | No | Division |
| emplStatus | string (32) | No | Employment status |
| employeeClass | string (256) | No | Employee class |
| employmentType | string (32) | No | Employment type |
| endDate | string (date) | No | Job end date |
| event | string (32) | No | Event type |
| eventReason | string | No | Event reason |
| fte | double | No | Full-time equivalent |
| isFulltimeEmployee | boolean | No | Full-time employee flag |
| jobCode | string (32) | No | Job code |
| jobTitle | string (256) | No | Job title |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| location | string (128) | No | Location |
| managerId | string (256) | No | Manager ID |
| payGrade | string (256) | No | Pay grade |
| payScaleArea | string (128) | No | Pay scale area |
| payScaleGroup | string (128) | No | Pay scale group |
| payScaleLevel | string (128) | No | Pay scale level |
| payScaleType | string (128) | No | Pay scale type |
| position | string (128) | No | Position |
| positionEntryDate | string (date) | No | Position entry date |
| probationPeriodEndDate | string (date) | No | Probation period end date |
| regularTemp | string (32) | No | Regular/temporary status |
| standardHours | double | No | Standard hours |
| timezone | string (128) | No | Timezone |
| workLocation | string (256) | No | Work location |
| workerCategory | string (256) | No | Worker category |
| workingDaysPerWeek | double | No | Working days per week |
| workscheduleCode | string (128) | No | Work schedule code |

#### Primary Keys
- `seqNumber` (int64)
- `startDate` (date)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with seqNumber, startDate, userId

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpJob | List all job records | $skip, $top, $count |
| GET | /EmpJob(seqNumber={seqNumber},startDate={startDate},userId='{userId}') | Get by key | N/A |

---

### EmpWorkPermit
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpWorkPermit

#### Description
Work permit and immigration document records for employees.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| country | string (256) | Yes | Country |
| documentNumber | string (256) | Yes | Document number |
| documentType | string (256) | Yes | Document type |
| userId | string (100) | Yes | User identifier |
| attachment | base64 | No | Attachment content |
| attachmentFileName | string (256) | No | Attachment file name |
| attachmentFileSize | decimal | No | Attachment file size |
| attachmentFileType | string (5) | No | Attachment file type |
| attachmentId | string | No | Attachment ID |
| attachmentMimeType | string (256) | No | Attachment MIME type |
| attachmentStatus | decimal | No | Attachment status |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| documentTitle | string (256) | No | Document title |
| expirationDate | string (date) | No | Expiration date |
| isValidated | boolean | No | Validation flag |
| issueDate | string (date) | No | Issue date |
| issuePlace | string (256) | No | Issue place |
| issuingAuthority | string (256) | No | Issuing authority |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| notes | string (4000) | No | Notes |

#### Primary Keys
- `country` (string)
- `documentNumber` (string)
- `documentType` (string)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with country, documentNumber, documentType, userId

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpWorkPermit | List all work permits | $skip, $top, $count |
| GET | /EmpWorkPermit(country='{country}',documentNumber='{documentNumber}',documentType='{documentType}',userId='{userId}') | Get by key | N/A |

---

### EmpJobRelationships
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpJobRelationships

#### Description
Job relationships between employees (e.g., manager, mentor, HR business partner).

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| relationshipType | string (100) | Yes | Relationship type |
| startDate | string (date) | Yes | Start date |
| userId | string (100) | Yes | User identifier |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| endDate | string (date) | No | End date |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| operation | string | No | Operation type |
| relUserId | string (384) | No | Related user ID |

#### Primary Keys
- `relationshipType` (string)
- `startDate` (date)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with relationshipType, startDate, userId

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpJobRelationships | List all job relationships | $skip, $top, $count |
| GET | /EmpJobRelationships(relationshipType='{relationshipType}',startDate={startDate},userId='{userId}') | Get by key | N/A |

---

### EmpBeneficiary
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpBeneficiary

#### Description
Employee beneficiary information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| personIdExternal | string (100) | Yes | External person identifier |
| userId | string (100) | Yes | User identifier |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| endDate | string (date) | No | End date |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| payrollEndDate | string (date) | No | Payroll end date |
| plannedEndDate | string (date) | No | Planned end date |
| startDate | string (date) | No | Start date |

#### Primary Keys
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime field; userId as primary key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpBeneficiary | List all beneficiary records | $skip, $top, $count |
| GET | /EmpBeneficiary('{userId}') | Get by userId | N/A |

---

### EmpPensionPayout
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpPensionPayout

#### Description
Employee pension payout information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| personIdExternal | string (100) | Yes | External person identifier |
| userId | string (100) | Yes | User identifier |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| endDate | string (date) | No | End date |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| payrollEndDate | string (date) | No | Payroll end date |
| plannedEndDate | string (date) | No | Planned end date |
| startDate | string (date) | No | Start date |

#### Primary Keys
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; userId as primary key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpPensionPayout | List all pension payouts | $skip, $top, $count |
| GET | /EmpPensionPayout('{userId}') | Get by userId | N/A |

---

### PersonEmpTerminationInfo
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/PersonEmpTerminationInfo

#### Description
Person-level employment termination summary information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| personIdExternal | string (100) | Yes | External person identifier |
| activeEmploymentsCount | int32 | No | Count of active employments |
| latestTerminationDate | string (date) | No | Latest termination date |

#### Primary Keys
- `personIdExternal` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field; read-only aggregate view

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /PersonEmpTerminationInfo | List all termination info | $skip, $top, $count |
| GET | /PersonEmpTerminationInfo('{personIdExternal}') | Get by personIdExternal | N/A |

---

### HireDateChange
**Source File**: ECEmploymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/HireDateChange

#### Description
Hire date change records for tracking modifications to employee hire dates.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | string (128) | Yes | Unique code |
| createdBy | string (255) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| lastModifiedBy | string (255) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| mdfSystemRecordStatus | string (255) | No | MDF system record status |
| newHireDate | string (date) | No | New hire date |
| originalHireDate | string (date) | No | Original hire date |
| processingStatus | string (128) | No | Processing status |
| usersSysId | string (100) | No | User system ID |

#### Primary Keys
- `code` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; code as primary key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /HireDateChange | List all hire date changes | $skip, $top, $count |
| GET | /HireDateChange('{code}') | Get by code | N/A |

---

## Objects from ECEmployeeCentralPayroll.json

### EmployeePayrollRunResults
**Source File**: ECEmployeeCentralPayroll.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmployeePayrollRunResults

#### Description
Replicated payroll run results containing pay date, currency, and payroll provider information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string (128) | Yes | External code identifier |
| mdfSystemEffectiveStartDate | string (date) | Yes | Effective start date |
| clientId | string (255) | No | Client ID |
| companyId | string (128) | No | Company ID |
| createdBy | string (255) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| currency | string (128) | No | Currency |
| employmentId | string (255) | No | Employment ID |
| endDateWhenPaid | string (date) | No | End date when paid |
| externalName | string (128) | No | External name |
| isVoid | boolean | No | Void flag |
| lastModifiedBy | string (255) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| mdfSystemEffectiveEndDate | string (date) | No | Effective end date |
| mdfSystemRecordStatus | string (255) | No | Record status |
| mdfSystemStatus | string (255) | No | System status |
| payDate | string (date) | No | Pay date |
| payrollId | string (255) | No | Payroll ID |
| payrollProviderId | string (255) | No | Payroll provider ID |
| payrollRunType | string (128) | No | Payroll run type |
| personId | string (255) | No | Person ID |
| sequenceNumber | string (255) | No | Sequence number |
| startDateWhenPaid | string (date) | No | Start date when paid |
| systemId | string (255) | No | System ID |
| userId | string (100) | No | User ID |

#### Primary Keys
- `externalCode` (string)
- `mdfSystemEffectiveStartDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with externalCode and mdfSystemEffectiveStartDate

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmployeePayrollRunResults | List all payroll results | $skip, $top, $count |
| GET | /EmployeePayrollRunResults(externalCode='{externalCode}',mdfSystemEffectiveStartDate={mdfSystemEffectiveStartDate}) | Get by key | N/A |

---

### EmployeePayrollRunResultsItems
**Source File**: ECEmployeeCentralPayroll.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmployeePayrollRunResultsItems

#### Description
Line items for payroll run results containing wage types, amounts, and quantities.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| EmployeePayrollRunResults_externalCode | string (128) | Yes | Parent external code |
| EmployeePayrollRunResults_mdfSystemEffectiveStartDate | string (date) | Yes | Parent effective start date |
| externalCode | string (128) | Yes | Item external code |
| amount | decimal | No | Amount |
| createdBy | string (255) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| endDateWhenEarned | string (date) | No | End date when earned |
| externalName | string (128) | No | External name |
| groupingReason | string (128) | No | Grouping reason |
| lastModifiedBy | string (255) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| mdfSystemRecordStatus | string (255) | No | Record status |
| payrollProviderWageType | string (255) | No | Payroll provider wage type |
| quantity | decimal | No | Quantity |
| startDateWhenEarned | string (date) | No | Start date when earned |
| unitOfMeasurement | string (128) | No | Unit of measurement |
| wageType | string (128) | No | Wage type |

#### Primary Keys
- `EmployeePayrollRunResults_externalCode` (string)
- `EmployeePayrollRunResults_mdfSystemEffectiveStartDate` (date)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key linking to parent result

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmployeePayrollRunResultsItems | List all payroll items | $skip, $top, $count |
| GET | /EmployeePayrollRunResultsItems(EmployeePayrollRunResults_externalCode='{...}',EmployeePayrollRunResults_mdfSystemEffectiveStartDate={...},externalCode='{externalCode}') | Get by key | N/A |

---

## Objects from ECDismissalProtection.json

### EmployeeDismissalProtection
**Source File**: ECDismissalProtection.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmployeeDismissalProtection

#### Description
Employee dismissal protection records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| workerId | string (100) | Yes | Worker identifier |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| mdfSystemRecordStatus | string (255) | No | Record status |

#### Primary Keys
- `workerId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; workerId as primary key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmployeeDismissalProtection | List all protection records | $skip, $top, $count |
| GET | /EmployeeDismissalProtection('{workerId}') | Get by workerId | N/A |

---

### EmployeeDismissalProtectionDetail
**Source File**: ECDismissalProtection.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmployeeDismissalProtectionDetail

#### Description
Detailed dismissal protection information with protection type and date ranges.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| EmployeeDismissalProtection_workerId | string (100) | Yes | Parent worker ID |
| externalCode | string (128) | Yes | External code |
| createdBy | string (100) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| dismissalProtectionType | string (128) | No | Dismissal protection type |
| lastModifiedBy | string (100) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| mdfSystemRecordStatus | string (255) | No | Record status |
| protectionEndDate | string (date) | No | Protection end date |
| protectionStartDate | string (date) | No | Protection start date |

#### Primary Keys
- `EmployeeDismissalProtection_workerId` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with parent workerId and externalCode

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmployeeDismissalProtectionDetail | List all protection details | $skip, $top, $count |
| GET | /EmployeeDismissalProtectionDetail(EmployeeDismissalProtection_workerId='{workerId}',externalCode='{externalCode}') | Get by key | N/A |

---

## Objects from EmpCostAssignment.json

### EmpCostAssignment
**Source File**: EmpCostAssignment.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpCostAssignment

#### Description
Employee cost assignment records defining organizational assignment and cost center allocation.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| effectiveStartDate | string (date) | Yes | Effective start date |
| worker | string (100) | Yes | Worker identifier |
| companyCode | string (4) | No | Company code |
| createdBy | string (100) | No | Created by user (read-only) |
| createdDateTime | string (date) | No | Creation timestamp (read-only) |
| doNotSyncFromPositionCostAssignment | boolean | No | Skip position cost sync flag |
| effectiveEndDate | string (date) | No | Effective end date (read-only) |
| lastModifiedBy | string (100) | No | Last modified by user (read-only) |
| lastModifiedDateTime | string (date) | No | Last modification timestamp (read-only) |
| mdfSystemRecordStatus | string (255) | No | Record status (C/D/F/N/P/PH) |
| mdfSystemStatus | string (128) | No | System status (A/I) |
| skipValidationDerivation | boolean | No | Skip validation flag |

#### Primary Keys
- `effectiveStartDate` (date)
- `worker` (string)

#### Ingestion Type
- **Type**: cdc_with_deletes
- **Cursor Field**: lastModifiedDateTime
- **Soft Delete Field**: mdfSystemRecordStatus = 'D'
- **Rationale**: Has lastModifiedDateTime; mdfSystemRecordStatus 'D' indicates soft-deleted records

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpCostAssignment | List all cost assignments | $skip, $top, $count |
| GET | /EmpCostAssignment(effectiveStartDate=datetime'{effectiveStartDate}',worker='{worker}') | Get by key | N/A |

---

## Objects from ECFoundationOrganization.json

### FODepartment
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FODepartment

#### Description
Foundation Object for organizational departments with multilingual name and description support.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string (32) | Yes | External code |
| startDate | string (date) | Yes | Start date |
| costCenter | string (128) | No | Cost center |
| createdBy | string (255) | No | Created by user |
| createdDateTime | string (date) | No | Creation timestamp |
| description | string (128) | No | Description |
| description_localized | string (128) | No | Localized description |
| endDate | string (date) | No | End date |
| headOfUnit | string (100) | No | Head of unit |
| lastModifiedBy | string (255) | No | Last modified by user |
| lastModifiedDateTime | string (date) | No | Last modification timestamp |
| name | string (32) | No | Name |
| name_localized | string (32) | No | Localized name |
| parent | string (128) | No | Parent department |
| status | string (255) | No | Status |

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime; composite key with externalCode and startDate

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FODepartment | List all departments | $skip, $top, $count |
| GET | /FODepartment(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FODivision
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FODivision

#### Description
Foundation Object for organizational divisions.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FODivision | List all divisions | $skip, $top, $count |
| GET | /FODivision(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOBusinessUnit
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOBusinessUnit

#### Description
Foundation Object for business units.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOBusinessUnit | List all business units | $skip, $top, $count |
| GET | /FOBusinessUnit(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOCompany
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOCompany

#### Description
Foundation Object for companies/legal entities.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOCompany | List all companies | $skip, $top, $count |
| GET | /FOCompany(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOCostCenter
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOCostCenter

#### Description
Foundation Object for cost centers.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOCostCenter | List all cost centers | $skip, $top, $count |
| GET | /FOCostCenter(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOJobCode
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOJobCode

#### Description
Foundation Object for job codes.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOJobCode | List all job codes | $skip, $top, $count |
| GET | /FOJobCode(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOLocation
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOLocation

#### Description
Foundation Object for locations.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOLocation | List all locations | $skip, $top, $count |
| GET | /FOLocation(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### FOPayGrade
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/FOPayGrade

#### Description
Foundation Object for pay grades.

#### Primary Keys
- `externalCode` (string)
- `startDate` (date)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /FOPayGrade | List all pay grades | $skip, $top, $count |
| GET | /FOPayGrade(externalCode='{externalCode}',startDate={startDate}) | Get by key | N/A |

---

### Territory
**Source File**: ECFoundationOrganization.json
**API Type**: OData v2
**Base Path**: /odata/v2/Territory

#### Description
Territory/Country lookup table.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| territoryCode | string (32) | Yes | Territory code |
| territoryName | string (512) | No | Territory name |

#### Primary Keys
- `territoryCode` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Static reference data without modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Territory | List all territories | $skip, $top, $count |
| GET | /Territory('{territoryCode}') | Get by territoryCode | N/A |

---

## Common Pagination Parameters

All OData v2 APIs in this segment support standard OData pagination:

| Parameter | Description | Default |
|-----------|-------------|---------|
| $top | Maximum number of records to return | 20 |
| $skip | Number of records to skip | 0 |
| $count | Include total count in response | false |
| $filter | OData filter expression | None |
| $orderby | Sort order specification | None |
| $select | Fields to include in response | All |
| $expand | Related entities to expand | None |

### Pagination Strategy
- Use `$skip` and `$top` for offset-based pagination
- Use `$inlinecount=allpages` to get total record count
- For incremental sync, filter on `lastModifiedDateTime gt datetime'{cursor}'`

---

## Ingestion Type Summary

| Entity | Ingestion Type | Cursor Field | Notes |
|--------|---------------|--------------|-------|
| EmpEmployment | cdc | lastModifiedDateTime | Composite key |
| EmpEmploymentTermination | cdc | lastModifiedDateTime | Composite key |
| EmpJob | cdc | lastModifiedDateTime | Composite key |
| EmpWorkPermit | cdc | lastModifiedDateTime | Composite key |
| EmpJobRelationships | cdc | lastModifiedDateTime | Composite key |
| EmpBeneficiary | cdc | lastModifiedDateTime | Single key |
| EmpPensionPayout | cdc | lastModifiedDateTime | Single key |
| PersonEmpTerminationInfo | snapshot | N/A | Aggregate view |
| HireDateChange | cdc | lastModifiedDateTime | Single key |
| EmployeePayrollRunResults | cdc | lastModifiedDateTime | Composite key |
| EmployeePayrollRunResultsItems | cdc | lastModifiedDateTime | Composite key |
| EmployeeDismissalProtection | cdc | lastModifiedDateTime | Single key |
| EmployeeDismissalProtectionDetail | cdc | lastModifiedDateTime | Composite key |
| EmpCostAssignment | cdc_with_deletes | lastModifiedDateTime | mdfSystemRecordStatus='D' for deletes |
| FODepartment | cdc | lastModifiedDateTime | Composite key |
| FODivision | cdc | lastModifiedDateTime | Composite key |
| FOBusinessUnit | cdc | lastModifiedDateTime | Composite key |
| FOCompany | cdc | lastModifiedDateTime | Composite key |
| FOCostCenter | cdc | lastModifiedDateTime | Composite key |
| FOJobCode | cdc | lastModifiedDateTime | Composite key |
| FOLocation | cdc | lastModifiedDateTime | Composite key |
| FOPayGrade | cdc | lastModifiedDateTime | Composite key |
| Territory | snapshot | N/A | Static reference data |
