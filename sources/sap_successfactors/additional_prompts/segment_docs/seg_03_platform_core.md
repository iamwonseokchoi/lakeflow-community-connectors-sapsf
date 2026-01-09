# SAP SuccessFactors API - Segment 3: Platform Services Core

## Overview
This segment covers platform foundation services, generic objects, user management, SSO, and role-based permissions in SAP SuccessFactors.

## Source Files
| File | API Title | Description |
|------|-----------|-------------|
| FoundationPlatformPLT.json | Common Platform APIs | Common APIs under SAP SuccessFactors platform |
| PLTGenericObjects.json | Generic Objects | APIs to access Generic Objects in the Metadata Framework |
| PLTUserManagement.json | User Management | API to access information about a system user |
| PLTSSO.json | Single Sign On (SSO) | API to get Service Provider (SP) metadata |
| PLTRoleBasedPermissions.json | Role Based Permissions | API for role based permission management |

---

## Entities

### FoundationPlatformPLT.json - Common Platform APIs

#### ExternalUser
- **Description**: Onboarding users external to the system
- **Primary Keys**: userId
- **Key Fields**: lastModifiedDateTime, is_deleted, personId, personGUID, status
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc_with_deletes (has is_deleted field and lastModifiedDateTime)
- **Navigation Properties**: extAddressInfo, extEmailInfo, extPersonalInfo, extPhoneInfo

#### PicklistOption
- **Description**: Legacy picklist options
- **Primary Keys**: id
- **Key Fields**: externalCode, optionValue, sortOrder, status
- **Cursor Field**: None
- **Ingestion Type**: snapshot (no lastModifiedDateTime)
- **Navigation Properties**: childPicklistOptions, parentPicklistOption, picklist, picklistLabels

#### Attachment
- **Description**: File attachments
- **Primary Keys**: attachmentId
- **Key Fields**: lastModifiedDateTime, createdDate, fileName, fileSize, mimeType, module, softDelete
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc_with_deletes (has softDelete field and lastModifiedDateTime)

#### PickListValueV2
- **Description**: MDF PickList values
- **Primary Keys**: PickListV2_effectiveStartDate, PickListV2_id, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, label_defaultValue, status
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc (has lastModifiedDateTime and mdfSystemRecordStatus)
- **Navigation Properties**: parentPickListValueNav

#### ExternalLearnerPersonalInfo
- **Description**: Personal info for learning users
- **Primary Keys**: itemId
- **Key Fields**: lastModifiedDateTime, is_deleted, firstName, lastName, dateOfBirth
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc_with_deletes (has is_deleted field)

#### PickListV2
- **Description**: MDF PickList
- **Primary Keys**: effectiveStartDate, id
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, name, status
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc (has lastModifiedDateTime)
- **Navigation Properties**: parentPickListNav, values

#### CompanyProvisioner
- **Description**: Company provisioner information
- **Primary Keys**: id
- **Key Fields**: name, email, status, createdAdminAccountNumber
- **Cursor Field**: None
- **Ingestion Type**: snapshot (no lastModifiedDateTime)

#### ExtAddressInfo
- **Description**: Address info for onboarding users
- **Primary Keys**: addressId
- **Key Fields**: lastModifiedDateTime, addressType, city, country, state, zipCode
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: addressTypeNav

#### CurrencyConversion
- **Description**: Currency conversion rates
- **Primary Keys**: code, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, baseCurrency, toCurrency, conversionRate
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: baseCurrencyNav, exchangeRateTypeNav, toCurrencyNav

#### InitiativeAlignmentBean
- **Description**: Initiative alignment for goals
- **Primary Keys**: externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, goalId, goalName, initiativeId, initiativeName
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### PicklistLabel
- **Description**: Legacy picklist labels
- **Primary Keys**: locale, optionId
- **Key Fields**: id, label
- **Cursor Field**: None
- **Ingestion Type**: snapshot (no lastModifiedDateTime)
- **Navigation Properties**: picklistOption

