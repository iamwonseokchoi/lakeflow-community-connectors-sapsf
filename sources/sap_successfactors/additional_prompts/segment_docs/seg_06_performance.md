# SAP SuccessFactors API Documentation - Segment 6: Performance Management

## Overview

This document covers Performance Management APIs including goal management, performance reviews, continuous performance management, 360 reviews, and continuous feedback.

## API Sources

| API Name | Protocol | Base Path |
|----------|----------|-----------|
| PerformanceandGoalsPMGM | OData v2 | `/odata/v2` |
| PMFormsManagement | OData v2 | `/odata/v2` |
| PMGMMultirater | OData v2 | `/odata/v2` |
| PMGMContinuousPerformanceManagement | OData v2 | `/odata/v2` |
| PMGMContinuousFeedback | OData v4 | `/odatav4/talent/continuousfeedback/v1` |
| PMGMContinuousPerformanceREST | REST | `/rest/talent/continuousperformance/v1` |
| PMGMPerformanceREST | REST | `/rest/talent/performance/admin/v1` |

---

## Entity Reference

### 1. PerformanceandGoalsPMGM (OData v2)

#### Goal Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| Goal_1 | id | lastModified | cdc |
| Goal_2 | id | lastModified | cdc |
| Goal_3 | id | lastModified | cdc |
| Goal_4 | id | lastModified | cdc |
| Goal_5 | id | lastModified | cdc |
| Goal_6 | id | lastModified | cdc |
| Goal_7 | id | lastModified | cdc |
| Goal_8 | id | lastModified | cdc |
| Goal_101 | id | lastModified | cdc |
| TeamGoal_1 | id | lastModified | cdc |
| TeamGoal_5 | id | lastModified | cdc |
| TeamGoal_7 | id | lastModified | cdc |
| SimpleGoal | id | - | snapshot |

#### Goal Task Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalTask_1 | id | lastModified | cdc |
| GoalTask_2 | id | lastModified | cdc |
| GoalTask_3 | id | lastModified | cdc |
| GoalTask_4 | id | lastModified | cdc |
| GoalTask_5 | id | lastModified | cdc |
| GoalTask_6 | id | lastModified | cdc |
| GoalTask_7 | id | lastModified | cdc |
| GoalTask_8 | id | lastModified | cdc |
| GoalTask_101 | id | lastModified | cdc |

#### Goal Milestone Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalMilestone_1 | id | lastModified | cdc |
| GoalMilestone_2 | id | lastModified | cdc |
| GoalMilestone_3 | id | lastModified | cdc |
| GoalMilestone_4 | id | lastModified | cdc |
| GoalMilestone_5 | id | lastModified | cdc |
| GoalMilestone_7 | id | lastModified | cdc |

#### Goal Comment Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalComment_1 | id | lastModified | cdc |
| GoalComment_5 | id | lastModified | cdc |

#### Goal Permission Entities (Snapshot - No Modification Tracking)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalPermission_1 | id | - | snapshot |
| GoalPermission_2 | id | - | snapshot |
| GoalPermission_3 | id | - | snapshot |
| GoalPermission_4 | id | - | snapshot |
| GoalPermission_5 | id | - | snapshot |
| GoalPermission_6 | id | - | snapshot |
| GoalPermission_7 | id | - | snapshot |
| GoalPermission_8 | id | - | snapshot |
| GoalPermission_101 | id | - | snapshot |

#### Goal Task Permission Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalTaskPermission_1 | id | - | snapshot |
| GoalTaskPermission_2 | id | - | snapshot |
| GoalTaskPermission_3 | id | - | snapshot |
| GoalTaskPermission_4 | id | - | snapshot |
| GoalTaskPermission_5 | id | - | snapshot |
| GoalTaskPermission_6 | id | - | snapshot |
| GoalTaskPermission_7 | id | - | snapshot |
| GoalTaskPermission_8 | id | - | snapshot |
| GoalTaskPermission_101 | id | - | snapshot |

