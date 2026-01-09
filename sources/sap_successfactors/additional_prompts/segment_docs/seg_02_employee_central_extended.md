# SAP SuccessFactors API Documentation - Employee Central Extended

## Segment Overview
- **Segment**: 2 - Employee Central Extended
- **Files Processed**: 6
- **Entities Documented**: 118
- **Endpoints Documented**: 236

## Source Files
1. ECPaymentInformation.json - Payment Information (country-specific)
2. ECCompensationInformation.json - Compensation Information
3. ECGlobalBenefits.json - Global Benefits
4. ECAdvances.json - Payroll Advances
5. ECSkillsManagement.json - Skills Management
6. sap-sf-EmpEmploymentHigherDuty-v1.json - Higher Duty Employment

---

## ECPaymentInformation.json

### PaymentInformationV3
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/PaymentInformationV3

#### Description
Main payment information entity for employees, containing effective-dated payment records.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| worker | string | Yes | User ID of the employee (max 100) |
| effectiveStartDate | DateTime | Yes | Start date for payment information |
| effectiveEndDate | DateTime | No | End date for payment information |
| effectiveStatus | string | No | Status of the record |
| createdBy | string | No | User who created the record |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | User who last modified |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | MDF record status |

#### Primary Keys
- `worker` (string)
- `effectiveStartDate` (DateTime)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime field for tracking changes, combined with composite primary key

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /PaymentInformationV3 | List all payment information | $skip, $top |
| GET | /PaymentInformationV3(effectiveStartDate={date},worker='{id}') | Get by key | N/A |

---

### PaymentInformationDetailV3
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/PaymentInformationDetailV3

#### Description
Detailed payment information including bank account details, payment methods, and amounts.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| PaymentInformationV3_effectiveStartDate | DateTime | Yes | Parent effective start date |
| PaymentInformationV3_worker | string | Yes | Parent worker ID |
| externalCode | int64 | Yes | External code identifier |
| accountNumber | string | No | Bank account number (max 255) |
| accountOwner | string | No | Account owner name (max 255) |
| amount | decimal | No | Payment amount |
| bank | string | No | Bank identifier (max 128) |
| bankCountry | string | No | Bank country code (max 128) |
| businessIdentifierCode | string | No | SWIFT/BIC code (max 11) |
| iban | string | No | IBAN (max 35) |
| currency | string | No | Currency code (max 128) |
| payType | string | No | Pay type (max 255) |
| paySequence | int64 | No | Payment sequence order |
| paymentMethod | string | No | Payment method (max 128) |
| percent | decimal | No | Percentage of payment |
| purpose | string | No | Payment purpose (max 40) |
| routingNumber | string | No | Bank routing number (max 255) |
| customPayType | string | No | Custom pay type reference |
| createdBy | string | No | Creator user ID |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier user ID |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |

#### Primary Keys
- `PaymentInformationV3_effectiveStartDate` (DateTime)
- `PaymentInformationV3_worker` (string)
- `externalCode` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime for incremental sync with composite keys

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /PaymentInformationDetailV3 | List all details | $skip, $top |
| GET | /PaymentInformationDetailV3(...) | Get by composite key | N/A |

---

### PaymentInformationDetailV3 (Country-Specific Variants)
**Source File**: ECPaymentInformation.json

The following country-specific entities extend PaymentInformationDetailV3 with country-specific fields:

| Entity | Country | Additional Fields |
|--------|---------|-------------------|
| PaymentInformationDetailV3ARG | Argentina | accountType |
| PaymentInformationDetailV3BRA | Brazil | accountType, bankCode |
| PaymentInformationDetailV3CHL | Chile | accountType |
| PaymentInformationDetailV3COL | Colombia | accountType |
| PaymentInformationDetailV3CZE | Czech Republic | specificSymbol, variableSymbol |
| PaymentInformationDetailV3ECU | Ecuador | accountType |
| PaymentInformationDetailV3ESP | Spain | controlKey |
| PaymentInformationDetailV3FRA | France | controlKey |
| PaymentInformationDetailV3GBR | Great Britain | buildingSocietyNumber |
| PaymentInformationDetailV3GHA | Ghana | accountType |
| PaymentInformationDetailV3IRQ | Iraq | accountType |
| PaymentInformationDetailV3ISR | Israel | branchName, branchNumberCode |
| PaymentInformationDetailV3ITA | Italy | controlKey |
| PaymentInformationDetailV3JPN | Japan | accountType, bankCode, branchCode |
| PaymentInformationDetailV3KEN | Kenya | accountType |
| PaymentInformationDetailV3MEX | Mexico | accountType, clabe |
| PaymentInformationDetailV3MKD | Macedonia | accountType |
| PaymentInformationDetailV3MMR | Myanmar | accountType |
| PaymentInformationDetailV3MOZ | Mozambique | accountType |
| PaymentInformationDetailV3MWI | Malawi | accountType |
| PaymentInformationDetailV3NAM | Namibia | accountType |
| PaymentInformationDetailV3NGA | Nigeria | accountType |
| PaymentInformationDetailV3NZL | New Zealand | accountSuffix |
| PaymentInformationDetailV3PER | Peru | accountType |
| PaymentInformationDetailV3PRY | Paraguay | accountType |
| PaymentInformationDetailV3BOL | Bolivia | accountType |
| PaymentInformationDetailV3SVK | Slovakia | specificSymbol, variableSymbol |
| PaymentInformationDetailV3SVN | Slovenia | controlKey |
| PaymentInformationDetailV3SUR | Suriname | accountType |
| PaymentInformationDetailV3TUN | Tunisia | accountType |
| PaymentInformationDetailV3USA | United States | accountType |
| PaymentInformationDetailV3VEN | Venezuela | accountType |
| PaymentInformationDetailV3ZAF | South Africa | accountType |
| PaymentInformationDetailV3ZWE | Zimbabwe | accountType |