#### Country
- **Description**: Country master data
- **Primary Keys**: code, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, currency, externalName_defaultValue, twoCharCountryCode
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: currencyNav

#### Photo
- **Description**: User photos
- **Primary Keys**: photoId, userId, photoType
- **Key Fields**: lastModifiedDateTime, mimeType, height, width
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### WorkOrder
- **Description**: Work orders for contingent workers
- **Primary Keys**: userSysId, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, vendor, workOrderId, billingAmount
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: currencyNav, vendorNav, workerTypeNav

#### CompetencyRating
- **Description**: Competency ratings
- **Primary Keys**: id, guid
- **Key Fields**: lastModifiedDateTime, rating, userId, rater, raterCategory, module
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExtEmailInfo
- **Description**: Email info for onboarding users
- **Primary Keys**: emailInfoId
- **Key Fields**: lastModifiedDateTime (implied from related entities)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### VendorInfo
- **Description**: Vendor information
- **Primary Keys**: vendorCode, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, vendorName
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### Picklist
- **Description**: Legacy picklist
- **Primary Keys**: picklistId
- **Key Fields**: parentPicklist
- **Cursor Field**: None
- **Ingestion Type**: snapshot

#### ExtPersonalInfo
- **Description**: Personal info for onboarding users
- **Primary Keys**: personalInfoId
- **Key Fields**: lastModifiedDateTime (implied)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExternalLearnerEmailInfo
- **Description**: Email info for learning users
- **Primary Keys**: itemId
- **Key Fields**: lastModifiedDateTime (from parent)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExternalLearnerAddressInfo
- **Description**: Address info for learning users
- **Primary Keys**: itemId
- **Key Fields**: lastModifiedDateTime (from parent)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExternalLearnerPhoneInfo
- **Description**: Phone info for learning users
- **Primary Keys**: itemId
- **Key Fields**: lastModifiedDateTime (from parent)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### TimeZone
- **Description**: Time zone master data
- **Primary Keys**: externalCode, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExternalLearner
- **Description**: External learners
- **Primary Keys**: userId
- **Key Fields**: lastModifiedDateTime, is_deleted, status
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc_with_deletes

#### Currency
- **Description**: Currency master data
- **Primary Keys**: code, effectiveStartDate
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, externalName_defaultValue
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### TeamGoalOwner
- **Description**: Team goal owners
- **Primary Keys**: externalCode
- **Key Fields**: lastModifiedDateTime, userId
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

#### ExtPhoneInfo
- **Description**: Phone info for onboarding users
- **Primary Keys**: phoneInfoId
- **Key Fields**: lastModifiedDateTime (implied)
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc

---

### PLTGenericObjects.json - Generic Objects

#### cust_voluntarySeparationRequest
- **Description**: Voluntary separation requests
- **Primary Keys**: effectiveStartDate, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_reason, cust_lastday
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc (has mdfSystemRecordStatus for soft delete tracking)
- **Navigation Properties**: mdfSystemRecordStatusNav

#### cust_CommutingAllowance
- **Description**: Commuting allowance for employees
- **Primary Keys**: effectiveStartDate, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_Amount, cust_OriginStation, cust_DestinationStation
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav

#### cust_ProgressiveDisciplinaryAction
- **Description**: Progressive disciplinary actions
- **Primary Keys**: effectiveStartDate, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_Severity, cust_step, cust_dateofincident
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav, mdfSystemStatusNav

#### cust_RecruitInterviewJP
- **Description**: Recruit interview (Japan)
- **Primary Keys**: effectiveStartDate, externalCode, mdfSystemTransactionSequence
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_RCinterviewer
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav

#### MDFEnumValue
- **Description**: MDF enumeration values (lookup table)
- **Primary Keys**: key, value
- **Key Fields**: Locale-specific labels (de_DE, en_US, fr_FR, ja_JP, etc.)
- **Cursor Field**: None
- **Ingestion Type**: snapshot (reference data without lastModifiedDateTime)