#### Goal Milestone Permission Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalMilestonePermission_1 | id | - | snapshot |
| GoalMilestonePermission_2 | id | - | snapshot |
| GoalMilestonePermission_3 | id | - | snapshot |
| GoalMilestonePermission_4 | id | - | snapshot |
| GoalMilestonePermission_5 | id | - | snapshot |
| GoalMilestonePermission_7 | id | - | snapshot |

#### Goal Metric & Target Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalMetricLookup_7 | id | lastModified | cdc |
| GoalTarget_7 | id | lastModified | cdc |
| GoalMetricLookupPermission_7 | id | - | snapshot |
| GoalTargetPermission_7 | id | - | snapshot |

#### Goal Plan Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalPlanTemplate | id | - | snapshot |
| GoalPlanState | planId, stateId, userId | lastModified | cdc |
| GoalWeight | planId, type, userId | - | snapshot |
| GoalEnum | planId, fieldId, value | - | snapshot |
| AssignTeamGoal | id | - | snapshot |

#### Development Goal Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| DevGoal_2001 | id | lastModified | cdc |
| DevGoal_2002 | id | lastModified | cdc |
| DevGoalPlanTemplate | id | - | snapshot |
| DevGoalCompetency | id | - | snapshot |
| DevGoalEnum | planId, fieldId, value | - | snapshot |
| DevGoalPermission_2001 | id | - | snapshot |
| DevGoalPermission_2002 | id | - | snapshot |
| DevGoalDetail | Activity_activityId, externalCode | lastModifiedDateTime | cdc_with_deletes |
| SimpleDevGoal | id | - | snapshot |

#### Form 360 Participant Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| Form360ParticipantConfig | formContentId, formDataId | - | snapshot |
| Form360ParticipantSection | formContentId, formDataId | - | snapshot |
| Form360ParticipantDetail | formContentId, formDataId, participantId | - | snapshot |
| Form360ParticipantCategory | formContentId, formDataId, categoryValue | - | snapshot |
| Form360ParticipantColumn | formContentId, formDataId, columnKey | - | snapshot |
| Form360Participant | formContentId, formDataId, participantId | - | snapshot |

#### Form Route Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormRouteMap | formDataId | - | snapshot |
| FormRouteStep | formDataId, stepOrder | - | snapshot |
| FormRouteSubStep | formDataId, stepOrder, subStepOrder | - | snapshot |

---

### 2. PMFormsManagement (OData v2)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormHeader | formDataId | formLastModifiedDate | cdc |
| FormFolder | folderId | - | snapshot |
| FormTemplate | formTemplateId | - | snapshot |
| FormCustomizedWeightedRatingSection | formContentId, formDataId | - | snapshot |
| FormPerfPotSummarySection | formContentId, formDataId | - | snapshot |

---

### 3. PMGMMultirater (OData v2)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| CORouteFormStatusBean | - (response type) | - | N/A (Service Operation Response) |

**Service Operations:**
- `complete360` - Complete a 360 review form

---

### 4. PMGMContinuousPerformanceManagement (OData v2)

#### Core CPM Entities (CDC with Deletes)

| Entity Name | Key Field(s) | Cursor Field | Delete Indicator | Ingestion Type |
|-------------|--------------|--------------|------------------|----------------|
| Achievement | achievementId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| Activity | activityId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| ActivityStatus | activityStatusId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| SupporterFeedback | feedbackId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| ActivityFeedback | Activity_activityId, activityFeedbackId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| GoalDetail | Activity_activityId, externalCode | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| AchievementGoalDetail | Achievement_achievementId, externalCode | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| AchievementDevGoalDetail | Achievement_achievementId, externalCode | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |
| FeedbackFlag | feedbackFlagId | lastModifiedDateTime | mdfSystemRecordStatus | cdc_with_deletes |

#### Permission Entity

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| ContinuousPerformanceUserPermission | targetUserId | - | snapshot |

#### Goal Achievement Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| GoalAchievements | goalId, subjectUserId | - | snapshot |
| GoalAchievementsList | achievementId, goalId, subjectUserId | - | snapshot |
| DevGoalAchievements | goalId, subjectUserId | - | snapshot |
| DevGoalAchievementsList | achievementId, goalId, subjectUserId | - | snapshot |