All country-specific entities share the same primary keys and ingestion type (cdc with lastModifiedDateTime cursor).

---

### PaymentMethodV3
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/PaymentMethodV3

#### Description
Payment method configuration entity with localized names.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code identifier (max 128) |
| externalName_defaultValue | string | No | Default name (max 255) |
| externalName_en_US | string | No | English US name |
| externalName_localized | string | No | Localized name |
| createdBy | string | No | Creator user ID |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier user ID |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Configuration entity with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /PaymentMethodV3 | List all payment methods | $skip, $top |
| GET | /PaymentMethodV3('{externalCode}') | Get by external code | N/A |

---

### PaymentMethodAssignmentV3
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/PaymentMethodAssignmentV3

#### Description
Assignment of payment methods to legal entities or countries.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| PaymentMethodV3_externalCode | string | Yes | Parent payment method |
| externalCode | int64 | Yes | External code identifier |
| country | string | No | Country code |
| createdBy | string | No | Creator user ID |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `PaymentMethodV3_externalCode` (string)
- `externalCode` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has modification tracking fields

---

### CustomPayType
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/CustomPayType

#### Description
Custom pay type definitions with localized names.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| externalName_defaultValue | string | No | Default name |
| externalName_localized | string | No | Localized name |
| standardPayType | string | No | Standard pay type mapping |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Configuration entity with modification tracking

---

### CustomPayTypeAssignment
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/CustomPayTypeAssignment

#### Description
Assignment of custom pay types to countries.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| CustomPayType_externalCode | string | Yes | Parent custom pay type |
| externalCode | int64 | Yes | External code |
| country | string | No | Country code |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `CustomPayType_externalCode` (string)
- `externalCode` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has modification tracking fields

---

### Bank
**Source File**: ECPaymentInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/Bank

#### Description
Bank master data with localized bank names and routing information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | Bank code identifier |
| bankName | string | No | Bank name |
| bankCountry | string | No | Country of the bank |
| routingNumber | string | No | Bank routing number |
| businessIdentifierCode | string | No | SWIFT/BIC code |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Master data entity with change tracking

---

## ECCompensationInformation.json

### EmpCompensation
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpCompensation

#### Description
Employee compensation information including salary and pay component data.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | string | Yes | User ID (max 100) |
| startDate | DateTime | Yes | Start date of compensation |
| seqNumber | int64 | Yes | Sequence number |
| payGroup | string | No | Pay group |
| payGrade | string | No | Pay grade |
| benefitRate | decimal | No | Benefit rate |
| compaRatio | double | No | Compa ratio |
| currencyCode | string | No | Currency code |
| frequency | string | No | Pay frequency |
| annualSalary | decimal | No | Annual salary |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `userId` (string)
- `startDate` (DateTime)
- `seqNumber` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Employee transactional data with effective dating

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpCompensation | List all compensation records | $skip, $top |
| GET | /EmpCompensation(startDate={date},userId='{id}',seqNumber={seq}) | Get by key | N/A |

---

### EmpCompensationCalculated
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpCompensationCalculated

#### Description
Calculated compensation values including compa-ratio, range penetration, and pay range data.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | string | Yes | User ID |
| startDate | DateTime | Yes | Start date |
| seqNumber | int64 | Yes | Sequence number |
| compaRatio | double | No | Compa-ratio value |
| rangePenetration | double | No | Range penetration percentage |
| yearlyBaseSalary | decimal | No | Annualized base salary |
| currency | string | No | Currency code |
| payRange | string | No | Pay range reference |
| proratedMinPointOfPayRange | decimal | No | Prorated minimum |
| proratedMidPointOfPayRange | decimal | No | Prorated midpoint |
| proratedMaxPointOfPayRange | decimal | No | Prorated maximum |
| errorCode | string | No | Error code if calculation failed |
| errorMessage | string | No | Error message |

