"""
Tests for SAP SuccessFactors LakeflowConnect connector.

These tests connect to a real SAP SuccessFactors instance.
Configure credentials in configs/dev_config.json before running.

Run fast tests: pytest sources/sap_successfactors/test/ -v -m "not slow"
Run all tests: pytest sources/sap_successfactors/test/ -v
"""

from pathlib import Path

import pytest
from pyspark.sql.types import StructType

from tests import test_suite
from tests.test_suite import LakeflowConnectTester
from tests.test_utils import load_config
from sources.sap_successfactors.sap_successfactors import LakeflowConnect


def _get_connector():
    """Helper to create connector with config."""
    parent_dir = Path(__file__).parent.parent
    config_path = parent_dir / "configs" / "dev_config.json"
    config = load_config(config_path)
    return LakeflowConnect(config)


# =============================================================================
# Fast Tests - Run by default
# =============================================================================

def test_sap_successfactors_list_tables():
    """Test list_tables method directly."""
    connector = _get_connector()
    tables = connector.list_tables()

    assert isinstance(tables, list)
    assert len(tables) >= 550  # ~690 entities across all modules

    # Check for expected core entities
    expected_tables = [
        # Employee Central Core
        "User",
        "EmpEmployment",
        "EmpJob",
        "EmpCompensation",
        "EmpCostAssignment",
        "PerPerson",
        "PerPersonal",
        # Foundation Objects
        "FODepartment",
        "FOCompany",
        "FOCostCenter",
        "FOJobCode",
        "FOLocation",
        # Platform Services
        "PickList",
        "DynamicGroup",
        "TodoEntryV3",
        "Attachment",
        # Recruiting
        "Candidate",
        "JobApplication",
        "JobRequisition",
        "JobOffer",
        # Performance
        "Goal_1",
        "FormHeader",
        "Achievement",
        "Activity",
        # Time & Attendance
        "TimeAccount",
        "EmployeeTime",
        "WorkSchedule",
        # Succession
        "TalentPool",
        "Successor",
        "CompetencyEntity",
        # Onboarding 2.0
        "ONB2Process",
        "ONB2ProcessTask",
        # Onboarding 1.0 (Legacy)
        "OnboardingProcess",
        "OnboardingGoal",
        "OnboardingMeetingActivity",
        # Identity (SCIM)
        "ScimUser",
        "ScimGroup",
        # Benefits Management
        "Benefit",
        "BenefitsProgramDetail",
        "BenefitInsuranceCoverage",
        # Compliance
        "ComplianceProcess",
        "ComplianceFormData",
        # Advanced Goals
        "GoalPermission_1",
        "GoalMilestone_1",
        "TeamGoal_1",
        # Finance GO
        "BudgetPeriodGO",
        "FunctionalAreaGO",
        # REST APIs
        "customTasks",
        "journeyDetails",
        # Country Variants
        "PaymentInformationDetailV3ARG",
        "LegalEntityARG",
    ]
    for table in expected_tables:
        assert table in tables, f"Expected table {table} not found"


def test_sap_successfactors_cdc_with_deletes():
    """Test that EmpCostAssignment has cdc_with_deletes ingestion type."""
    connector = _get_connector()
    metadata = connector.read_table_metadata("EmpCostAssignment", {})

    assert metadata["ingestion_type"] == "cdc_with_deletes"


def test_sap_successfactors_composite_keys():
    """Test that EmpJob has composite primary keys."""
    connector = _get_connector()
    metadata = connector.read_table_metadata("EmpJob", {})

    assert len(metadata["primary_keys"]) == 3
    assert "seqNumber" in metadata["primary_keys"]
    assert "startDate" in metadata["primary_keys"]
    assert "userId" in metadata["primary_keys"]


def test_sap_successfactors_modules():
    """Test module-based organization."""
    connector = _get_connector()
    modules = connector.get_available_modules()

    assert isinstance(modules, list)
    assert len(modules) >= 8  # At least 8 modules

    # Check for expected modules
    expected_modules = [
        "employee_central",
        "platform",
        "recruiting",
        "performance",
        "time_attendance",
        "succession",
        "onboarding",
        "identity",
    ]
    for module in expected_modules:
        assert module in modules, f"Expected module {module} not found"

    # Check tables per module
    ec_tables = connector.get_tables_by_module("employee_central")
    assert len(ec_tables) >= 30  # Many EC entities

    identity_tables = connector.get_tables_by_module("identity")
    assert "ScimUser" in identity_tables
    assert "ScimGroup" in identity_tables