#### cust_groupMedicalInsuranceIND
- **Description**: Group medical insurance (India)
- **Primary Keys**: BenefitEmployeeClaim_id, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_hospitalName, cust_patientName
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav

#### cust_grievances
- **Description**: Employee grievances
- **Primary Keys**: effectiveStartDate, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_grievanceStatus, cust_outcome
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav, mdfSystemStatusNav

#### cust_auth_sign
- **Description**: Authentication signatures
- **Primary Keys**: externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_signature, cust_asofdate
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav

#### MDFLocalizedValue
- **Description**: MDF localized values (lookup table)
- **Primary Keys**: locale
- **Key Fields**: value
- **Cursor Field**: None
- **Ingestion Type**: snapshot (reference data)

#### cust_groupInsuranceDetailsIND
- **Description**: Group insurance details (India)
- **Primary Keys**: BenefitEmployeeClaim_id, externalCode
- **Key Fields**: lastModifiedDateTime, mdfSystemRecordStatus, cust_sicknessDetails
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: mdfSystemRecordStatusNav

---

### PLTUserManagement.json - User Management

#### User
- **Description**: System user with personal and organizational information
- **Primary Keys**: userId
- **Key Fields**: lastModifiedDateTime, username, firstName, lastName, email, status, department, division, jobCode, hireDate, manager
- **Cursor Field**: lastModifiedDateTime
- **Ingestion Type**: cdc
- **Navigation Properties**: customManager, customReports, directReports, hr, hrReports, manager, matrixManager, matrixReports, proxy, secondManager, secondReports, userPermissionsNav

#### UserPermissions
- **Description**: User field-level permissions
- **Primary Keys**: userId
- **Key Fields**: All fields are permission flags (integer uint8 format)
- **Cursor Field**: None
- **Ingestion Type**: snapshot (permission metadata without timestamps)

---

### PLTSSO.json - Single Sign On

#### SPMetadataGenerator
- **Description**: Service Provider metadata generator for SSO configuration
- **Primary Keys**: None (function response type)
- **Key Fields**: errorMessage, result, status
- **Cursor Field**: None
- **Ingestion Type**: N/A (function import response, not a queryable entity)

---

### PLTRoleBasedPermissions.json - Role Based Permissions

#### DGExpression
- **Description**: Dynamic group expressions
- **Primary Keys**: expressionID
- **Key Fields**: expressionID
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: operator, values

#### DynamicGroup
- **Description**: Dynamic groups for permission targeting
- **Primary Keys**: groupID
- **Key Fields**: lastModifiedDate, groupName, groupType, staticGroup, userType, activeMembershipCount
- **Cursor Field**: lastModifiedDate
- **Ingestion Type**: cdc
- **Navigation Properties**: dgExcludePools, dgIncludePools

#### RBPRule
- **Description**: Role-based permission rules
- **Primary Keys**: ruleId
- **Key Fields**: status, accessUserType, targetUserType, relationRole
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: accessGroups, roles, targetGroups

#### DGField
- **Description**: Dynamic group fields
- **Primary Keys**: name
- **Key Fields**: dataType, label, picklistId
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: allowedOperators

#### DGFieldValue
- **Description**: Dynamic group field values
- **Primary Keys**: fieldValue
- **Key Fields**: fieldValue
- **Cursor Field**: None
- **Ingestion Type**: snapshot

#### DGFilter
- **Description**: Dynamic group filters
- **Primary Keys**: filterId
- **Key Fields**: filterId
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: expressions, field

#### RBPRole
- **Description**: Role-based permission roles
- **Primary Keys**: roleId
- **Key Fields**: lastModifiedDate, lastModifiedBy, roleName, roleDesc, userType
- **Cursor Field**: lastModifiedDate
- **Ingestion Type**: cdc
- **Navigation Properties**: permissions, rules