#### Primary Keys
- `userId` (string)
- `startDate` (DateTime)
- `seqNumber` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Calculated/derived data without modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpCompensationCalculated | List all calculated records | $skip, $top |
| GET | /EmpCompensationCalculated(seqNumber={seq},startDate={date},userId='{id}') | Get by key | N/A |

---

### EmpCompensationGroupSumCalculated
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpCompensationGroupSumCalculated

#### Description
Calculated group sum of employee compensation.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| seqNumber | int64 | Yes | Sequence number |
| startDate | DateTime | Yes | Start date |
| userId | string | Yes | User ID |
| payComponentGroupId | string | No | Pay component group ID |
| payComponentGroupAmount | decimal | No | Group sum amount |
| currency | string | No | Currency code |

#### Primary Keys
- `userId` (string)
- `startDate` (DateTime)
- `seqNumber` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: Calculated aggregation without modification tracking

---

### EmpPayCompRecurring
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpPayCompRecurring

#### Description
Recurring pay component information for employees.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | string | Yes | User ID (max 100) |
| startDate | DateTime | Yes | Start date |
| seqNumber | int64 | Yes | Sequence number |
| payComponent | string | Yes | Pay component code |
| currencyCode | string | No | Currency code (max 32) |
| paycompvalue | double | No | Pay component value |
| frequency | string | No | Frequency (max 30) |
| endDate | DateTime | No | End date |
| notes | string | No | Notes (max 4000) |
| operation | string | No | Operation type |
| createdBy | string | No | Creator (max 100) |
| createdDateTime | DateTime | No | Creation timestamp |
| createdOn | DateTime | No | Created on date |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| lastModifiedOn | DateTime | No | Last modified on date |

#### Primary Keys
- `userId` (string)
- `startDate` (DateTime)
- `seqNumber` (int64)
- `payComponent` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Transactional data with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpPayCompRecurring | List all recurring pay | $skip, $top |
| GET | /EmpPayCompRecurring(payComponent='{pc}',seqNumber={seq},startDate={date},userId='{id}') | Get by key | N/A |

---

### EmpPayCompNonRecurring
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpPayCompNonRecurring

#### Description
Non-recurring (one-time) pay component information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | string | Yes | User ID |
| payComponentCode | string | Yes | Pay component code |
| payDate | DateTime | Yes | Payment date |
| currencyCode | string | No | Currency code |
| paycompvalue | double | No | Pay component value |
| notes | string | No | Notes |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `userId` (string)
- `payComponentCode` (string)
- `payDate` (DateTime)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Transactional data with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpPayCompNonRecurring | List all non-recurring pay | $skip, $top |
| GET | /EmpPayCompNonRecurring(payComponentCode='{pc}',payDate={date},userId='{id}') | Get by key | N/A |

---

### OneTimeDeduction
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/OneTimeDeduction

#### Description
One-time deduction records for employees.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | int64 | Yes | External code identifier |
| userSysId | string | No | User system ID (max 100) |
| payComponentType | string | No | Pay component type (max 32) |
| amount | decimal | No | Deduction amount |
| equivalentAmount | decimal | No | Equivalent amount |
| currency | string | No | Currency code (max 128) |
| deductionDate | DateTime | No | Deduction date |
| additionalInfo | string | No | Additional information (max 40) |
| advanceId | string | No | Related advance ID (max 128) |
| referenceId | string | No | Reference ID (max 20) |
| unitOfMeasure | string | No | Unit of measure (max 128) |
| auditUserSysId | string | No | Audit user system ID |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |
| mdfSystemStatus | string | No | System status |

#### Primary Keys
- `externalCode` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Transactional records with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /OneTimeDeduction | List all one-time deductions | $skip, $top |
| GET | /OneTimeDeduction({externalCode}) | Get by external code | N/A |

---

### RecurringDeduction
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/RecurringDeduction

#### Description
Recurring deduction configuration for employees.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| effectiveStartDate | DateTime | Yes | Effective start date |
| userSysId | string | Yes | User system ID (max 100) |
| effectiveEndDate | DateTime | No | Effective end date |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemEntityId | string | No | Entity ID |
| mdfSystemRecordStatus | string | No | Record status |