#### Form Content Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormContent | formContentId, formDataId | lastModifiedDate | cdc |
| FormPMReviewContentDetail | formContentId, formDataId | - | snapshot |
| Form360ReviewContentDetail | formContentId, formDataId | - | snapshot |
| FormIntroductionSection | formContentId, formDataId | - | snapshot |
| FormUserInformationSection | formContentId, formDataId | - | snapshot |
| FormSummarySection | formContentId, formDataId | - | snapshot |
| FormObjCompSummarySection | formContentId, formDataId | - | snapshot |

#### Form Signature Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormSignatureSection | formContentId, formDataId, sectionIndex | - | snapshot |
| FormSignature | formContentId, formDataId, sectionIndex, signatureStepId | - | snapshot |

#### Form 360 Rater Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| Form360Rater | formContentId, formDataId | - | snapshot |
| Form360RaterSection | formContentId, formDataId | - | snapshot |
| FormRaterListSection | formContentId, formDataId | - | snapshot |

#### Form Objective Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormObjectiveSection | formContentId, formDataId, sectionIndex | - | snapshot |
| FormObjective | formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormObjectiveComment | formContentId, formDataId, itemId, sectionIndex, userId | - | snapshot |
| FormObjectiveDetails | formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormObjectiveOtherDetails | formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormObjectiveOtherDetailsItem | formContentId, formDataId, itemId, rowIndex, sectionIndex | - | snapshot |
| FormObjectiveOtherDetailsItemCol | formContentId, formDataId, itemId, sectionIndex, type | - | snapshot |
| FormObjectiveOtherDetailsItemValueCell | formContentId, formDataId, itemId, rowIndex, sectionIndex, type | - | snapshot |

#### Form Competency Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormCompetencySection | formContentId, formDataId, sectionIndex | - | snapshot |
| FormCompetency | formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormCompetencyBehavior | behaviorId, formContentId, formDataId, itemId, sectionIndex | - | snapshot |

#### Form Rating & Comment Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormUserRatingComment | formContentId, formDataId, itemId, ratingType, sectionIndex, userId | - | snapshot |
| FormBehaviorRatingComment | behaviorId, formContentId, formDataId, itemId, ratingType, sectionIndex, userId | - | snapshot |
| FormRatingScale | formContentId, formDataId, scaleId, sectionIndex | - | snapshot |
| FormRatingScaleValue | formContentId, formDataId, scaleId, sectionIndex, value | - | snapshot |

#### Form Custom Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormCustomSection | formContentId, formDataId, sectionIndex | - | snapshot |
| FormCustomElement | elementKey, formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormCustomElementListValue | elementKey, formContentId, formDataId, itemId, sectionIndex, value | - | snapshot |

#### Form Configuration & Audit Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormSectionConfiguration | formContentId, formDataId, sectionIndex | - | snapshot |
| FormItemConfiguration | formContentId, formDataId, itemId, sectionIndex | - | snapshot |
| FormAuditTrail | auditTrailId, formContentId, formDataId | - | snapshot |

#### Form Feedback Entities

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FormReviewFeedbackList | formDataId | - | snapshot |
| FormReviewFeedback | feedbackId, formDataId | - | snapshot |

---

### 5. PMGMContinuousFeedback (OData v4)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| FeedbackRequests | recordId | lastModifiedAt | cdc |
| Feedback | recordId | lastModifiedAt | cdc |
| Recipient | recordId | - | snapshot |
| UserCapabilities | targetUserAssignmentUUID | - | snapshot |

---

### 6. PMGMContinuousPerformanceREST (REST API)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| activityStatus | activityStatusRecordId | lastModifiedDateTime | cdc |
| activities | activityRecordId | lastModifiedDate | cdc |
| activityUpdates | activityUpdateRecordId | lastModifiedDate | cdc |
| achievements | achievementRecordId | lastModifiedDate | cdc |
| userPermissions | targetUserAssignmentUUID | - | snapshot |

---

### 7. PMGMPerformanceREST (REST API)

| Entity Name | Key Field(s) | Cursor Field | Ingestion Type |
|-------------|--------------|--------------|----------------|
| reviewRouteMap | reviewId (path param) | - | snapshot |
| reviewRouteStep | stepId | - | snapshot |
| reviewRouteSubStep | - (nested) | - | snapshot |