#### DGPeoplePool
- **Description**: Dynamic group people pools
- **Primary Keys**: peoplePoolId
- **Key Fields**: peoplePoolId
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: filters

#### RBPBasicPermission
- **Description**: Basic permissions
- **Primary Keys**: permissionId
- **Key Fields**: permissionType, permissionStringValue, permissionLongValue
- **Cursor Field**: None
- **Ingestion Type**: snapshot

#### DGFieldOperator
- **Description**: Dynamic group field operators
- **Primary Keys**: token
- **Key Fields**: label, token
- **Cursor Field**: None
- **Ingestion Type**: snapshot

#### DynamicGroupDefinition
- **Description**: Dynamic group definitions
- **Primary Keys**: groupID
- **Key Fields**: includedPeoplePool1, includedPeoplePool2, includedPeoplePool3, excludedPeoplePool1, excludedPeoplePool2, excludedPeoplePool3
- **Cursor Field**: None
- **Ingestion Type**: snapshot
- **Navigation Properties**: group

#### DynamicGroupBean
- **Description**: Dynamic group bean (function response)
- **Primary Keys**: groupId
- **Key Fields**: groupId, groupName
- **Cursor Field**: None
- **Ingestion Type**: N/A (function response type)

#### DynamicGroupUserBean
- **Description**: Dynamic group user bean (function response)
- **Primary Keys**: userId
- **Key Fields**: userId, userName, firstName, lastName, middleName
- **Cursor Field**: None
- **Ingestion Type**: N/A (function response type)

---

## API Endpoints

### FoundationPlatformPLT.json

| Entity | GET Collection | GET by Key | Key Pattern |
|--------|----------------|------------|-------------|
| ExternalUser | /ExternalUser | /ExternalUser('{userId}') | userId (string) |
| PicklistOption | /PicklistOption | /PicklistOption({id}) | id (int64) |
| Attachment | /Attachment | /Attachment({attachmentId}) | attachmentId (int64) |
| PickListValueV2 | /PickListValueV2 | /PickListValueV2(...) | Composite key |
| PickListV2 | /PickListV2 | /PickListV2(effectiveStartDate={date},id='{id}') | effectiveStartDate, id |
| Country | /Country | /Country(code='{code}',effectiveStartDate={date}) | code, effectiveStartDate |
| Currency | /Currency | /Currency(code='{code}',effectiveStartDate={date}) | code, effectiveStartDate |
| CurrencyConversion | /CurrencyConversion | /CurrencyConversion(code='{code}',effectiveStartDate={date}) | code, effectiveStartDate |
| Photo | /Photo | /Photo(photoId={id},userId='{userId}',photoType={type}) | photoId, userId, photoType |
| WorkOrder | /WorkOrder | /WorkOrder(userSysId='{id}',effectiveStartDate={date}) | userSysId, effectiveStartDate |
| CompetencyRating | /CompetencyRating | /CompetencyRating(id={id},guid='{guid}') | id, guid |
| TimeZone | /TimeZone | /TimeZone(externalCode='{code}',effectiveStartDate={date}) | externalCode, effectiveStartDate |
| VendorInfo | /VendorInfo | /VendorInfo(vendorCode='{code}',effectiveStartDate={date}) | vendorCode, effectiveStartDate |
| ExternalLearner | /ExternalLearner | /ExternalLearner('{userId}') | userId |
| Picklist | /Picklist | /Picklist('{picklistId}') | picklistId |
| PicklistLabel | /PicklistLabel | /PicklistLabel(locale='{locale}',optionId={id}) | locale, optionId |
| TeamGoalOwner | /TeamGoalOwner | /TeamGoalOwner('{externalCode}') | externalCode |
| CompanyProvisioner | /CompanyProvisioner | /CompanyProvisioner('{id}') | id |

### PLTGenericObjects.json