#### Primary Keys
- `effectiveStartDate` (DateTime)
- `userSysId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Effective-dated configuration with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /RecurringDeduction | List all recurring deductions | $skip, $top |
| GET | /RecurringDeduction(effectiveStartDate={date},userSysId='{id}') | Get by key | N/A |

---

### RecurringDeductionItem
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/RecurringDeductionItem

#### Description
Individual recurring deduction items under a recurring deduction.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| RecurringDeduction_effectiveStartDate | DateTime | Yes | Parent effective start date |
| RecurringDeduction_userSysId | string | Yes | Parent user system ID |
| payComponentType | string | Yes | Pay component type (max 32) |
| amount | decimal | No | Deduction amount |
| equivalentAmount | decimal | No | Equivalent amount |
| currency | string | No | Currency code (max 128) |
| frequency | string | No | Deduction frequency (max 32) |
| endDate | DateTime | No | End date |
| additionalInfo | string | No | Additional information (max 40) |
| advanceId | string | No | Related advance ID |
| referenceId | string | No | Reference ID (max 20) |
| unitOfMeasure | string | No | Unit of measure (max 128) |
| editPermission | string | No | Edit permission flag |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `RecurringDeduction_effectiveStartDate` (DateTime)
- `RecurringDeduction_userSysId` (string)
- `payComponentType` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Child records with modification tracking

---

### DeductionScreenId
**Source File**: ECCompensationInformation.json
**API Type**: OData v2
**Base Path**: /odata/v2/DeductionScreenId

#### Description
Screen configuration for deduction UI components.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| onetimeDeductionId | string | No | One-time deduction screen ID |
| onetimeDeductionUserGoAdminId | string | No | Admin screen ID |
| onetimeDeductionUserGoEmployeeEditId | string | No | Employee edit screen ID |
| onetimeDeductionUserGoEmployeeId | string | No | Employee screen ID |
| recurringDeductionId | string | No | Recurring deduction screen ID |
| dummyFieldValue | string | No | Placeholder field |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Configuration entity with modification tracking

---

## ECAdvances.json

### Advance
**Source File**: ECAdvances.json
**API Type**: OData v2
**Base Path**: /odata/v2/Advance

#### Description
Payroll advance requests from employees with approval workflow.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| NonRecurringPayment_externalCode | string | Yes | Parent non-recurring payment code (max 128) |
| externalCode | string | Yes | External code (max 128) |
| advanceType | string | No | Advance type code (max 32) |
| advanceEligibilityCode | string | No | Eligibility rule code (max 128) |
| approvalStatus | string | No | Workflow approval status |
| approver | string | No | Approver user ID (max 100) |
| currencyCode | string | No | Currency code |
| currencyGO | string | No | Generic object currency (max 128) |
| eligibileAmount | decimal | No | Eligible amount |
| eligibilityAmount | decimal | No | Eligibility amount |
| eligibleAdvanceType | string | No | Eligible advance type |
| requestedAmount | decimal | No | Requested amount |
| installmentAmount | decimal | No | Installment amount |
| installmentFrequency | string | No | Frequency of installments (max 32) |
| numberOfInstallments | int64 | No | Number of installments |
| interestRate | decimal | No | Interest rate |
| interestType | string | No | Interest type |
| paymentMode | string | No | Payment mode (max 128) |
| pendingAmount | decimal | No | Pending amount |
| recoveryMode | string | No | Recovery mode |
| recoveryStatus | string | No | Recovery status |
| remainingRequests | int64 | No | Remaining requests |
| requestDate | DateTime | No | Request date |
| totalRepaymentAmount | decimal | No | Total repayment amount |
| periodStartDate | DateTime | No | Period start date |
| periodEndDate | DateTime | No | Period end date |
| notesForApprover | string | No | Notes for approver |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |
| mdfSystemStatus | string | No | System status |

#### Primary Keys
- `NonRecurringPayment_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Transactional records with workflow and modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Advance | List all advances | $skip, $top |
| GET | /Advance(NonRecurringPayment_externalCode='{nrp}',externalCode='{id}') | Get by key | N/A |

---

### AdvancesInstallments
**Source File**: ECAdvances.json
**API Type**: OData v2
**Base Path**: /odata/v2/AdvancesInstallments

