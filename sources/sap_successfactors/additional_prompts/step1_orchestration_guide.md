# SAP SuccessFactors API Documentation - Step 1 Orchestration Guide

## Overview

This guide orchestrates the documentation of 67 JSON API specifications (924 entities, 1,279 endpoints) across 3 API types (OData v2, OData v4, REST) into a single comprehensive API documentation file.

### Scope
| API Type | Files | Entities | Endpoints |
|----------|-------|----------|-----------|
| OData v2 | 41 | 759 | 1,198 |
| OData v4 | 6 | 0 | 31 |
| REST | 20 | 165 | 50 |
| **Total** | **67** | **924** | **1,279** |

### Output
- **Final**: `sources/sap_successfactors/sap_successfactors_api_doc.md`
- **Intermediate**: `sources/sap_successfactors/additional_prompts/segment_docs/seg_XX_*.md`

---

## Three-Phase Execution

### Phase 1: Parallel Segment Processing
Process 12 segments in parallel batches (4 agents per batch, 3 batches).

### Phase 2: Consolidation
Merge all segment docs into unified documentation with deduplication.

### Phase 3: Validation
Verify completeness, coverage, and template compliance.

---

## Segment Definitions

### Segment 1: Employee Central Core
**Output**: `seg_01_employee_central_core.md`
**Files** (from `api_spec_docs/odatav2/`):
- ECEmploymentInformation.json
- ECFoundationOrganization.json
- ECEmployeeCentralPayroll.json
- ECDismissalProtection.json
- EmpCostAssignment.json

**Focus**: Employment records, job information, organizational structure, payroll integration.

---

### Segment 2: Employee Central Extended
**Output**: `seg_02_employee_central_extended.md`
**Files** (from `api_spec_docs/odatav2/`):
- ECPaymentInformation.json
- ECCompensationInformation.json
- ECGlobalBenefits.json
- ECAdvances.json
- ECSkillsManagement.json
- sap-sf-EmpEmploymentHigherDuty-v1.json

**Focus**: Payment, compensation, benefits, skills management.

---

### Segment 3: Platform Services Core
**Output**: `seg_03_platform_core.md`
**Files** (from `api_spec_docs/odatav2/`):
- FoundationPlatformPLT.json
- PLTGenericObjects.json
- PLTUserManagement.json
- PLTSSO.json
- PLTRoleBasedPermissions.json

**Focus**: Platform foundation, generic objects, user management, SSO, permissions.

---

### Segment 4: Platform Services Extended
**Output**: `seg_04_platform_extended.md`
**Files** (from `api_spec_docs/odatav2/`):
- PLTTodo.json
- PLTSuccessStore.json
- PLTExecutionManager.json
- PLTUserInterfaceThemes.json
- PLTCustomNavigation.json

**Focus**: Todos, success store, execution management, UI themes, navigation.

---

### Segment 5: Recruitment Management
**Output**: `seg_05_recruitment.md`
**Files** (from `api_spec_docs/odatav2/`):
- RCMCandidate.json
- RCMJobApplication.json
- RCMJobRequisition.json
- RCMOffer.json
- RecruitingRCM.json

**Focus**: Candidates, job applications, requisitions, offers, recruiting workflows.

---

### Segment 6: Performance Management
**Output**: `seg_06_performance.md`
**Files**:
- odatav2/PerformanceandGoalsPMGM.json
- odatav2/PMFormsManagement.json
- odatav2/PMGMContinuousPerformanceManagement.json
- odatav2/PMGMMultirater.json
- odatav4/PMGMContinuousFeedback.json
- rest/PMGMContinuousPerformanceREST.json
- rest/PMGMPerformanceREST.json

**Focus**: Goals, performance forms, continuous feedback, multi-rater assessments.

---

### Segment 7: Time & Attendance
**Output**: `seg_07_time_attendance.md`
**Files**:
- odatav4/ClockInClockOutIntegration.json
- odatav4/ClockInClockOutExternal.json
- rest/ClockInClockOut.json
- rest/ClockInClockOutTimeEventsRestAPI.json
- rest/Balances.json
- rest/TimeOffEvents.json
- rest/AvailableTimeTypes.json

**Focus**: Clock events, time balances, time off, available time types.

---

### Segment 8: Succession & Development
**Output**: `seg_08_succession_dev.md`
**Files**:
- odatav2/SuccessionandDevelopmentSD.json
- odatav2/SDSuccessionManagement.json
- odatav2/SDCalibration.json
- odatav4/CalSession.json
- odatav4/SCMNominationService.json

**Focus**: Succession planning, calibration sessions, nominations.

---

### Segment 9: Onboarding
**Output**: `seg_09_onboarding.md`
**Files** (from `api_spec_docs/odatav2/`):
- OnboardingONB.json
- OnboardingOBX.json

**Focus**: Onboarding workflows, new hire processes.

---

### Segment 10: Finance & Operations
**Output**: `seg_10_finance_ops.md`
**Files** (from `api_spec_docs/odatav2/`):
- BudgetPeriodGO.json
- FunctionalAreaGO.json
- FundCenterGO.json
- sap-sf-FundGO-v1.json
- sap-sf-GrantGO-v1.json
- ProjectControllingObject.json