| Entity | GET Collection | GET by Key | Key Pattern |
|--------|----------------|------------|-------------|
| cust_voluntarySeparationRequest | /cust_voluntarySeparationRequest | /cust_voluntarySeparationRequest(effectiveStartDate={date},externalCode='{code}') | effectiveStartDate, externalCode |
| cust_CommutingAllowance | /cust_CommutingAllowance | /cust_CommutingAllowance(effectiveStartDate={date},externalCode='{code}') | effectiveStartDate, externalCode |
| cust_ProgressiveDisciplinaryAction | /cust_ProgressiveDisciplinaryAction | /cust_ProgressiveDisciplinaryAction(effectiveStartDate={date},externalCode='{code}') | effectiveStartDate, externalCode |
| cust_RecruitInterviewJP | /cust_RecruitInterviewJP | /cust_RecruitInterviewJP(effectiveStartDate={date},externalCode='{code}',mdfSystemTransactionSequence={seq}) | effectiveStartDate, externalCode, mdfSystemTransactionSequence |
| MDFEnumValue | /MDFEnumValue | /MDFEnumValue(key='{key}',value='{value}') | key, value |
| cust_groupMedicalInsuranceIND | /cust_groupMedicalInsuranceIND | /cust_groupMedicalInsuranceIND(BenefitEmployeeClaim_id={id},externalCode={code}) | BenefitEmployeeClaim_id, externalCode |
| cust_grievances | /cust_grievances | /cust_grievances(effectiveStartDate={date},externalCode='{code}') | effectiveStartDate, externalCode |
| cust_auth_sign | /cust_auth_sign | /cust_auth_sign('{externalCode}') | externalCode |
| MDFLocalizedValue | /MDFLocalizedValue | /MDFLocalizedValue('{locale}') | locale |
| cust_groupInsuranceDetailsIND | /cust_groupInsuranceDetailsIND | /cust_groupInsuranceDetailsIND(BenefitEmployeeClaim_id={id},externalCode='{code}') | BenefitEmployeeClaim_id, externalCode |

### PLTUserManagement.json

| Entity | GET Collection | GET by Key | Key Pattern |
|--------|----------------|------------|-------------|
| User | /User | /User('{userId}') | userId (string) |
| UserPermissions | /UserPermissions | /UserPermissions({userId}) | userId (integer) |

**Service Operations:**
- GET /getUserNameFormat - Get user name format by locale
- GET /getPasswordPolicy - Get password policy by locale

### PLTSSO.json

| Function | Endpoint | Parameters |
|----------|----------|------------|
| getSPMetadata | GET /getSPMetadata | dcDomain (required), companyId (required) |

### PLTRoleBasedPermissions.json

| Entity | GET Collection | GET by Key | Key Pattern |
|--------|----------------|------------|-------------|
| DGExpression | /DGExpression | /DGExpression('{expressionID}') | expressionID |
| DynamicGroup | /DynamicGroup | /DynamicGroup({groupID}) | groupID (int64) |
| RBPRule | /RBPRule | /RBPRule({ruleId}) | ruleId (int64) |
| DGField | /DGField | /DGField('{name}') | name |
| DGFieldValue | /DGFieldValue | /DGFieldValue('{fieldValue}') | fieldValue |
| DGFilter | /DGFilter | /DGFilter('{filterId}') | filterId |
| RBPRole | /RBPRole | /RBPRole({roleId}) | roleId (int64) |
| DGPeoplePool | /DGPeoplePool | /DGPeoplePool('{peoplePoolId}') | peoplePoolId |
| RBPBasicPermission | /RBPBasicPermission | /RBPBasicPermission({permissionId}) | permissionId (int64) |
| DGFieldOperator | /DGFieldOperator | /DGFieldOperator('{token}') | token |
| DynamicGroupDefinition | /DynamicGroupDefinition | /DynamicGroupDefinition({groupID}) | groupID (int64) |