#### Description
Individual installment records for advance repayment.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Advance_externalCode | string | Yes | Parent advance code (max 128) |
| NonRecurringPayment_externalCode | string | Yes | Parent payment code (max 128) |
| externalCode | string | Yes | External code (max 128) |
| installmentAmount | decimal | No | Installment amount |
| interestAmount | decimal | No | Interest amount |
| amortization | decimal | No | Amortization amount |
| amortizationTotal | decimal | No | Total amortization |
| balanceRemaining | decimal | No | Remaining balance |
| currency | string | No | Currency code |
| currencyGO | string | No | Generic object currency |
| effectiveStatus | string | No | Effective status |
| installmentStatus | string | No | Installment status |
| paymentDate | DateTime | No | Payment date |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `Advance_externalCode` (string)
- `NonRecurringPayment_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Child transactional records with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /AdvancesInstallments | List all installments | $skip, $top |
| GET | /AdvancesInstallments(Advance_externalCode='{adv}',NonRecurringPayment_externalCode='{nrp}',externalCode='{id}') | Get by key | N/A |

---

### AdvancesEligibility
**Source File**: ECAdvances.json
**API Type**: OData v2
**Base Path**: /odata/v2/AdvancesEligibility

#### Description
Eligibility rules and configuration for advance requests.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| effectiveStartDate | DateTime | Yes | Effective start date |
| effectiveEndDate | DateTime | No | Effective end date |
| effectiveStatus | string | No | Effective status |
| advanceType | string | No | Advance type (max 32) |
| company | string | No | Company code (max 128) |
| department | string | No | Department code (max 128) |
| paygrade | string | No | Pay grade (max 32) |
| currency | string | No | Currency code (max 128) |
| currencyGO | string | No | Generic object currency |
| eligibilityAmount | decimal | No | Eligibility amount |
| maximumEligibilityAmount | decimal | No | Maximum eligibility |
| installmentAmount | decimal | No | Installment amount |
| installmentFrequency | string | No | Installment frequency |
| numberOfInstallments | int64 | No | Number of installments |
| numberOfOccurences | int64 | No | Number of occurrences |
| interestRate | decimal | No | Interest rate |
| interestType | string | No | Interest type |
| recoveryMode | string | No | Recovery mode |
| enableAutoRecovery | string | No | Auto recovery flag |
| defaultWorkflow | string | No | Default workflow (max 32) |
| exceptionWorkflow | string | No | Exception workflow |
| externalName | string | No | External name (max 128) |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `effectiveStartDate` (DateTime)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Effective-dated configuration with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /AdvancesEligibility | List all eligibility rules | $skip, $top |
| GET | /AdvancesEligibility(effectiveStartDate={date},externalCode='{id}') | Get by key | N/A |

---

### AdvancesAccumulation
**Source File**: ECAdvances.json
**API Type**: OData v2
**Base Path**: /odata/v2/AdvancesAccumulation

#### Description
Accumulated advance amounts and usage tracking per employee.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| userSysId | string | No | User system ID (max 100) |
| advanceType | string | No | Advance type (max 32) |
| accumulatedAmount | decimal | No | Total accumulated amount |
| remainingEligibleAmount | decimal | No | Remaining eligible amount |
| numberOfOccurances | int64 | No | Number of occurrences used |
| remainingNumberOfOccurances | int64 | No | Remaining occurrences |
| currency | string | No | Currency code |
| currencyGO | string | No | Generic object currency |
| periodStartDate | DateTime | No | Period start date |
| periodEndDate | DateTime | No | Period end date |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |
| mdfSystemRecordStatus | string | No | Record status |
| mdfSystemStatus | string | No | System status |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Running totals with modification tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /AdvancesAccumulation | List all accumulations | $skip, $top |
| GET | /AdvancesAccumulation('{externalCode}') | Get by external code | N/A |

---

## ECSkillsManagement.json

### SkillProfile
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/SkillProfile

#### Description
Employee skill profile containing rated and self-reported skills.

#### Primary Keys
- `externalCode` (string)
- `userId` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Profile data with modification tracking

---

### SkillEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/SkillEntity

#### Description
Master data for skills with localized names and descriptions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| name_defaultValue | string | No | Default name (max 256) |
| name_localized | string | No | Localized name |
| name_en_US | string | No | English US name |
| description_defaultValue | string | No | Default description (max 4000) |
| description_localized | string | No | Localized description |
| category | string | No | Skill category |
| status | string | No | Status |
| subModule | string | No | Sub-module |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Master data with modification tracking

---

### SkillContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/SkillContent

#### Description
Skill content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### CompetencyEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/CompetencyEntity

#### Description
Competency definitions with localized names.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| name_defaultValue | string | No | Default name |
| name_localized | string | No | Localized name |
| description_defaultValue | string | No | Default description |
| category | string | No | Competency category |
| status | string | No | Status |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### CompetencyContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/CompetencyContent

#### Description
Competency content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### CompetencyType
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/CompetencyType

#### Description
Competency type classification.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### CertificationEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/CertificationEntity

#### Description
Certification definitions with localized names and descriptions.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| certification_defaultValue | string | No | Default certification name (max 256) |
| certification_localized | string | No | Localized name |
| description_defaultValue | string | No | Default description (max 4000) |
| effectiveStartDate | DateTime | No | Effective start date |
| effectiveEndDate | DateTime | No | Effective end date |
| status | string | No | Status |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### CertificationContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/CertificationContent

#### Description
Certification content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobProfile
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobProfile

#### Description
Job profile definitions containing skills, competencies, and responsibilities.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| name_defaultValue | string | No | Default name |
| name_localized | string | No | Localized name |
| description_defaultValue | string | No | Default description |
| effectiveStartDate | DateTime | No | Effective start date |
| effectiveEndDate | DateTime | No | Effective end date |
| status | string | No | Status |
| subModule | string | No | Sub-module |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobProfileLocalizedData
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobProfileLocalizedData

#### Description
Localized data for job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobDescTemplate
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobDescTemplate

#### Description
Job description templates.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobDescSection
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobDescSection

#### Description
Sections within job description templates.

#### Primary Keys
- `JobDescTemplate_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### FamilyEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/FamilyEntity