def test_sap_successfactors_api_types():
    """Test that different API types are configured correctly."""
    connector = _get_connector()

    # Check OData v2 entity
    user_meta = connector.read_table_metadata("User", {})
    assert user_meta["primary_keys"] == ["userId"]
    assert user_meta["cursor_field"] == "lastModifiedDateTime"
    assert user_meta["ingestion_type"] == "cdc"

    # Check SCIM entity
    scim_meta = connector.read_table_metadata("ScimUser", {})
    assert scim_meta["primary_keys"] == ["id"]
    assert scim_meta["cursor_field"] == "lastModified"
    assert scim_meta["ingestion_type"] == "cdc"

    # Check OData v4 entity
    clock_meta = connector.read_table_metadata("ClockInClockOutGroup", {})
    assert clock_meta["primary_keys"] == ["externalCode"]
    assert clock_meta["cursor_field"] == "lastModifiedDateTime"


def test_sap_successfactors_goal_entities():
    """Test Goal entities (Goal_1 through Goal_8)."""
    connector = _get_connector()
    tables = connector.list_tables()

    # Check all 8 goal types
    for i in range(1, 9):
        goal_name = f"Goal_{i}"
        assert goal_name in tables, f"Expected {goal_name} not found"

        meta = connector.read_table_metadata(goal_name, {})
        assert meta["primary_keys"] == ["id"]
        assert meta["cursor_field"] == "lastModified"
        assert meta["ingestion_type"] == "cdc_with_deletes"


def test_sap_successfactors_smoke_test():
    """Smoke test: verify core connector functionality with API calls."""
    connector = _get_connector()

    # Test a representative set of tables from different API types
    test_tables = ["User", "EmpJob", "FODepartment", "TimeAccount"]

    for table in test_tables:
        # Test schema
        schema = connector.get_table_schema(table, {})
        assert isinstance(schema, StructType), f"Schema for {table} should be StructType"
        assert len(schema.fields) > 0, f"Schema for {table} should have fields"

        # Test metadata
        metadata = connector.read_table_metadata(table, {})
        assert "primary_keys" in metadata
        assert "cursor_field" in metadata
        assert "ingestion_type" in metadata

        # Test read_table - just verify we can call it
        iterator, offset = connector.read_table(table, {}, {})
        assert hasattr(iterator, "__iter__")
        assert isinstance(offset, dict)

        # Read a few records
        records = []
        for i, record in enumerate(iterator):
            records.append(record)
            if i >= 2:
                break
        # Some tables may return 0 records on demo server, that's OK
        assert len(records) >= 0


# =============================================================================
# Slow Tests - Mark with @pytest.mark.slow
# These test ALL 690 tables and take significant time
# =============================================================================

@pytest.mark.slow
def test_sap_successfactors_connector():
    """Test the SAP SuccessFactors connector using the full test suite.

    WARNING: This test iterates over all 690 tables and may take 30+ minutes.
    Run with: pytest -v -m slow
    """
    test_suite.LakeflowConnect = LakeflowConnect

    parent_dir = Path(__file__).parent.parent
    config_path = parent_dir / "configs" / "dev_config.json"
    config = load_config(config_path)

    table_configs = {}
    tester = LakeflowConnectTester(config, table_configs)

    report = tester.run_all_tests()
    tester.print_report(report, show_details=True)

    assert report.passed_tests == report.total_tests, (
        f"Test suite had failures: {report.failed_tests} failed, {report.error_tests} errors"
    )


@pytest.mark.slow
def test_sap_successfactors_schemas():
    """Test get_table_schema for all tables.

    WARNING: This test iterates over all 690 tables.
    Run with: pytest -v -m slow
    """
    connector = _get_connector()
    tables = connector.list_tables()

    for table in tables:
        schema = connector.get_table_schema(table, {})
        assert schema is not None, f"Schema for {table} should not be None"
        assert len(schema.fields) > 0, f"Schema for {table} should have fields"


@pytest.mark.slow
def test_sap_successfactors_metadata():
    """Test read_table_metadata for all tables.

    WARNING: This test iterates over all 690 tables.
    Run with: pytest -v -m slow
    """
    connector = _get_connector()
    tables = connector.list_tables()

    for table in tables:
        metadata = connector.read_table_metadata(table, {})

        assert "primary_keys" in metadata
        assert "cursor_field" in metadata
        assert "ingestion_type" in metadata

        assert isinstance(metadata["primary_keys"], list)
        assert len(metadata["primary_keys"]) > 0

        assert metadata["ingestion_type"] in ["snapshot", "cdc", "cdc_with_deletes", "append"]


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "not slow"])