**Focus**: Budget periods, functional areas, fund centers, grants, project controlling.

---

### Segment 11: REST Extended APIs
**Output**: `seg_11_rest_extended.md`
**Files** (from `api_spec_docs/rest/`):
- sap-sf-customTasks-v2.json
- sap-sf-newhirejourney-v1.json
- sap-sf-FMLARequest-v1.json
- sap-sf-employeeCompensation-v1.json
- sap-sf-PLTRBPGenAI-v1.json
- sap-sf-PositionBudgetingControl-v1.json
- UserManagementSCIM.json
- i9audittrail.json

**Focus**: Custom tasks, new hire journey, FMLA, compensation, AI features, SCIM, audit trails.

---

### Segment 12: Remaining APIs (Misc)
**Output**: `seg_12_misc.md`
**Files**:
- rest/PLTScim.json
- rest/PLTDPCS.json
- rest/ExtensionPoint.json
- rest/InstructionalText.json
- rest/UploadAttachment.json
- odatav4/AdditionalServices.json

**Focus**: SCIM provisioning, data privacy, extensions, attachments, additional services.

---

## Agent Prompt Template

Use this template for each segment agent:

```markdown
## Task: Document SAP SuccessFactors API Segment {SEGMENT_NUMBER}

### Segment: {SEGMENT_NAME}
### Output File: sources/sap_successfactors/additional_prompts/segment_docs/{OUTPUT_FILENAME}

### Input Files
Read and process these JSON API specification files from `sources/sap_successfactors/api_spec_docs/`:
{FILE_LIST}

### Documentation Template
Follow the structure from `prompts/templates/source_api_doc_template.md`:

1. **Authorization** (segment-specific notes only, full auth in consolidated doc)
2. **Object List** - Extract all entities/objects from the JSON specs
3. **Object Schema** - Document all fields for each entity
4. **Get Object Primary Keys** - Identify key fields per entity
5. **Object's Ingestion Type** - Determine: cdc, cdc_with_deletes, snapshot, or append
6. **Read API for Data Retrieval** - Document all GET endpoints with pagination
7. **Field Type Mapping** - Map JSON types to Spark types

### Extraction Rules

**For OData v2 (Swagger 2.0)**:
- Entities: Extract from `definitions` section (skip odata.error types)
- Endpoints: Extract from `paths` section
- Primary Keys: Look for fields with "key" in description or typical patterns (userId, externalCode, etc.)
- Pagination: OData uses `$skip`, `$top`, `$count`
- Incremental: Look for `lastModifiedDateTime`, `createdDateTime` fields

**For OData v4 (OpenAPI 3.0)**:
- Entities: Extract from `components/schemas` section
- Endpoints: Extract from `paths` section
- Pagination: OData v4 uses `$skip`, `$top`, `@odata.nextLink`
- Incremental: Look for timestamp fields

**For REST (OpenAPI 3.0.3)**:
- Entities: Extract from `components/schemas` section
- Endpoints: Extract from `paths` section
- Pagination: Varies by API (check parameters)
- Incremental: Check for date/timestamp query parameters

### Output Format
```markdown
# SAP SuccessFactors API Documentation - {SEGMENT_NAME}

## Segment Overview
- **Segment**: {SEGMENT_NUMBER} - {SEGMENT_NAME}
- **Files Processed**: {FILE_COUNT}
- **Entities Documented**: {ENTITY_COUNT}
- **Endpoints Documented**: {ENDPOINT_COUNT}

## Objects

### {EntityName}
**Source File**: {filename.json}
**API Type**: OData v2 | OData v4 | REST
**Base Path**: /odata/v2/{entity} | /odatav4/{path} | /rest/{path}

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ... | ... | ... | ... |

#### Primary Keys
- `fieldName` (type)

#### Ingestion Type
- **Type**: cdc | snapshot | append
- **Cursor Field**: lastModifiedDateTime (if applicable)
- **Rationale**: {why this type was chosen}

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Entity | List all | $skip, $top |
| GET | /Entity('{id}') | Get by ID | N/A |

---

(Repeat for each entity)
```

### Completion Checklist
- [ ] All {FILE_COUNT} JSON files processed
- [ ] All entities documented with full schemas
- [ ] Primary keys identified for each entity
- [ ] Ingestion type determined for each entity
- [ ] All GET endpoints documented
- [ ] Pagination method noted per endpoint
```

---

## Execution Instructions

### Batch 1 (Segments 1-4) - Employee Central & Platform Core
Run these 4 agents in parallel:
```
Agent 1: Segment 1 - Employee Central Core (5 files)
Agent 2: Segment 2 - Employee Central Extended (6 files)
Agent 3: Segment 3 - Platform Services Core (5 files)
Agent 4: Segment 4 - Platform Services Extended (5 files)
```