#### Description
Job family definitions with localized names.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| name_defaultValue | string | No | Default name (max 128) |
| name_localized | string | No | Localized name |
| effectiveStartDate | DateTime | No | Effective start date |
| effectiveEndDate | DateTime | No | Effective end date |
| status | string | No | Status |
| createdLocale | string | No | Created locale |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### FamilySkillMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/FamilySkillMappingEntity

#### Description
Mapping of skills to job families.

#### Primary Keys
- `FamilyEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### FamilyCompetencyMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/FamilyCompetencyMappingEntity

#### Description
Mapping of competencies to job families.

#### Primary Keys
- `FamilyEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RoleEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RoleEntity

#### Description
Role definitions for skills management.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RoleSkillMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RoleSkillMappingEntity

#### Description
Mapping of skills to roles.

#### Primary Keys
- `RoleEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RoleCompetencyMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RoleCompetencyMappingEntity

#### Description
Mapping of competencies to roles.

#### Primary Keys
- `RoleEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RoleCompetencyBehaviorMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RoleCompetencyBehaviorMappingEntity

#### Description
Mapping of competency behaviors to roles.

#### Primary Keys
- `RoleEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RoleTalentPoolMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RoleTalentPoolMappingEntity

#### Description
Mapping of talent pools to roles.

#### Primary Keys
- `RoleEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### PositionEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/PositionEntity

#### Description
Position definitions for skills management.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### PositionSkillMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/PositionSkillMappingEntity

#### Description
Mapping of skills to positions.

#### Primary Keys
- `PositionEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### PositionCompetencyMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/PositionCompetencyMappingEntity

#### Description
Mapping of competencies to positions.

#### Primary Keys
- `PositionEntity_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobResponsibilityEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobResponsibilityEntity

#### Description
Job responsibility definitions with localized names.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | Yes | External code (max 128) |
| name_defaultValue | string | No | Default name (max 256) |
| name_localized | string | No | Localized name |
| duty_defaultValue | string | No | Duty description (max 4000) |
| category_defaultValue | string | No | Category (max 128) |
| description_defaultValue | string | No | Description (max 4000) |
| libName_defaultValue | string | No | Library name (max 128) |
| effectiveStartDate | DateTime | No | Effective start date |
| effectiveEndDate | DateTime | No | Effective end date |
| status | string | No | Status |
| createdBy | string | No | Creator |
| createdDateTime | DateTime | No | Creation timestamp |
| lastModifiedBy | string | No | Last modifier |
| lastModifiedDateTime | DateTime | No | Last modification timestamp |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobResponsibilityContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobResponsibilityContent

#### Description
Job responsibility content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### InterviewQuestionEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/InterviewQuestionEntity

#### Description
Interview question definitions.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### InterviewQuestionContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/InterviewQuestionContent

#### Description
Interview question content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### PhysicalReqEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/PhysicalReqEntity

#### Description
Physical requirement definitions.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### PhysicalReqContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/PhysicalReqContent

#### Description
Physical requirement content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### EmploymentConditionEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmploymentConditionEntity

#### Description
Employment condition definitions.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### EmploymentConditionContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmploymentConditionContent

#### Description
Employment condition content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RelevantIndustryEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RelevantIndustryEntity

#### Description
Relevant industry definitions.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RelevantIndustryContent
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RelevantIndustryContent

#### Description
Relevant industry content linked to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BehaviorMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/BehaviorMappingEntity

#### Description
Behavior mapping definitions.

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### RatedSkillMapping
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/RatedSkillMapping

#### Description
Mapping of rated skills to employees.

#### Primary Keys
- `SkillProfile_externalCode` (string)
- `SkillProfile_userId` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### SelfReportSkillMapping
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/SelfReportSkillMapping

#### Description
Mapping of self-reported skills to employees.