**Service Operations:**
- GET /checkUserPermission - Check user permission
- GET /updateStaticGroup - Update static group
- GET /getDynamicGroupsByUser - Get dynamic groups by user
- GET /getUsersByDynamicGroup - Get users by dynamic group
- GET /getUserRolesReport - Get user roles report
- GET /getPermissionMetadata - Get permission metadata
- GET /getUsersPermissions - Get users permissions
- GET /getRolesPermissions - Get roles permissions
- GET /getExpandedDynamicGroupByName - Get expanded dynamic group by name
- GET /getExpandedDynamicGroupByNameAndSubType - Get expanded dynamic group by name and sub type
- GET /getExpandedDynamicGroupById - Get expanded dynamic group by ID
- GET /getUserRolesByUserId - Get user roles by user ID
- POST /checkUserPermissions - Check user permissions (action)

---

## Ingestion Type Summary

| Ingestion Type | Entities |
|----------------|----------|
| **cdc** | User, Country, Currency, CurrencyConversion, Photo, WorkOrder, CompetencyRating, TimeZone, VendorInfo, PickListV2, PickListValueV2, ExtAddressInfo, InitiativeAlignmentBean, TeamGoalOwner, DynamicGroup, RBPRole, cust_voluntarySeparationRequest, cust_CommutingAllowance, cust_ProgressiveDisciplinaryAction, cust_RecruitInterviewJP, cust_groupMedicalInsuranceIND, cust_grievances, cust_auth_sign, cust_groupInsuranceDetailsIND |
| **cdc_with_deletes** | ExternalUser, ExternalLearner, ExternalLearnerPersonalInfo, Attachment |
| **snapshot** | PicklistOption, PicklistLabel, Picklist, CompanyProvisioner, UserPermissions, MDFEnumValue, MDFLocalizedValue, DGExpression, RBPRule, DGField, DGFieldValue, DGFilter, DGPeoplePool, RBPBasicPermission, DGFieldOperator, DynamicGroupDefinition |

---

## Common MDF System Fields

Many entities in this segment use the MDF (Metadata Framework) system fields:

| Field | Description | Type |
|-------|-------------|------|
| mdfSystemRecordStatus | Record status (e.g., "C" for created, "U" for updated, "D" for deleted) | string |
| mdfSystemEffectiveEndDate | Effective end date for time-sliced records | DateTime |
| mdfSystemEffectiveStartDate | Effective start date for time-sliced records | DateTime |
| mdfSystemEntityId | Entity identifier | string |
| mdfSystemObjectType | Object type identifier | string |
| mdfSystemRecordId | Record identifier | string |
| mdfSystemTransactionSequence | Transaction sequence number | int64 |
| mdfSystemVersionId | Version identifier | int64 |
| mdfSystemCreatedBy | User who created the record | string |
| mdfSystemCreatedDate | Creation date | DateTime |
| mdfSystemLastModifiedBy | User who last modified the record | string |
| mdfSystemLastModifiedDate | Last modification date | DateTime |
| mdfSystemLastModifiedDateWithTZ | Last modification date with timezone | DateTime |

---

## Pagination

All collection endpoints support OData v2 pagination parameters:
- **$top**: Limit number of results (default: 20)
- **$skip**: Skip first n results
- **$count**: Include count of items (boolean)
- **$inlinecount=allpages**: Get total count with results
- **$filter**: Filter by property values
- **$orderby**: Order by property values
- **$select**: Select specific properties
- **$expand**: Expand navigation properties

---

## Notes

1. **Custom Objects (cust_*)**: These are example generic objects configured in the MDF framework. Actual available objects depend on customer configuration.

2. **Function Imports**: Service operations like getSPMetadata and various permission-related functions return single objects or collections, not paginated entity sets.

3. **Navigation Properties**: Many entities have navigation properties for related data. Use $expand to include related entities in a single request.

4. **Effective Dating**: Entities with effectiveStartDate support time-sliced data. Query with date filters to get point-in-time data.

5. **Soft Deletes**: Entities with is_deleted or mdfSystemRecordStatus fields use soft deletion. Filter appropriately for active records only.
