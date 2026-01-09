#!/usr/bin/env python3
"""Generate full_pipeline_spec.md by parsing the entity registry directly."""

import json
import re
from pathlib import Path

def get_scd_type(ingestion_type: str) -> str:
    """Map ingestion type to SCD type."""
    mapping = {
        "cdc": "SCD_TYPE_2",
        "cdc_with_deletes": "SCD_TYPE_2",
        "snapshot": "SCD_TYPE_1",
        "append": "APPEND_ONLY",
    }
    return mapping.get(ingestion_type, "SCD_TYPE_2")

def build_entity_registry():
    """Build the entity registry (copied from sap_successfactors.py)."""
    registry = {}

    # Employee Central Core
    ec_core = {
        "User": {"pks": ["userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpEmployment": {"pks": ["personIdExternal", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpJob": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpCompensation": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpJobRelationships": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpWorkPermit": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpGlobalAssignment": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpPayCompRecurring": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpPayCompNonRecurring": {"pks": ["seqNumber", "startDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpCostAssignment": {"pks": ["effectiveStartDate", "worker"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "PerPerson": {"pks": ["personIdExternal"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerPersonal": {"pks": ["personIdExternal", "startDate"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerEmail": {"pks": ["personIdExternal", "emailType"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerPhone": {"pks": ["personIdExternal", "phoneType"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerAddressDEFLT": {"pks": ["personIdExternal", "addressType", "startDate"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerEmergencyContacts": {"pks": ["personIdExternal", "name"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "PerNationalId": {"pks": ["personIdExternal", "country", "cardType"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
        "EmpEmploymentTermination": {"pks": ["personIdExternal", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc"},
    }
    for name, cfg in ec_core.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg["ing"], "module": "employee_central",
        }

    # Foundation Objects
    fo_objects = [
        "FODepartment", "FOCompany", "FOCostCenter", "FOJobCode", "FOLocation",
        "FOBusinessUnit", "FODivision", "FOEventReason", "FOFrequency",
        "FOGeozoneMapping", "FOGlobalOrganization", "FOJobFunction", "FOJobClassLocalDEFLT",
        "FOLegalEntityLocalDEFLT", "FOPayComponent", "FOPayComponentGroup", "FOPayGrade",
        "FOPayGroup", "FOPayRange", "FOPayrollEntity", "FOWfConfig", "FOCorporateAddressDEFLT",
    ]
    for name in fo_objects:
        registry[name] = {
            "primary_keys": ["externalCode", "startDate"], "cursor_field": "lastModifiedDateTime",
            "ingestion_type": "cdc", "module": "employee_central",
        }

    # Single-key FO objects
    fo_single_key = ["Position", "JobClassificationCountry", "JobClassificationMethod"]
    for name in fo_single_key:
        registry[name] = {
            "primary_keys": ["code" if name == "Position" else "externalCode"],
            "cursor_field": "lastModifiedDateTime", "ingestion_type": "cdc",
            "module": "employee_central",
        }

    # Payment entities
    payment_entities = [
        "PaymentInformationV3", "PaymentInformationDetailV3",
        "Bank", "BankBranch", "Currency", "PayCalendar", "PayPeriod",
        "CustomPayType", "CustomPayTypeAssignment",
    ]
    for name in payment_entities:
        pks = ["externalCode"] if name != "PaymentInformationDetailV3" else ["PaymentInformationV3_effectiveStartDate", "PaymentInformationV3_worker", "externalCode"]
        registry[name] = {
            "primary_keys": pks, "cursor_field": "lastModifiedDateTime",
            "ingestion_type": "cdc", "module": "employee_central",
        }

    # Country-specific payment entities
    payment_countries = ["USA", "DEU", "GBR", "FRA", "CAN", "AUS", "IND", "JPN", "CHN", "BRA", "MEX",
                        "ARG", "AUT", "BEL", "BLR", "BOL", "CHE", "CHL", "COL",
                        "CZE", "DNK", "EGY", "ESP", "FIN", "GRC", "HKG", "HUN",
                        "IDN", "IRL", "ISR", "ITA", "KOR", "MYS", "NLD", "NOR",
                        "NZL", "PHL", "POL", "PRT", "RUS", "SAU", "SGP", "SVK",
                        "SVN", "SWE", "THA", "TUN", "TUR", "TWN", "VEN", "ZAF"]
    for country in payment_countries:
        name = f"PaymentInformationDetailV3{country}"
        registry[name] = {
            "primary_keys": ["PaymentInformationDetailV3_PaymentInformationV3_effectiveStartDate",
                             "PaymentInformationDetailV3_PaymentInformationV3_worker",
                             "PaymentInformationDetailV3_externalCode", "externalCode"],
            "cursor_field": "lastModifiedDateTime", "ingestion_type": "cdc",
            "module": "employee_central",
        }

    # Platform entities
    platform_entities = {
        "PickList": {"pks": ["picklistId"], "cursor": "lastModifiedDateTime"},
        "PickListV2": {"pks": ["PickListV2_id"], "cursor": "lastModifiedDateTime"},
        "PicklistOption": {"pks": ["id"], "cursor": "lastModifiedDateTime"},
        "PicklistLabel": {"pks": ["locale", "optionId"], "cursor": "lastModifiedDateTime"},
        "DynamicGroup": {"pks": ["groupID"], "cursor": "lastModifiedDateTime"},
        "DynamicGroupBean": {"pks": ["beanID"], "cursor": "lastModifiedDateTime"},
        "TodoEntryV3": {"pks": ["todoEntryId"], "cursor": "lastModifiedDateTime"},
        "TodoAction": {"pks": ["actionId"], "cursor": "lastModifiedDateTime"},
        "Attachment": {"pks": ["attachmentId"], "cursor": "lastModifiedDateTime"},
        "Photo": {"pks": ["photoType", "userId"], "cursor": "lastModifiedDateTime"},
        "TimeZone": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "Country": {"pks": ["code"], "cursor": "lastModifiedDateTime"},
        "WfRequest": {"pks": ["wfRequestId"], "cursor": "lastModifiedOn"},
        "WfRequestStep": {"pks": ["wfRequestStepId"], "cursor": "lastModifiedOn"},
        "WfRequestComments": {"pks": ["wfRequestCommentId"], "cursor": "lastModifiedOn"},
        "WfRequestUIData": {"pks": ["wfRequestId"], "cursor": "lastModifiedOn"},
        "MessageDetail": {"pks": ["code"], "cursor": "lastModifiedDateTime"},
        "SecondaryAssignment": {"pks": ["effectiveStartDate", "externalCode"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "SecondaryAssignmentsItem": {"pks": ["SecondaryAssignment_effectiveStartDate", "SecondaryAssignment_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in platform_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "platform",
        }

    # Recruiting entities
    recruiting_entities = {
        "Candidate": {"pks": ["candidateId"], "cursor": "lastModifiedDateTime"},
        "CandidateLight": {"pks": ["candidateId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_Certificates": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_Education": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_InsideWorkExperience": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_Languages": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_Mobility": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_OutsideWorkExperience": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_TalentPool": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateBackground_TalentPoolcorp": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "CandidateProfileConversionInfo": {"pks": ["candidateId"], "cursor": "lastModifiedDateTime"},
        "CandidateProfileExtension": {"pks": ["candidateId"], "cursor": "lastModifiedDateTime"},
        "CandidateTags": {"pks": ["tagId"], "cursor": "lastModifiedDateTime"},
        "CandidateComments": {"pks": ["commentId"], "cursor": "lastModifiedDateTime"},
        "JobApplication": {"pks": ["applicationId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_Certificates": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_Education": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_InsideWorkExperience": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_Languages": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_Mobility": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_OutsideWorkExperience": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_TalentPool": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationSnapshot_TalentPoolcorp": {"pks": ["backgroundElementId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationComments": {"pks": ["commentId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationInterview": {"pks": ["applicationInterviewId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationInterviewFieldControls": {"pks": ["applicationInterviewId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationOnboardingData": {"pks": ["applicationId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationOnboardingStatus": {"pks": ["applicationId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationAudit": {"pks": ["revNumber", "applicationId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationStatusAuditTrail": {"pks": ["revNumber"], "cursor": "createdDate"},
        "JobRequisition": {"pks": ["jobReqId"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "JobRequisitionLocale": {"pks": ["jobReqLocalId"], "cursor": "lastModifiedDateTime"},
        "JobRequisitionFieldControls": {"pks": ["jobReqId"], "cursor": "lastModifiedDateTime"},
        "JobRequisitionOperator": {"pks": ["jobReqId", "operatorRole"], "cursor": "lastModifiedDateTime"},
        "JobRequisitionPosting": {"pks": ["jobPostingId"], "cursor": "lastModifiedDateTime"},
        "JobRequisitionAssessment": {"pks": ["jobReqId"], "cursor": "lastModifiedDateTime"},
        "JobOffer": {"pks": ["offerApprovalId"], "cursor": "lastModifiedDateTime"},
        "JobOfferApprover": {"pks": ["offerApprovalId", "offerApproverId"], "cursor": "lastModifiedDateTime"},
        "JobOfferFieldControls": {"pks": ["offerApprovalId"], "cursor": "lastModifiedDateTime"},
        "JobOfferTemplate_Offer_Detail": {"pks": ["templateId"], "cursor": "lastModifiedDateTime"},
        "JobOfferTemplate_Standard_Offer": {"pks": ["templateId"], "cursor": "lastModifiedDateTime"},
        "OfferLetter": {"pks": ["offerApprovalId"], "cursor": "lastModifiedDateTime"},
        "InterviewOverallAssessment": {"pks": ["interviewOverallAssessmentId"], "cursor": "lastModifiedDateTime"},
        "RCMCompetency": {"pks": ["competencyId"], "cursor": "lastModifiedDateTime"},
        "RCMAdminReassignOfferApprover": {"pks": ["offerId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationAssessmentOrder": {"pks": ["assessmentOrderId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationAssessmentReport": {"pks": ["reportId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationAssessmentReportDetail": {"pks": ["reportId", "detailId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationBackgroundCheckRequest": {"pks": ["requestId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationBackgroundCheckResult": {"pks": ["resultId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationQuestionResponse": {"pks": ["responseId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationStatus": {"pks": ["statusId"], "cursor": "lastModifiedDateTime"},
        "JobApplicationStatusLabel": {"pks": ["labelId"], "cursor": "lastModifiedDateTime"},
        "JobReqQuestion": {"pks": ["questionId"], "cursor": "lastModifiedDateTime"},
        "JobReqScreeningQuestion": {"pks": ["questionId"], "cursor": "lastModifiedDateTime"},
        "JobReqScreeningQuestionChoice": {"pks": ["questionId", "choiceId"], "cursor": "lastModifiedDateTime"},
        "JobReqGOPosition": {"pks": ["jobReqId", "positionId"], "cursor": "lastModifiedDateTime"},
        "JobRequisitionGroupOperator": {"pks": ["jobReqId", "operatorRole", "recruiterId"], "cursor": "lastModifiedDateTime"},
        "JobReqFwdCandidates": {"pks": ["candidateId", "jobReqId"], "cursor": "lastModifiedDateTime"},
        "InterviewIndividualAssessment": {"pks": ["assessmentId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in recruiting_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "recruiting",
        }

    # Goal entities (Goal_1 through Goal_8)
    for i in range(1, 9):
        registry[f"Goal_{i}"] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc_with_deletes", "module": "performance",
        }
        for suffix in ["Task", "Metric", "Target", "AchievementsList", "AchievementsItem"]:
            registry[f"Goal{suffix}_{i}"] = {
                "primary_keys": ["id"], "cursor_field": "lastModified",
                "ingestion_type": "cdc", "module": "performance",
            }
        # Permission variants
        registry[f"GoalPermission_{i}"] = {
            "primary_keys": ["id"], "cursor_field": None,
            "ingestion_type": "snapshot", "module": "performance",
        }
        registry[f"GoalMilestone_{i}"] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }
        registry[f"GoalComment_{i}"] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }
        registry[f"GoalTaskPermission_{i}"] = {
            "primary_keys": ["id"], "cursor_field": None,
            "ingestion_type": "snapshot", "module": "performance",
        }
        registry[f"GoalMilestonePermission_{i}"] = {
            "primary_keys": ["id"], "cursor_field": None,
            "ingestion_type": "snapshot", "module": "performance",
        }

    # Team Goals
    for i in [1, 5, 7]:
        registry[f"TeamGoal_{i}"] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }

    # Simple goal entities
    simple_goal = ["SimpleGoal", "DevGoal", "DevGoalCompetency", "DevGoalDetail",
                   "DevGoalPlanTemplate", "DevGoalTask", "DevGoalEnum"]
    for name in simple_goal:
        registry[name] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }

    # Goal plan entities
    goal_plan_entities = ["GoalPlanState", "GoalPlanTemplate", "GoalWeight"]
    for name in goal_plan_entities:
        registry[name] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }

    # Goal_101
    registry["Goal_101"] = {
        "primary_keys": ["id"], "cursor_field": "lastModified",
        "ingestion_type": "cdc_with_deletes", "module": "performance",
    }

    # DevGoal variants
    for i in [2001, 2002]:
        registry[f"DevGoal_{i}"] = {
            "primary_keys": ["id"], "cursor_field": "lastModified",
            "ingestion_type": "cdc", "module": "performance",
        }
        registry[f"DevGoalPermission_{i}"] = {
            "primary_keys": ["id"], "cursor_field": None,
            "ingestion_type": "snapshot", "module": "performance",
        }

    # Performance form entities
    perf_form_entities = {
        "FormHeader": {"pks": ["formDataId"], "cursor": "lastModifiedDateTime"},
        "FormContent": {"pks": ["formContentId"], "cursor": "lastModifiedDateTime"},
        "FormFolder": {"pks": ["folderId"], "cursor": "lastModifiedDateTime"},
        "FormSubject": {"pks": ["formSubjectId"], "cursor": "lastModifiedDateTime"},
        "FormPerfPotSummary": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormObjective": {"pks": ["formContentId", "formDataId", "itemId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormObjectiveComment": {"pks": ["formContentId", "formDataId", "itemId", "sectionIndex", "userId"], "cursor": "lastModifiedDateTime"},
        "FormObjectiveOtherDetails": {"pks": ["formContentId", "formDataId", "itemId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormCustomElement": {"pks": ["elementKey", "formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormRatingScale": {"pks": ["formContentId", "formDataId", "sectionIndex", "scaleId"], "cursor": "lastModifiedDateTime"},
        "FormRatingScaleValue": {"pks": ["formContentId", "formDataId", "scaleId", "scaleIndex", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormReviewerInfoSection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormReviewFeedback": {"pks": ["formContentId", "formDataId", "formReviewFeedbackId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormReviewFeedbackList": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormSectionConfiguration": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormSectionComment": {"pks": ["formContentId", "formDataId", "sectionIndex", "userId"], "cursor": "lastModifiedDateTime"},
        "FormSummarySection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormUserInformationSection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormAuditTrail": {"pks": ["auditTrailId"], "cursor": "lastModifiedDateTime"},
        "FormIntroductionSection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormJobRole": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormRouteMap": {"pks": ["formDataId"], "cursor": "lastModifiedDateTime"},
        "FormRouteSubStep": {"pks": ["formDataId", "stepOrder"], "cursor": "lastModifiedDateTime"},
        "FormSignature": {"pks": ["formDataId", "signatureOrder"], "cursor": "lastModifiedDateTime"},
        "FormSignatureSection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "FormTemplate": {"pks": ["formTemplateId"], "cursor": "lastModifiedDateTime"},
        "PMReviewerInfoSectionConfig": {"pks": ["formReviewerInfoSectionConfigId"], "cursor": "lastModifiedDateTime"},
        "PerformanceReviewContent": {"pks": ["formContentId", "formDataId"], "cursor": "lastModifiedDateTime"},
        "PerformanceReviewContentDetail": {"pks": ["formContentId", "formDataId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in perf_form_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": "cdc", "module": "performance",
        }

    # Form360 entities
    form360_entities = {
        "Form360Participant": {"pks": ["formContentId", "formDataId", "participantId"], "cursor": "lastModifiedDateTime"},
        "Form360ParticipantConfig": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "Form360ParticipantSection": {"pks": ["formContentId", "formDataId", "participantId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "Form360ParticipantDetail": {"pks": ["formContentId", "formDataId", "participantId", "itemId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "Form360ParticipantCategory": {"pks": ["formContentId", "formDataId", "categoryOrder"], "cursor": "lastModifiedDateTime"},
        "Form360ParticipantColumn": {"pks": ["formContentId", "formDataId", "columnKey"], "cursor": "lastModifiedDateTime"},
        "Form360Rater": {"pks": ["formContentId", "formDataId", "participantId"], "cursor": "lastModifiedDateTime"},
        "Form360RaterSection": {"pks": ["formContentId", "formDataId", "participantId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "Form360SummarySection": {"pks": ["formContentId", "formDataId", "sectionIndex"], "cursor": "lastModifiedDateTime"},
        "Form360ReviewContentDetail": {"pks": ["formContentId", "formDataId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in form360_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": "cdc", "module": "performance",
        }

    # CPM entities
    cpm_entities = {
        "Achievement": {"pks": ["achievementId"], "ing": "cdc_with_deletes"},
        "AchievementDevGoalDetail": {"pks": ["Achievement_achievementId", "externalCode"], "ing": "cdc"},
        "AchievementGoalDetail": {"pks": ["Achievement_achievementId", "externalCode"], "ing": "cdc"},
        "Activity": {"pks": ["activityId"], "ing": "cdc_with_deletes"},
        "ActivityFeedback": {"pks": ["Activity_activityId", "feedbackId"], "ing": "cdc"},
        "ActivityStatus": {"pks": ["externalCode"], "ing": "cdc"},
        "Feedback": {"pks": ["feedbackId"], "ing": "cdc_with_deletes"},
        "FeedbackFlag": {"pks": ["Feedback_feedbackId", "externalCode"], "ing": "cdc"},
        "PMActivity": {"pks": ["activityId"], "ing": "cdc_with_deletes"},
        "PMAchievement": {"pks": ["achievementId"], "ing": "cdc_with_deletes"},
        "PMActivityFeedback": {"pks": ["activityId", "feedbackId"], "ing": "cdc"},
        "CalibrationSession": {"pks": ["sessionId"], "ing": "cdc"},
        "CalibrationSessionSubject": {"pks": ["sessionSubjectId"], "ing": "cdc"},
        "CalibrationSubjectRank": {"pks": ["subjectRankId"], "ing": "cdc"},
        "CalibrationTemplate": {"pks": ["templateId"], "ing": "cdc"},
    }
    for name, cfg in cpm_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": "lastModifiedDateTime",
            "ingestion_type": cfg["ing"], "module": "performance",
        }

    # Time entities
    time_entities = {
        "TimeAccount": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountDetail": {"pks": ["TimeAccount_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountPostingRule": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountPurchaseProfile": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountPurchaseProfilePayComponentAssignment": {"pks": ["TimeAccountPurchaseProfile_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountSnapshot": {"pks": ["accountSnapshotIdentifier"], "cursor": "lastModifiedDateTime"},
        "TimeAccountType": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeAccountTypeAUS": {"pks": ["TimeAccountType_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeType": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeTypeProfile": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeGroup": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeGroupItem": {"pks": ["EmployeeTimeGroup_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeMEX": {"pks": ["EmployeeTime_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeUSA": {"pks": ["EmployeeTime_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeSheet": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeSheetEntry": {"pks": ["EmployeeTimeSheet_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeValuationResult": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "WorkSchedule": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "WorkScheduleDay": {"pks": ["WorkSchedule_externalCode", "day"], "cursor": "lastModifiedDateTime"},
        "WorkScheduleDayModel": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "WorkScheduleDayModelSegment": {"pks": ["WorkScheduleDayModel_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "HolidayCalendar": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "Holiday": {"pks": ["HolidayCalendar_externalCode", "holidayDate"], "cursor": "lastModifiedDateTime"},
        "HolidayAssignment": {"pks": ["Holiday_HolidayCalendar_externalCode", "Holiday_holidayDate", "externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeManagementAlert": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeManagementAlertMessage": {"pks": ["TimeManagementAlert_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTime": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "EmployeeTimeAUS": {"pks": ["EmployeeTime_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "EmployeeTimeCalendar": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TemporaryTimeInformation": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "AvailableTimeType": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "TimeEventType": {"pks": ["code"], "cursor": "lastModifiedDateTime"},
        "ClockInClockOutMessage": {"pks": ["messageId"], "cursor": "lastModifiedDateTime"},
        "ClockInClockOutGroup": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ClockInClockOutBreakTimes": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ClockInClockOutConfiguration": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in time_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "time_attendance",
        }

    # Succession entities
    succession_entities = {
        "TalentPool": {"pks": ["code"], "cursor": "lastModifiedDateTime"},
        "Successor": {"pks": ["id"], "cursor": "lastModifiedDateTime"},
        "NominationTarget": {"pks": ["nominationId"], "cursor": "lastModifiedDateTime"},
        "NomineeRelationships": {"pks": ["nomineeId", "nominationId"], "cursor": "lastModifiedDateTime"},
        "RightToReturn": {"pks": ["positionId", "returnToWorkDate", "userId"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "PositionCompetencyMappingEntity": {"pks": ["Position_code", "externalCode"], "cursor": "lastModifiedDateTime"},
        "PositionMatrixRelationship": {"pks": ["Position_code", "matrixRelationshipType", "relatedPosition"], "cursor": "lastModifiedDateTime"},
        "PositionRightToReturn": {"pks": ["Position_code", "externalCode"], "cursor": "lastModifiedDateTime"},
        "SuccessionGoal": {"pks": ["goalId"], "cursor": "lastModified"},
        "SuccessionGoalDetail": {"pks": ["goalDetailId"], "cursor": "lastModified"},
        "SuccessionGoalPlan": {"pks": ["goalPlanId"], "cursor": "lastModified"},
        "Mentor": {"pks": ["mentorId"], "cursor": "lastModifiedDateTime"},
        "MentorNominee": {"pks": ["nomineeId"], "cursor": "lastModifiedDateTime"},
        "Competency": {"pks": ["competencyId"], "cursor": "lastModifiedDateTime"},
        "CompetencyContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "CompetencyEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "CompetencyRating": {"pks": ["competencyRatingId"], "cursor": "lastModifiedDateTime"},
        "CompetencyType": {"pks": ["GUID"], "cursor": "lastModifiedDateTime"},
        "CertificationContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "CertificationEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "LegacyPositionEntity": {"pks": ["positionId"], "cursor": "lastModifiedDateTime"},
        "RoleEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SkillContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "SkillEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SkillProfile": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "InterviewQuestionContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "InterviewQuestionEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "JobProfile": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "JobResponsibilityContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "JobResponsibilityEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "EducationDegreeContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "EducationDegreeEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "EducationMajorContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "EducationMajorEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "PhysicalReqContent": {"pks": ["jobProfileId", "roleId"], "cursor": "lastModifiedDateTime"},
        "PhysicalReqEntity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAward": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardBudget": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardCategory": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardGuidelinesRule": {"pks": ["SpotAwardProgram_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardLevel": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardProgram": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardRedemption": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardRedemptionOrder": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "SpotAwardRedemptionProduct": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "NomineeHistory": {"pks": ["historyId"], "cursor": "lastModifiedDateTime"},
        "TalentGraphicOption": {"pks": ["optionId"], "cursor": "lastModifiedDateTime"},
        "TalentRatings": {"pks": ["ratingId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSessionOwner": {"pks": ["sessionId", "ownerId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSessionReviewer": {"pks": ["sessionId", "reviewerId"], "cursor": "lastModifiedDateTime"},
        "CalibrationExecutiveReviewer": {"pks": ["sessionId", "reviewerId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSubjectRating": {"pks": ["ratingId"], "cursor": "lastModifiedDateTime"},
        "CalibrationRating": {"pks": ["ratingId"], "cursor": "lastModifiedDateTime"},
        "CalibrationRatingOption": {"pks": ["optionId"], "cursor": "lastModifiedDateTime"},
        "CalibrationTemplateRater": {"pks": ["templateId", "raterId"], "cursor": "lastModifiedDateTime"},
        "CalibrationTemplateCommentType": {"pks": ["templateId", "typeId"], "cursor": "lastModifiedDateTime"},
        "CalibrationTemplateCommentFieldName": {"pks": ["templateId", "fieldNameId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSubjectWeightage": {"pks": ["subjectId", "weightageId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSubjectObjectRanking": {"pks": ["subjectId", "rankingId"], "cursor": "lastModifiedDateTime"},
        "CalibrationCompetencyRating": {"pks": ["ratingId"], "cursor": "lastModifiedDateTime"},
        "DevLearning_4201": {"pks": ["learningId"], "cursor": None, "ing": "snapshot"},
        "DevLearningCertifications": {"pks": ["certificationId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in succession_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "succession",
        }

    # Onboarding entities
    onboarding_entities = {
        "ONB2Process": {"pks": ["processId"], "cursor": "lastModifiedDateTime"},
        "ONB2ProcessTask": {"pks": ["processTaskId"], "cursor": "lastModifiedDateTime"},
        "ONB2ResponsiblePartyConfig": {"pks": ["ONB2ProcessTask_processTaskId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2ExternalHireData": {"pks": ["externalHireId"], "cursor": "lastModifiedDateTime"},
        "ONB2BuddyActivity": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2BuddyProfile": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2DataCollectionUserConfig": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2Equipment": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2EquipmentActivity": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2EquipmentType": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2EquipmentTypeValue": {"pks": ["ONB2EquipmentType_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2NewHireActivitiesStep": {"pks": ["processStepId"], "cursor": "lastModifiedDateTime"},
        "ONB2OffboardeeDetails": {"pks": ["processId"], "cursor": "lastModifiedDateTime"},
        "ONB2OffboardingInfo": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2OnboardeeDetails": {"pks": ["processId"], "cursor": "lastModifiedDateTime"},
        "ONB2OnboardingInfo": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2RecommendedActivity": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2ReviewStep": {"pks": ["processStepId"], "cursor": "lastModifiedDateTime"},
        "ONB2WelcomeActivity": {"pks": ["ONB2Process_processId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "ONB2WelcomeStep": {"pks": ["processStepId"], "cursor": "lastModifiedDateTime"},
        "ComplianceProcess": {"pks": ["processId"], "cursor": "lastModifiedDateTime"},
        "ComplianceProcessTask": {"pks": ["processTaskId"], "cursor": "lastModifiedDateTime"},
        "ComplianceFormData": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ComplianceDocumentFlow": {"pks": ["flowId"], "cursor": "lastModifiedDateTime"},
        "ComplianceFormSignature": {"pks": ["signatureId"], "cursor": "lastModifiedDateTime"},
        "ComplianceUserFormData": {"pks": ["userId", "formId"], "cursor": "lastModifiedDateTime"},
        "ComplianceFormDataFieldValue": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "AssignedComplianceForm": {"pks": ["formId"], "cursor": "lastModifiedDateTime"},
        "OnboardingProcess": {"pks": ["onboardingProcessId"], "cursor": "lastModifiedDateTime"},
        "OnboardingGoal": {"pks": ["goalId"], "cursor": "lastModifiedDateTime"},
        "OnboardingGoalActivity": {"pks": ["activityId"], "cursor": "lastModifiedDateTime"},
        "OnboardingGoalCategory": {"pks": ["categoryId"], "cursor": "lastModifiedDateTime"},
        "OnboardingMeetingActivity": {"pks": ["activityId", "processStepId", "onboardingProcessId"], "cursor": "lastModifiedDateTime"},
        "OnboardingMeetingEvent": {"pks": ["eventId"], "cursor": "lastModifiedDateTime"},
        "OnboardingEquipmentActivity": {"pks": ["activityId", "processStepId", "onboardingProcessId"], "cursor": "lastModifiedDateTime"},
        "OnboardingEquipment": {"pks": ["equipmentId"], "cursor": "lastModifiedDateTime"},
        "OnboardingEquipmentType": {"pks": ["typeId"], "cursor": "lastModifiedDateTime"},
        "OnboardingEquipmentTypeValue": {"pks": ["valueId"], "cursor": "lastModifiedDateTime"},
        "OnboardingCandidateInfo": {"pks": ["applicantId"], "cursor": "lastModifiedDateTime"},
        "OnboardingNewHireActivitiesStep": {"pks": ["processStepId", "onboardingProcessId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in onboarding_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "onboarding",
        }

    # Finance entities
    finance_entities = {
        "GLAccountMapping": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ExpenseItem": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "ExpenseItemType": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "PayrollConfigurationCategory": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "PayrollExternalHRIS": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "PayrollSystemConfiguration": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "NonRecurringPayment": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "RecurringDeduction": {"pks": ["effectiveStartDate", "userSysId"], "cursor": "lastModifiedDateTime"},
        "RecurringDeductionItem": {"pks": ["RecurringDeduction_effectiveStartDate", "RecurringDeduction_userSysId", "payComponentType"], "cursor": "lastModifiedDateTime"},
        "AdvancesInstallments": {"pks": ["NonRecurringPayment_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "BenefitEnrollmentConfirmation": {"pks": ["benefitEnrollmentId"], "cursor": "lastModifiedDateTime"},
        "CentralCompensation": {"pks": ["effectiveStartDate", "userId"], "cursor": "lastModifiedDateTime"},
        "CentralCompensationItem": {"pks": ["CentralCompensation_effectiveStartDate", "CentralCompensation_userId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "CentralCompensationPayComponent": {"pks": ["CentralCompensationItem_CentralCompensation_effectiveStartDate", "CentralCompensationItem_CentralCompensation_userId", "CentralCompensationItem_externalCode", "payComponent"], "cursor": "lastModifiedDateTime"},
        "BenefitProgramGroupItem": {"pks": ["BenefitProgramGroup_externalCode", "externalCode"], "cursor": "lastModifiedDateTime"},
        "BenefitProgramGroup": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "BudgetPeriodGO": {"pks": ["budgetPeriodId", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "FunctionalAreaGO": {"pks": ["functionalAreaID", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "FundCenterGO": {"pks": ["externalCode", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "FundGO": {"pks": ["externalCode", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "GrantGO": {"pks": ["grantCode", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
        "ProjectControllingObject": {"pks": ["externalCode", "effectiveStartDate"], "cursor": "lastModifiedDateTime", "ing": "cdc_with_deletes"},
    }
    for name, cfg in finance_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "finance",
        }

    # Legal Entity country variants
    legal_countries = [
        "DEU", "ESP", "FRA", "GBR", "USA", "ARG", "AUS", "AUT", "BEL", "BLR", "BOL", "BRA", "CAN", "CHE", "CHL",
        "CHN", "COL", "CZE", "DNK", "EGY", "FIN", "GRC", "HKG", "HUN", "IDN",
        "IND", "IRL", "ISR", "ITA", "JPN", "KOR", "MEX", "MYS", "NLD", "NOR",
        "NZL", "PHL", "POL", "PRT", "RUS", "SAU", "SGP", "SVK", "SVN", "SWE",
        "THA", "TUN", "TUR", "TWN", "VEN", "ZAF"
    ]
    for country in legal_countries:
        name = f"LegalEntity{country}"
        if name not in registry:
            registry[name] = {
                "primary_keys": ["LegalEntity_externalCode", "externalCode"],
                "cursor_field": "lastModifiedDateTime", "ingestion_type": "cdc",
                "module": "finance",
            }

    # Benefits entities
    benefit_entities = {
        "Benefit": {"pks": ["benefitId"], "cursor": "lastModifiedDateTime"},
        "BenefitsProgramDetail": {"pks": ["externalCode", "effectiveStartDate"], "cursor": "lastModifiedDateTime"},
        "BenefitsAvailableProgramOption": {"pks": ["externalCode"], "cursor": "lastModifiedDateTime"},
        "BenefitEnrollment": {"pks": ["enrollmentId"], "cursor": "lastModifiedDateTime"},
        "BenefitEnrollmentDocument": {"pks": ["documentId"], "cursor": "lastModifiedDateTime"},
        "BenefitProgram": {"pks": ["programId"], "cursor": "lastModifiedDateTime"},
        "BenefitProgramOptions": {"pks": ["optionId"], "cursor": "lastModifiedDateTime"},
        "BenefitInsurancePlan": {"pks": ["planId"], "cursor": "lastModifiedDateTime"},
        "BenefitInsurancePlanUSA": {"pks": ["BenefitInsurancePlan_planId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "BenefitInsuranceCoverage": {"pks": ["coverageId"], "cursor": "lastModifiedDateTime"},
        "BenefitInsuranceCoverageDetails": {"pks": ["detailId"], "cursor": "lastModifiedDateTime"},
        "BenefitInsuranceProvider": {"pks": ["providerId"], "cursor": "lastModifiedDateTime"},
        "BenefitInsuranceEnrollmentDetails": {"pks": ["detailId"], "cursor": "lastModifiedDateTime"},
        "BenefitSavingsPlan": {"pks": ["planId"], "cursor": "lastModifiedDateTime"},
        "BenefitSavingsPlanSubType": {"pks": ["subTypeId"], "cursor": "lastModifiedDateTime"},
        "BenefitSavingsPlanEnrollment": {"pks": ["enrollmentId"], "cursor": "lastModifiedDateTime"},
        "BenefitPensionFund": {"pks": ["fundId"], "cursor": "lastModifiedDateTime"},
        "BenefitPensionPlan": {"pks": ["planId"], "cursor": "lastModifiedDateTime"},
        "BenefitPensionPlanContribution": {"pks": ["contributionId"], "cursor": "lastModifiedDateTime"},
        "BenefitCompanyCar": {"pks": ["carId"], "cursor": "lastModifiedDateTime"},
        "BenefitCompanyCarEnrollment": {"pks": ["enrollmentId"], "cursor": "lastModifiedDateTime"},
        "BenefitCompanyCarOrder": {"pks": ["orderId"], "cursor": "lastModifiedDateTime"},
        "BenefitCompanyHousing": {"pks": ["housingId"], "cursor": "lastModifiedDateTime"},
        "BenefitCompanyHousingEnrollment": {"pks": ["enrollmentId"], "cursor": "lastModifiedDateTime"},
        "BenefitEmployeeClaim": {"pks": ["claimId"], "cursor": "lastModifiedDateTime"},
        "BenefitEmployeeClaimDetail": {"pks": ["BenefitEmployeeClaim_claimId", "externalCode"], "cursor": "lastModifiedDateTime"},
        "BenefitClaimConfiguration": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "BenefitDependentDetail": {"pks": ["dependentId"], "cursor": "lastModifiedDateTime"},
        "BenefitDependentCoverage": {"pks": ["coverageId"], "cursor": "lastModifiedDateTime"},
        "BenefitEvent": {"pks": ["eventId"], "cursor": "lastModifiedDateTime"},
        "BenefitLifeEventConfiguration": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "BenefitDocuments": {"pks": ["documentId"], "cursor": "lastModifiedDateTime"},
        "BenefitLegalEntity": {"pks": ["entityId"], "cursor": "lastModifiedDateTime"},
        "BenefitEligibilityRule": {"pks": ["ruleId"], "cursor": "lastModifiedDateTime"},
        "BenefitProgramConfiguration": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "BenefitPayComponentDetail": {"pks": ["detailId"], "cursor": "lastModifiedDateTime"},
        "BenefitPlanCoverage": {"pks": ["coverageId"], "cursor": "lastModifiedDateTime"},
        "BenefitCost": {"pks": ["costId"], "cursor": "lastModifiedDateTime"},
        "BenefitsCreditConfiguration": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "BenefitHSAEmployerContribution": {"pks": ["contributionId"], "cursor": "lastModifiedDateTime"},
        "BenefitFSAConfiguration": {"pks": ["configId"], "cursor": "lastModifiedDateTime"},
        "EmpPensionAdditionalEmployeeContributionDetail": {"pks": ["detailId"], "cursor": "lastModifiedDateTime"},
        "EmpPensionAdditionalEmployerContributionDetail": {"pks": ["detailId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in benefit_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": "cdc", "module": "benefits",
        }

    # Learning
    registry["LearningHistoryData"] = {
        "primary_keys": ["lmsId", "userId"], "cursor_field": "lastModifiedDateTime",
        "ingestion_type": "cdc", "module": "learning",
    }

    # SCIM entities
    scim_entities = {
        "ScimUser": {"pks": ["id"], "cursor": "lastModified"},
        "ScimGroup": {"pks": ["id"], "cursor": "lastModified"},
        "ScimSchema": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "ScimResourceType": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "ScimServiceProviderConfig": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
    }
    for name, cfg in scim_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "identity",
        }

    # REST API entities
    rest_entities = {
        "TimeAccountBalanceResponse": {"pks": ["userId", "timeAccountType"], "cursor": None, "ing": "snapshot"},
        "customTasks": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "journeyDetails": {"pks": ["journeyId"], "cursor": None, "ing": "snapshot"},
        "FMLARequest": {"pks": ["assignmentId", "id"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompEntryDTO": {"pks": ["compEntryId"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompSalaryEntryDTO": {"pks": ["entryId"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompBonusEntryDTO": {"pks": ["entryId"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompStockEntryDTO": {"pks": ["entryId"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompVarpayEntryDTO": {"pks": ["entryId"], "cursor": None, "ing": "snapshot"},
        "EmployeeCompForceCommentDTO": {"pks": ["commentId"], "cursor": None, "ing": "cdc"},
        "PBCReplicationData": {"pks": ["id", "startDate", "endDate"], "cursor": None, "ing": "cdc"},
        "SymbolicAccountData": {"pks": ["id"], "cursor": None, "ing": "cdc"},
        "EmployeeGroupingData": {"pks": ["id"], "cursor": None, "ing": "cdc"},
        "i9AuditTrailRecord": {"pks": ["externalCode"], "cursor": None, "ing": "append"},
        "TimeTypeBalanceResponse": {"pks": ["userId", "timeTypeCode"], "cursor": None, "ing": "snapshot"},
        "TerminationTimeAccountBalanceResponse": {"pks": ["userId"], "cursor": None, "ing": "snapshot"},
        "TimeOffEventResponse": {"pks": ["externalCode"], "cursor": None, "ing": "snapshot"},
        "DPCSVersion": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "DPCSStatus": {"pks": ["type", "country", "subjectId"], "cursor": None, "ing": "snapshot"},
        "ExtensionPointTaskDetail": {"pks": ["taskId"], "cursor": None, "ing": "snapshot"},
        "InstructionalTextEO": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
    }
    for name, cfg in rest_entities.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "snapshot"), "module": "rest_api",
        }

    # Custom MDF entities
    mdf_entities = [
        "cust_RCMApplicantStatus", "cust_RCMJobReqStatus", "cust_RCMOfferStatus",
        "cust_Location", "cust_Department", "cust_CostCenter",
        "cust_WorkLocation", "cust_PayGrade", "cust_PayRange",
        "cust_EmployeeClass", "cust_EmploymentType", "cust_RegularTemp",
        "cust_ManagerLevel", "cust_JobClassificationMethod",
    ]
    for name in mdf_entities:
        registry[name] = {
            "primary_keys": ["externalCode"], "cursor_field": "lastModifiedDateTime",
            "ingestion_type": "cdc", "module": "custom",
        }

    # OData v4 extended entities
    odata_v4_extended = {
        "AdditionalServices": {"pks": ["id"], "cursor": None, "ing": "snapshot"},
        "CalibrationSessionV4": {"pks": ["sessionId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSubjectV4": {"pks": ["subjectId"], "cursor": "lastModifiedDateTime"},
        "CalibrationSubjectComment": {"pks": ["commentId"], "cursor": "lastModifiedDateTime"},
        "ClockInClockOutExternal": {"pks": ["externalId"], "cursor": "lastChangedAt"},
        "timeevents": {"pks": ["externalId"], "cursor": "lastChangedAt", "ing": "append"},
        "TimeEventTypes": {"pks": ["code"], "cursor": None, "ing": "snapshot"},
        "SCMNominationApprovalWorkflow": {"pks": ["approvalId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in odata_v4_extended.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "odata_v4",
        }

    # Platform extended entities
    platform_extended = {
        "ExternalUser": {"pks": ["externalUserId"], "cursor": "lastModifiedDateTime"},
        "ExternalLearner": {"pks": ["externalLearnerId"], "cursor": "lastModifiedDateTime"},
        "ExternalLearnerPersonalInfo": {"pks": ["ExternalLearner_externalLearnerId", "itemId"], "cursor": "lastModifiedDateTime"},
        "ExternalLearnerEmailInfo": {"pks": ["ExternalLearner_externalLearnerId", "itemId"], "cursor": "lastModifiedDateTime"},
        "ExternalLearnerAddressInfo": {"pks": ["ExternalLearner_externalLearnerId", "itemId"], "cursor": "lastModifiedDateTime"},
        "ExternalLearnerPhoneInfo": {"pks": ["ExternalLearner_externalLearnerId", "itemId"], "cursor": "lastModifiedDateTime"},
        "ExtAddressInfo": {"pks": ["addressId"], "cursor": "lastModifiedDateTime"},
        "ExtEmailInfo": {"pks": ["emailId"], "cursor": "lastModifiedDateTime"},
        "ExtPersonalInfo": {"pks": ["personalInfoId"], "cursor": "lastModifiedDateTime"},
        "ExtPhoneInfo": {"pks": ["phoneId"], "cursor": "lastModifiedDateTime"},
        "EMMonitoredProcess": {"pks": ["processDefinitionId", "processInstanceId", "processType"], "cursor": "lastEventTime"},
        "EMEvent": {"pks": ["id"], "cursor": "eventTime", "ing": "append"},
        "EMEventPayload": {"pks": ["eventId", "payloadId"], "cursor": "eventTime", "ing": "append"},
        "EMEventAttribute": {"pks": ["eventId", "attributeId"], "cursor": "eventTime", "ing": "append"},
        "ThemeTemplate": {"pks": ["id"], "cursor": "lastModifiedDate"},
        "ThemeExternalResource": {"pks": ["themeId", "resourceId"], "cursor": "lastModifiedDate"},
        "RBPBasicPermission": {"pks": ["permissionId"], "cursor": "lastModifiedDateTime"},
        "RBPRole": {"pks": ["roleId"], "cursor": "lastModifiedDateTime"},
        "RBPRule": {"pks": ["ruleId"], "cursor": "lastModifiedDateTime"},
        "UserPermissions": {"pks": ["userId"], "cursor": "lastModifiedDateTime"},
        "UserCapabilities": {"pks": ["userId"], "cursor": "lastModifiedDateTime"},
        "WfRequestParticipator": {"pks": ["wfRequestParticipatorId"], "cursor": "lastModifiedOn"},
        "CurrencyConversion": {"pks": ["fromCurrency", "toCurrency", "effectiveDate"], "cursor": "lastModifiedDateTime"},
        "MDFEnumValue": {"pks": ["externalCode", "mdfSystemEffectiveStartDate"], "cursor": "lastModifiedDateTime"},
        "MDFLocalizedValue": {"pks": ["externalCode", "locale"], "cursor": "lastModifiedDateTime"},
        "WorkOrder": {"pks": ["workOrderId"], "cursor": "lastModifiedDateTime"},
        "VendorInfo": {"pks": ["vendorId"], "cursor": "lastModifiedDateTime"},
        "InitiativeAlignmentBean": {"pks": ["initiativeId"], "cursor": "lastModifiedDateTime"},
        "CompanyProvisioner": {"pks": ["id"], "cursor": "lastModifiedDateTime"},
        "SuccessStoreContentBlob": {"pks": ["contentId", "blobId"], "cursor": None, "ing": "snapshot"},
        "DynamicGroupDefinition": {"pks": ["groupId"], "cursor": "lastModifiedDateTime"},
        "DGExpression": {"pks": ["expressionId"], "cursor": "lastModifiedDateTime"},
        "DGField": {"pks": ["fieldId"], "cursor": "lastModifiedDateTime"},
        "DGFieldValue": {"pks": ["fieldId", "valueId"], "cursor": "lastModifiedDateTime"},
        "DGFilter": {"pks": ["filterId"], "cursor": "lastModifiedDateTime"},
        "DGPeoplePool": {"pks": ["poolId"], "cursor": "lastModifiedDateTime"},
        "DGFieldOperator": {"pks": ["operatorId"], "cursor": "lastModifiedDateTime"},
    }
    for name, cfg in platform_extended.items():
        registry[name] = {
            "primary_keys": cfg["pks"], "cursor_field": cfg["cursor"],
            "ingestion_type": cfg.get("ing", "cdc"), "module": "platform",
        }

    # Job Classification Country Variants
    job_classification_countries = ["AUS", "BRA", "CAN", "FRA", "GBR", "ITA", "USA", "ZAF"]
    for country in job_classification_countries:
        name = f"JobClassificationCountry{country}"
        if name not in registry:
            registry[name] = {
                "primary_keys": ["JobClassificationCountry_externalCode", "externalCode"],
                "cursor_field": "lastModifiedDateTime", "ingestion_type": "cdc",
                "module": "employee_central",
            }

    return registry

def generate_pipeline_spec():
    """Generate the full pipeline spec markdown file."""
    registry = build_entity_registry()

    # Group entities by module
    modules = {}
    for name, config in registry.items():
        module = config.get("module", "other")
        if module not in modules:
            modules[module] = []
        modules[module].append((name, config))

    # Sort entities within each module
    for module in modules:
        modules[module].sort(key=lambda x: x[0])

    # Define module order
    module_order = [
        "employee_central", "platform", "recruiting", "performance",
        "time_attendance", "succession", "onboarding", "finance",
        "benefits", "learning", "identity", "rest_api", "custom", "odata_v4"
    ]

    # Generate output
    lines = []
    lines.append("# SAP SuccessFactors - Complete Pipeline Specification")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- **Total entities**: {len(registry)}")
    lines.append("- **Organized by**: Module/functional area")
    lines.append("- **Generated from**: `_ENTITY_REGISTRY` in `sap_successfactors.py`")
    lines.append("")
    lines.append("## Usage")
    lines.append("")
    lines.append("Copy the entire `pipeline_spec` below or select specific modules/entities as needed.")
    lines.append("Modify `connection_name` to match your Unity Catalog connection.")
    lines.append("")
    lines.append("## Pipeline Specification")
    lines.append("")
    lines.append("```python")
    lines.append("pipeline_spec = {")
    lines.append('    "connection_name": "sap_successfactors_connection",')
    lines.append('    "objects": [')

    for module in module_order:
        if module not in modules:
            continue
        entities = modules[module]
        lines.append(f"        # {'=' * 65}")
        lines.append(f"        # Module: {module} ({len(entities)} entities)")
        lines.append(f"        # {'=' * 65}")

        for name, config in entities:
            pks = config.get("primary_keys", [])
            cursor = config.get("cursor_field")
            ing_type = config.get("ingestion_type", "cdc")
            scd_type = get_scd_type(ing_type)

            lines.append("        {")
            lines.append('            "table": {')
            lines.append(f'                "source_table": "{name}",')
            lines.append('                "table_configuration": {')
            lines.append(f'                    "scd_type": "{scd_type}",')
            lines.append(f'                    "primary_keys": \'{json.dumps(pks)}\'{"," if cursor else ""}')
            if cursor:
                lines.append(f'                    "sequence_by": "{cursor}"')
            lines.append("                }")
            lines.append("            }")
            lines.append("        },")

        lines.append("")

    # Handle any modules not in the predefined order
    for module, entities in modules.items():
        if module in module_order:
            continue
        lines.append(f"        # {'=' * 65}")
        lines.append(f"        # Module: {module} ({len(entities)} entities)")
        lines.append(f"        # {'=' * 65}")

        for name, config in entities:
            pks = config.get("primary_keys", [])
            cursor = config.get("cursor_field")
            ing_type = config.get("ingestion_type", "cdc")
            scd_type = get_scd_type(ing_type)

            lines.append("        {")
            lines.append('            "table": {')
            lines.append(f'                "source_table": "{name}",')
            lines.append('                "table_configuration": {')
            lines.append(f'                    "scd_type": "{scd_type}",')
            lines.append(f'                    "primary_keys": \'{json.dumps(pks)}\'{"," if cursor else ""}')
            if cursor:
                lines.append(f'                    "sequence_by": "{cursor}"')
            lines.append("                }")
            lines.append("            }")
            lines.append("        },")

        lines.append("")

    lines.append("    ]")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("## Module Summary")
    lines.append("")
    lines.append("| Module | Entity Count |")
    lines.append("|--------|--------------|")
    for module in module_order:
        if module in modules:
            lines.append(f"| `{module}` | {len(modules[module])} |")
    for module in modules:
        if module not in module_order:
            lines.append(f"| `{module}` | {len(modules[module])} |")
    lines.append(f"| **Total** | **{len(registry)}** |")

    # Write to file
    project_root = Path(__file__).parent.parent.parent
    output_path = project_root / "sources" / "sap_successfactors" / "full_pipeline_spec.md"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Generated {output_path}")
    print(f"Total entities: {len(registry)}")

if __name__ == "__main__":
    generate_pipeline_spec()