#### Primary Keys
- `SkillProfile_externalCode` (string)
- `SkillProfile_userId` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JobCodeMappingEntity
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JobCodeMappingEntity

#### Description
Mapping of job codes to job profiles.

#### Primary Keys
- `JobProfile_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### JDTemplateFamilyMapping
**Source File**: ECSkillsManagement.json
**API Type**: OData v2
**Base Path**: /odata/v2/JDTemplateFamilyMapping

#### Description
Mapping of job description templates to families.

#### Primary Keys
- `JobDescTemplate_externalCode` (string)
- `externalCode` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

## ECGlobalBenefits.json

### Benefit
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/Benefit

#### Description
Main benefit configuration entity.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitProgram
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitProgram

#### Description
Benefit program definitions.

#### Primary Keys
- `benefitProgramID` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitProgramEnrollment
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitProgramEnrollment

#### Description
Employee enrollments in benefit programs.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitProgramEnrollmentDetail
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitProgramEnrollmentDetail

#### Description
Details of benefit program enrollments.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitEnrollment
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitEnrollment

#### Description
Benefit enrollment records.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitEnrollmentGroup
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitEnrollmentGroup

#### Description
Benefit enrollment groups.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsurancePlan
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsurancePlan

#### Description
Insurance plan configurations.

#### Primary Keys
- `id` (int64)
- `effectiveStartDate` (DateTime)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsurancePlanUSA
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsurancePlanUSA

#### Description
USA-specific insurance plan configurations.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsurancePlanEnrollmentDetails
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsurancePlanEnrollmentDetails

#### Description
Insurance plan enrollment details.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsuranceCoverage
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsuranceCoverage

#### Description
Insurance coverage options.

#### Primary Keys
- `id` (int64)
- `effectiveStartDate` (DateTime)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsuranceCoverageDetails
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsuranceCoverageDetails

#### Description
Details of insurance coverage.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitInsuranceProvider
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitInsuranceProvider

#### Description
Insurance provider master data.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitSavingsPlanSubType
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitSavingsPlanSubType

#### Description
Savings plan sub-type definitions.

#### Primary Keys
- `benefitSavingsPlanID` (int64)
- `effectiveStartDate` (DateTime)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitPensionFund
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitPensionFund

#### Description
Pension fund configurations.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitCompanyCar
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitCompanyCar

#### Description
Company car benefit configurations.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitCompanyCarEnrollment
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitCompanyCarEnrollment

#### Description
Company car enrollments.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitCompanyHousing
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitCompanyHousing

#### Description
Company housing benefit configurations.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitCompanyHousingEnrollment
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitCompanyHousingEnrollment

#### Description
Company housing enrollments.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitEmployeeClaim
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitEmployeeClaim

#### Description
Employee benefit claims.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitEmployeeClaimDetail
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitEmployeeClaimDetail

#### Description
Details of employee benefit claims.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitDependentDetail
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitDependentDetail

#### Description
Benefit dependent information.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitEvent
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitEvent

#### Description
Benefit life events.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitLifeEventConfiguration
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitLifeEventConfiguration

#### Description
Life event configurations for benefits.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitDocuments
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitDocuments

#### Description
Benefit-related documents.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### BenefitLegalEntity
**Source File**: ECGlobalBenefits.json
**API Type**: OData v2
**Base Path**: /odata/v2/BenefitLegalEntity

#### Description
Legal entity configurations for benefits.

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime

---

### Additional ECGlobalBenefits Entities

The following entities follow similar patterns with `id` as primary key and `lastModifiedDateTime` for CDC:

- BenefitSchedules
- BenefitSchedulePeriod
- BenefitPaymentOptions
- BenefitBalanceCarryForward
- BenefitBalanceCarryForwardDetail
- BenefitClaimAccumulation
- BenefitContact
- BenefitExceptionDetails
- BenefitProgramExceptionDetails
- BenefitsException
- BenefitEffectiveDateConfiguration
- BenefitOpenEnrollmentCycleConfiguration
- BenefitsConfirmationStatementConfiguration
- BenefitInsuranceRateChart
- BenefitInsuranceRateChartFixedAmount
- BenefitInsuranceRateChartEnrollee
- BenefitInsuranceEnrolleeOptions
- BenefitInsuranceEnrolleeType
- BenefitInsuranceCoverageOptions
- BenefitInsuranceDependentDetail
- BenefitPensionDependentNominees
- BenefitPensionNonDependentNominees
- BenefitPensionEmployeeContributionDetail
- BenefitPensionEmployerContributionDetail
- BenefitPensionEnrollmentContributionDetail
- BenefitPensionFundEnrollmentContributionDetail
- BenefitSavingsPlanEnrollmentContributionDetail
- BenefitSavingsPlanSubTypeCountryLookup
- BenefitPensionStatutoryMinimumLookup
- BenefitFuelReimbursement
- BenefitFuelReimbursementClaimDetail
- BenefitLeaveTravelReimbursementClaim
- BenefitCompanyCarLeaseServiceProvider
- BenefitCompanyCarAllowedModels
- BenefitCompanyCarRecommendedVendors
- BenefitCompanyCarClaim
- BenefitsIntegrationOneTimeInfo
- BenefitsIntegrationRecurringInfo
- BenefitsConfigUIScreenLookup
- ACAReportingInformation
- ACAReportingDependentDetails
- InsuranceEnrollmentFieldsConfiguration
- InsuranceBenefitDetails
- SavingsAccountBenefitDetails
- SavingsAccountUSA
- SavingsAccountTierConfiguration
- SavingsAccountDeductionDetails
- IRSPremiumTable
- ImputedCostForAgeRanges
- BenefitPensionAdditionalEmployeeContributionDetail
- BenefitPensionAdditionalContributionLimits
- PensionBandingConfiguration
- PensionBandingConfigurationDetails
- BenefitPensionMinMaxContributionLimits
- LifeEventForBenefit
- BenefitEmployeeLifeEventDeclarationForm
- EmployeeWithEmployerMatchContributions
- EmployeeWithEmployerMatchContributionEntries
- BenefitDeductibleAllowanceEnrollment
- BenefitSavingsPlanTierConfiguration
- BenefitSavingsPlanERContributionConfig
- BenefitSavingsPlanERContributionConfigDetail
- BenefitSavingsPlanCatchUpDetail
- BenefitEnrollmentDependencyConfiguration
- BenefitEnrollmentDependencyDetails
- BenefitSavingsPlanPrimaryBeneficiary
- BenefitSavingsPlanContingentBeneficiary
- BenefitHyperlinkConfiguration
- BenefitOverviewHyperlinkConfiguration
- BenefitOverviewHyperlinkDetails
- BenefitEmployeeOptoutRequests
- BenefitEnrollmentOptoutDetails
- BenefitHSAEmployerContribution
- BenefitHSAEmployerContributionDetail
- BenefitHSAEmployerContributionTierDetail
- BenefitAutomaticActionConfiguration
- BenefitSavingsPlanEnrollmentDetails
- BenefitDeductionDetails

---

## sap-sf-EmpEmploymentHigherDuty-v1.json

### EmpEmploymentHigherDuty
**Source File**: sap-sf-EmpEmploymentHigherDuty-v1.json
**API Type**: OData v2
**Base Path**: /odata/v2/EmpEmploymentHigherDuty

#### Description
Higher duty employment assignments for public sector employees.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| personIdExternal | string | Yes | External person ID |
| userId | string | Yes | User ID |
| homeAssignment | string | Yes | Home assignment reference |
| startDate | DateTime | Yes | Start date of higher duty |
| plannedEndDate | DateTime | Yes | Planned end date |

#### Primary Keys
- `personIdExternal` (string)
- `userId` (string)
- `startDate` (DateTime)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field available; requires full refresh

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EmpEmploymentHigherDuty | Retrieve all higher duty records | $skip, $top |

---

## Pagination Reference

All OData v2 endpoints support standard pagination:
- `$top`: Limit number of records returned (default: 20)
- `$skip`: Skip first n records
- `$count`: Include total count in response
- `$filter`: Filter by property values
- `$orderby`: Order results by property
- `$select`: Select specific properties
- `$expand`: Expand related entities
- `$inlinecount=allpages`: Include total count inline

## Common MDF System Fields

Most entities include these standard MDF (Metadata Framework) fields:
- `mdfSystemRecordId`: Unique record identifier
- `mdfSystemRecordStatus`: Record status (e.g., active, deleted)
- `mdfSystemVersionId`: Version number for optimistic locking
- `mdfSystemTransactionSequence`: Transaction sequence number
- `mdfSystemObjectType`: Object type identifier
- `mdfSystemEntityId`: Entity identifier
- `mdfSystemEffectiveStartDate`: Effective start date
- `mdfSystemEffectiveEndDate`: Effective end date
- `mdfSystemCreatedBy`: Creator user ID
- `mdfSystemCreatedDate`: Creation date
- `mdfSystemLastModifiedBy`: Last modifier user ID
- `mdfSystemLastModifiedDate`: Last modification date
- `mdfSystemLastModifiedDateWithTZ`: Last modification with timezone

## Ingestion Type Summary

| Type | Count | Description |
|------|-------|-------------|
| cdc | 112 | Change Data Capture with lastModifiedDateTime cursor |
| snapshot | 6 | Full refresh required (calculated/derived data or no tracking) |
| append | 0 | N/A for this segment |