---

## GET Endpoints Reference

### PerformanceandGoalsPMGM (OData v2)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/Goal_1` | GET | $skip, $top, $count |
| `/Goal_1({id})` | GET | - |
| `/Goal_2` | GET | $skip, $top, $count |
| `/Goal_2({id})` | GET | - |
| `/Goal_3` | GET | $skip, $top, $count |
| `/Goal_3({id})` | GET | - |
| `/Goal_4` | GET | $skip, $top, $count |
| `/Goal_4({id})` | GET | - |
| `/Goal_5` | GET | $skip, $top, $count |
| `/Goal_5({id})` | GET | - |
| `/Goal_6` | GET | $skip, $top, $count |
| `/Goal_6({id})` | GET | - |
| `/Goal_7` | GET | $skip, $top, $count |
| `/Goal_7({id})` | GET | - |
| `/Goal_8` | GET | $skip, $top, $count |
| `/Goal_8({id})` | GET | - |
| `/Goal_101` | GET | $skip, $top, $count |
| `/Goal_101({id})` | GET | - |
| `/TeamGoal_1` | GET | $skip, $top, $count |
| `/TeamGoal_1({id})` | GET | - |
| `/TeamGoal_5` | GET | $skip, $top, $count |
| `/TeamGoal_5({id})` | GET | - |
| `/TeamGoal_7` | GET | $skip, $top, $count |
| `/TeamGoal_7({id})` | GET | - |
| `/GoalTask_1` | GET | $skip, $top, $count |
| `/GoalTask_1({id})` | GET | - |
| `/GoalTask_2` | GET | $skip, $top, $count |
| `/GoalTask_2({id})` | GET | - |
| `/GoalTask_3` | GET | $skip, $top, $count |
| `/GoalTask_3({id})` | GET | - |
| `/GoalTask_4` | GET | $skip, $top, $count |
| `/GoalTask_4({id})` | GET | - |
| `/GoalTask_5` | GET | $skip, $top, $count |
| `/GoalTask_5({id})` | GET | - |
| `/GoalTask_6` | GET | $skip, $top, $count |
| `/GoalTask_6({id})` | GET | - |
| `/GoalTask_7` | GET | $skip, $top, $count |
| `/GoalTask_7({id})` | GET | - |
| `/GoalTask_8` | GET | $skip, $top, $count |
| `/GoalTask_8({id})` | GET | - |
| `/GoalTask_101` | GET | $skip, $top, $count |
| `/GoalTask_101({id})` | GET | - |
| `/GoalMilestone_1` | GET | $skip, $top, $count |
| `/GoalMilestone_1({id})` | GET | - |
| `/GoalMilestone_2` | GET | $skip, $top, $count |
| `/GoalMilestone_2({id})` | GET | - |
| `/GoalMilestone_3` | GET | $skip, $top, $count |
| `/GoalMilestone_3({id})` | GET | - |
| `/GoalMilestone_4` | GET | $skip, $top, $count |
| `/GoalMilestone_4({id})` | GET | - |
| `/GoalMilestone_5` | GET | $skip, $top, $count |
| `/GoalMilestone_5({id})` | GET | - |
| `/GoalMilestone_7` | GET | $skip, $top, $count |
| `/GoalMilestone_7({id})` | GET | - |
| `/GoalComment_1` | GET | $skip, $top, $count |
| `/GoalComment_1({id})` | GET | - |
| `/GoalComment_5` | GET | $skip, $top, $count |
| `/GoalComment_5({id})` | GET | - |
| `/GoalPermission_1` | GET | $skip, $top, $count |
| `/GoalPermission_1({id})` | GET | - |
| `/GoalPermission_2` | GET | $skip, $top, $count |
| `/GoalPermission_2({id})` | GET | - |
| `/GoalPermission_3` | GET | $skip, $top, $count |
| `/GoalPermission_3({id})` | GET | - |
| `/GoalPermission_4` | GET | $skip, $top, $count |
| `/GoalPermission_4({id})` | GET | - |
| `/GoalPermission_5` | GET | $skip, $top, $count |
| `/GoalPermission_5({id})` | GET | - |
| `/GoalPermission_6` | GET | $skip, $top, $count |
| `/GoalPermission_6({id})` | GET | - |
| `/GoalPermission_7` | GET | $skip, $top, $count |
| `/GoalPermission_7({id})` | GET | - |
| `/GoalPermission_8` | GET | $skip, $top, $count |
| `/GoalPermission_8({id})` | GET | - |
| `/GoalPermission_101` | GET | $skip, $top, $count |
| `/GoalPermission_101({id})` | GET | - |
| `/GoalTaskPermission_1` | GET | $skip, $top, $count |
| `/GoalTaskPermission_1({id})` | GET | - |
| `/GoalTaskPermission_2` | GET | $skip, $top, $count |
| `/GoalTaskPermission_2({id})` | GET | - |
| `/GoalTaskPermission_3` | GET | $skip, $top, $count |
| `/GoalTaskPermission_3({id})` | GET | - |
| `/GoalTaskPermission_4` | GET | $skip, $top, $count |
| `/GoalTaskPermission_4({id})` | GET | - |
| `/GoalTaskPermission_5` | GET | $skip, $top, $count |
| `/GoalTaskPermission_5({id})` | GET | - |
| `/GoalTaskPermission_6` | GET | $skip, $top, $count |
| `/GoalTaskPermission_6({id})` | GET | - |
| `/GoalTaskPermission_7` | GET | $skip, $top, $count |
| `/GoalTaskPermission_7({id})` | GET | - |
| `/GoalTaskPermission_8` | GET | $skip, $top, $count |
| `/GoalTaskPermission_8({id})` | GET | - |
| `/GoalTaskPermission_101` | GET | $skip, $top, $count |
| `/GoalTaskPermission_101({id})` | GET | - |
| `/GoalMilestonePermission_1` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_1({id})` | GET | - |
| `/GoalMilestonePermission_2` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_2({id})` | GET | - |
| `/GoalMilestonePermission_3` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_3({id})` | GET | - |
| `/GoalMilestonePermission_4` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_4({id})` | GET | - |
| `/GoalMilestonePermission_5` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_5({id})` | GET | - |
| `/GoalMilestonePermission_7` | GET | $skip, $top, $count |
| `/GoalMilestonePermission_7({id})` | GET | - |
| `/GoalMetricLookup_7` | GET | $skip, $top, $count |
| `/GoalMetricLookup_7({id})` | GET | - |
| `/GoalMetricLookupPermission_7` | GET | $skip, $top, $count |
| `/GoalMetricLookupPermission_7({id})` | GET | - |
| `/GoalTarget_7` | GET | $skip, $top, $count |
| `/GoalTarget_7({id})` | GET | - |
| `/GoalTargetPermission_7` | GET | $skip, $top, $count |
| `/GoalTargetPermission_7({id})` | GET | - |
| `/GoalPlanTemplate` | GET | $skip, $top, $count |
| `/GoalPlanTemplate({id})` | GET | - |
| `/GoalPlanState` | GET | $skip, $top, $count |
| `/GoalPlanState(planId={planId},stateId={stateId},userId='{userId}')` | GET | - |
| `/GoalWeight` | GET | $skip, $top, $count |
| `/GoalWeight(planId={planId},type='{type}',userId='{userId}')` | GET | - |
| `/GoalEnum` | GET | $skip, $top, $count |
| `/GoalEnum(planId={planId},fieldId='{fieldId}',value='{value}')` | GET | - |
| `/SimpleGoal` | GET | $skip, $top, $count |
| `/SimpleGoal({id})` | GET | - |
| `/AssignTeamGoal` | GET | $skip, $top, $count |
| `/AssignTeamGoal({id})` | GET | - |
| `/DevGoal_2001` | GET | $skip, $top, $count |
| `/DevGoal_2001({id})` | GET | - |
| `/DevGoal_2002` | GET | $skip, $top, $count |
| `/DevGoal_2002({id})` | GET | - |
| `/DevGoalPlanTemplate` | GET | $skip, $top, $count |
| `/DevGoalPlanTemplate({id})` | GET | - |
| `/DevGoalCompetency` | GET | $skip, $top, $count |
| `/DevGoalCompetency({id})` | GET | - |
| `/DevGoalEnum` | GET | $skip, $top, $count |
| `/DevGoalEnum(planId={planId},fieldId='{fieldId}',value='{value}')` | GET | - |
| `/DevGoalPermission_2001` | GET | $skip, $top, $count |
| `/DevGoalPermission_2001({id})` | GET | - |
| `/DevGoalPermission_2002` | GET | $skip, $top, $count |
| `/DevGoalPermission_2002({id})` | GET | - |
| `/DevGoalDetail` | GET | $skip, $top, $count |
| `/DevGoalDetail(Activity_activityId={Activity_activityId},externalCode={externalCode})` | GET | - |
| `/SimpleDevGoal` | GET | $skip, $top, $count |
| `/SimpleDevGoal({id})` | GET | - |
| `/Form360ParticipantConfig` | GET | $skip, $top, $count |
| `/Form360ParticipantConfig(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/Form360ParticipantSection` | GET | $skip, $top, $count |
| `/Form360ParticipantSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/Form360ParticipantDetail` | GET | $skip, $top, $count |
| `/Form360ParticipantDetail(formContentId={formContentId},formDataId={formDataId},participantId='{participantId}')` | GET | - |
| `/Form360ParticipantCategory` | GET | $skip, $top, $count |
| `/Form360ParticipantCategory(formContentId={formContentId},formDataId={formDataId},categoryValue='{categoryValue}')` | GET | - |
| `/Form360ParticipantColumn` | GET | $skip, $top, $count |
| `/Form360ParticipantColumn(formContentId={formContentId},formDataId={formDataId},columnKey='{columnKey}')` | GET | - |
| `/Form360Participant` | GET | $skip, $top, $count |
| `/Form360Participant(formContentId={formContentId},formDataId={formDataId},participantId='{participantId}')` | GET | - |
| `/FormRouteMap` | GET | $skip, $top, $count |
| `/FormRouteMap({formDataId})` | GET | - |
| `/FormRouteStep` | GET | $skip, $top, $count |
| `/FormRouteStep(formDataId={formDataId},stepOrder={stepOrder})` | GET | - |
| `/FormRouteSubStep` | GET | $skip, $top, $count |
| `/FormRouteSubStep(formDataId={formDataId},stepOrder={stepOrder},subStepOrder={subStepOrder})` | GET | - |

### PMFormsManagement (OData v2)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/FormHeader` | GET | $skip, $top, $count |
| `/FormHeader({formDataId})` | GET | - |
| `/FormFolder` | GET | $skip, $top, $count |
| `/FormFolder({folderId})` | GET | - |
| `/FormTemplate` | GET | $skip, $top, $count |
| `/FormTemplate({formTemplateId})` | GET | - |
| `/FormCustomizedWeightedRatingSection` | GET | $skip, $top, $count |
| `/FormCustomizedWeightedRatingSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormPerfPotSummarySection` | GET | $skip, $top, $count |
| `/FormPerfPotSummarySection(formContentId={formContentId},formDataId={formDataId})` | GET | - |

### PMGMMultirater (OData v2)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/complete360` | GET (Function Import) | - |

### PMGMContinuousPerformanceManagement (OData v2)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/Achievement` | GET | $skip, $top, $count |
| `/Achievement({achievementId})` | GET | - |
| `/Activity` | GET | $skip, $top, $count |
| `/Activity({activityId})` | GET | - |
| `/ActivityStatus` | GET | $skip, $top, $count |
| `/ActivityStatus({activityStatusId})` | GET | - |
| `/SupporterFeedback` | GET | $skip, $top, $count |
| `/SupporterFeedback({feedbackId})` | GET | - |
| `/ActivityFeedback` | GET | $skip, $top, $count |
| `/ActivityFeedback(Activity_activityId={Activity_activityId},activityFeedbackId={activityFeedbackId})` | GET | - |
| `/GoalDetail` | GET | $skip, $top, $count |
| `/GoalDetail(Activity_activityId={Activity_activityId},externalCode={externalCode})` | GET | - |
| `/AchievementGoalDetail` | GET | $skip, $top, $count |
| `/AchievementGoalDetail(Achievement_achievementId={Achievement_achievementId},externalCode={externalCode})` | GET | - |
| `/AchievementDevGoalDetail` | GET | $skip, $top, $count |
| `/AchievementDevGoalDetail(Achievement_achievementId={Achievement_achievementId},externalCode={externalCode})` | GET | - |
| `/FeedbackFlag` | GET | $skip, $top, $count |
| `/FeedbackFlag('{feedbackFlagId}')` | GET | - |
| `/ContinuousPerformanceUserPermission` | GET | $skip, $top, $count |
| `/ContinuousPerformanceUserPermission('{targetUserId}')` | GET | - |
| `/GoalAchievements` | GET | $skip, $top, $count |
| `/GoalAchievements(goalId='{goalId}',subjectUserId='{subjectUserId}')` | GET | - |
| `/GoalAchievementsList` | GET | $skip, $top, $count |
| `/GoalAchievementsList(achievementId={achievementId},goalId='{goalId}',subjectUserId='{subjectUserId}')` | GET | - |
| `/DevGoalAchievements` | GET | $skip, $top, $count |
| `/DevGoalAchievements(goalId='{goalId}',subjectUserId='{subjectUserId}')` | GET | - |
| `/DevGoalAchievementsList` | GET | $skip, $top, $count |
| `/DevGoalAchievementsList(achievementId={achievementId},goalId='{goalId}',subjectUserId='{subjectUserId}')` | GET | - |
| `/FormContent` | GET | $skip, $top, $count |
| `/FormContent(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormPMReviewContentDetail` | GET | $skip, $top, $count |
| `/FormPMReviewContentDetail(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/Form360ReviewContentDetail` | GET | $skip, $top, $count |
| `/Form360ReviewContentDetail(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormSignatureSection` | GET | $skip, $top, $count |
| `/FormSignatureSection(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex})` | GET | - |
| `/FormSignature` | GET | $skip, $top, $count |
| `/FormSignature(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex},signatureStepId={signatureStepId})` | GET | - |
| `/Form360Rater` | GET | $skip, $top, $count |
| `/Form360Rater(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/Form360RaterSection` | GET | $skip, $top, $count |
| `/Form360RaterSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormRaterListSection` | GET | $skip, $top, $count |
| `/FormRaterListSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormObjectiveSection` | GET | $skip, $top, $count |
| `/FormObjectiveSection(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex})` | GET | - |
| `/FormObjective` | GET | $skip, $top, $count |
| `/FormObjective(formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex})` | GET | - |
| `/FormCompetencySection` | GET | $skip, $top, $count |
| `/FormCompetencySection(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex})` | GET | - |
| `/FormCompetency` | GET | $skip, $top, $count |
| `/FormCompetency(formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex})` | GET | - |
| `/FormCompetencyBehavior` | GET | $skip, $top, $count |
| `/FormCompetencyBehavior(behaviorId={behaviorId},formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex})` | GET | - |
| `/FormUserRatingComment` | GET | $skip, $top, $count |
| `/FormUserRatingComment(formContentId={formContentId},formDataId={formDataId},itemId={itemId},ratingType='{ratingType}',sectionIndex={sectionIndex},userId='{userId}')` | GET | - |
| `/FormBehaviorRatingComment` | GET | $skip, $top, $count |
| `/FormBehaviorRatingComment(behaviorId={behaviorId},formContentId={formContentId},formDataId={formDataId},itemId={itemId},ratingType='{ratingType}',sectionIndex={sectionIndex},userId='{userId}')` | GET | - |
| `/FormRatingScale` | GET | $skip, $top, $count |
| `/FormRatingScale(formContentId={formContentId},formDataId={formDataId},scaleId='{scaleId}',sectionIndex={sectionIndex})` | GET | - |
| `/FormRatingScaleValue` | GET | $skip, $top, $count |
| `/FormRatingScaleValue(formContentId={formContentId},formDataId={formDataId},scaleId='{scaleId}',sectionIndex={sectionIndex},value='{value}')` | GET | - |
| `/FormCustomSection` | GET | $skip, $top, $count |
| `/FormCustomSection(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex})` | GET | - |
| `/FormCustomElement` | GET | $skip, $top, $count |
| `/FormCustomElement(elementKey='{elementKey}',formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex})` | GET | - |
| `/FormCustomElementListValue` | GET | $skip, $top, $count |
| `/FormCustomElementListValue(elementKey='{elementKey}',formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex},value='{value}')` | GET | - |
| `/FormSectionConfiguration` | GET | $skip, $top, $count |
| `/FormSectionConfiguration(formContentId={formContentId},formDataId={formDataId},sectionIndex={sectionIndex})` | GET | - |
| `/FormItemConfiguration` | GET | $skip, $top, $count |
| `/FormItemConfiguration(formContentId={formContentId},formDataId={formDataId},itemId={itemId},sectionIndex={sectionIndex})` | GET | - |
| `/FormAuditTrail` | GET | $skip, $top, $count |
| `/FormAuditTrail(auditTrailId={auditTrailId},formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormReviewFeedbackList` | GET | $skip, $top, $count |
| `/FormReviewFeedbackList({formDataId})` | GET | - |
| `/FormReviewFeedback` | GET | $skip, $top, $count |
| `/FormReviewFeedback(feedbackId={feedbackId},formDataId={formDataId})` | GET | - |
| `/FormIntroductionSection` | GET | $skip, $top, $count |
| `/FormIntroductionSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormUserInformationSection` | GET | $skip, $top, $count |
| `/FormUserInformationSection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormSummarySection` | GET | $skip, $top, $count |
| `/FormSummarySection(formContentId={formContentId},formDataId={formDataId})` | GET | - |
| `/FormObjCompSummarySection` | GET | $skip, $top, $count |
| `/FormObjCompSummarySection(formContentId={formContentId},formDataId={formDataId})` | GET | - |

### PMGMContinuousFeedback (OData v4)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/feedbackRequests` | GET | $skip, $top, $count |
| `/feedbackRequests('{recordId}')` | GET | - |
| `/feedback` | GET | $skip, $top, $count |
| `/feedback('{recordId}')` | GET | - |
| `/userCapabilities('{targetUserAssignmentUUID}')` | GET | - |

### PMGMContinuousPerformanceREST (REST API)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/activityStatuses` | GET | offset, limit |
| `/activityStatuses/{statusRecordId}` | GET | - |
| `/activities` | GET | offset, limit |
| `/activities/{activityRecordId}` | GET | - |
| `/activities/{activityRecordId}/activityUpdates` | GET | offset, limit |
| `/achievements` | GET | offset, limit |
| `/achievements/{achievementRecordId}` | GET | - |
| `/userPermissions` | GET | - |
| `/userPermissions/{targetUserAssignmentUUID}` | GET | - |

### PMGMPerformanceREST (REST API)

| Endpoint | Method | Pagination |
|----------|--------|------------|
| `/reviewRouteMaps/{reviewId}` | GET | - |

---

## Ingestion Type Summary

| Ingestion Type | Count | Description |
|----------------|-------|-------------|
| cdc | 45+ | Entities with lastModified/lastModifiedDateTime field |
| cdc_with_deletes | 10 | Entities with mdfSystemRecordStatus delete indicator |
| snapshot | 90+ | Entities without modification tracking |
| N/A | 1 | Service operation response types |

---

## Notes

1. **OData v2 Pagination**: Use `$skip`, `$top`, and `$inlinecount=allpages` for pagination
2. **OData v4 Pagination**: Use `$skip`, `$top`, and `$count=true` for pagination
3. **REST API Pagination**: Use `offset` and `limit` query parameters
4. **CDC with Deletes**: Filter on `mdfSystemRecordStatus` to identify deleted records
5. **Composite Keys**: Many form-related entities use composite keys (formContentId + formDataId + additional fields)
6. **Goal Plan Variants**: Goal entities (Goal_1 through Goal_101) represent different goal plan configurations
7. **Development Goals**: DevGoal_2001 and DevGoal_2002 represent different development goal plan templates