### Batch 2 (Segments 5-8) - Talent Management
Run these 4 agents in parallel:
```
Agent 5: Segment 5 - Recruitment Management (5 files)
Agent 6: Segment 6 - Performance Management (7 files)
Agent 7: Segment 7 - Time & Attendance (7 files)
Agent 8: Segment 8 - Succession & Development (5 files)
```

### Batch 3 (Segments 9-12) - Specialized & Misc
Run these 4 agents in parallel:
```
Agent 9: Segment 9 - Onboarding (2 files)
Agent 10: Segment 10 - Finance & Operations (6 files)
Agent 11: Segment 11 - REST Extended APIs (8 files)
Agent 12: Segment 12 - Remaining APIs (6 files)
```

---

## Phase 2: Consolidation Template

After all segments complete, run consolidation:

```markdown
## Task: Consolidate SAP SuccessFactors API Documentation

### Input
Read all segment files from `sources/sap_successfactors/additional_prompts/segment_docs/`:
- seg_01_employee_central_core.md
- seg_02_employee_central_extended.md
- ... (all 12 files)

### Output
Write to: `sources/sap_successfactors/sap_successfactors_api_doc.md`

### Consolidation Rules

1. **Authorization Section** (write once at top)
   - Basic Auth: `{userId}@{companyId}` as username, API key as password
   - OAuth 2.0: SAML Bearer Assertion flow
   - All APIs use HTTPS, Accept: application/json

2. **Object List Section**
   - Create master index table with all entities
   - Group by business domain
   - Include source file reference

3. **Object Schema Section**
   - Merge all entity schemas
   - Group by domain
   - Add cross-references for related entities

4. **Primary Keys Section**
   - Consolidate all primary key mappings

5. **Ingestion Type Section**
   - Master table of all objects with their ingestion types
   - Summary statistics

6. **Read API Section**
   - Organize by API type (OData v2, v4, REST)
   - Common pagination patterns
   - Rate limit notes (if found in specs)

7. **Field Type Mapping**
   - Unified type mapping table
   - Special handling notes

8. **Sources and References**
   - List all 67 JSON files processed
   - SAP Help Portal links from externalDocs
   - Confidence: User-provided JSON specs - Highest

### Deduplication Rules
- Merge duplicate entities that appear in multiple specs
- Keep most complete schema definition
- Note source file for each entity
```

---

## Phase 3: Validation Checklist

```markdown
## Validation Task

### Coverage Verification
- [ ] All 67 JSON files listed in Sources section
- [ ] Entity count matches or exceeds 924
- [ ] Endpoint count matches or exceeds 1,279

### Template Compliance
- [ ] Authorization section complete
- [ ] Object List section has all entities
- [ ] Object Schema section has all fields
- [ ] Primary Keys identified for all entities
- [ ] Ingestion Type specified for all entities
- [ ] Read API documented for all endpoints
- [ ] Field Type Mapping complete
- [ ] Sources and References complete

### Quality Checks
- [ ] No TBD markers without rationale
- [ ] All links valid
- [ ] Consistent formatting
- [ ] No duplicate entities
```

---

## Common Patterns Reference

### SAP SuccessFactors URL Patterns
| API Type | Base URL Pattern |
|----------|------------------|
| OData v2 | `https://{api-server}/odata/v2/{Entity}` |
| OData v4 | `https://{api-server}/odatav4/{service}/{version}/{resource}` |
| REST | `https://{api-server}/rest/{module}/{version}/{resource}` |

### Common Query Parameters
| Parameter | OData v2 | OData v4 | REST |
|-----------|----------|----------|------|
| Pagination | `$skip`, `$top` | `$skip`, `$top` | Varies |
| Select | `$select` | `$select` | Varies |
| Filter | `$filter` | `$filter` | Varies |
| Order | `$orderby` | `$orderby` | Varies |
| Count | `$inlinecount=allpages` | `$count=true` | Varies |

### Typical Primary Key Patterns
- Employee entities: `userId`, `personIdExternal`
- Generic objects: `externalCode`
- Temporal entities: `effectiveStartDate` + `externalCode`
- Navigation: `{parentId}` + entity key

### Ingestion Type Determination
| Condition | Ingestion Type |
|-----------|----------------|
| Has `lastModifiedDateTime` + key fields | `cdc` |
| Has `lastModifiedDateTime` + soft delete field | `cdc_with_deletes` |
| No modification tracking | `snapshot` |
| Event/log tables (timestamps only) | `append` |

---

## File Count Verification

After Phase 1, verify all files processed:

| Segment | Expected Files | Actual Files | Status |
|---------|----------------|--------------|--------|
| 1 | 5 | _ | _ |
| 2 | 6 | _ | _ |
| 3 | 5 | _ | _ |
| 4 | 5 | _ | _ |
| 5 | 5 | _ | _ |
| 6 | 7 | _ | _ |
| 7 | 7 | _ | _ |
| 8 | 5 | _ | _ |
| 9 | 2 | _ | _ |
| 10 | 6 | _ | _ |
| 11 | 8 | _ | _ |
| 12 | 6 | _ | _ |
| **Total** | **67** | _ | _ |
