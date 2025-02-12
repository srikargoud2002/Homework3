"""
Unit tests for OperationHistory class.
"""
from decimal import Decimal
import pytest
from calculator.calculations import OperationHistory
from calculator.calculation import OperationRecord
from calculator.operations import add_numbers

@pytest.fixture
def setup_records():
    OperationHistory.clear_records()
    OperationHistory.add_record(OperationRecord(Decimal("10"), Decimal("5"), add_numbers))
    OperationHistory.add_record(OperationRecord(Decimal("20"), Decimal("3"), add_numbers))

def test_add_record(setup_records):
    record = OperationRecord(Decimal("3"), Decimal("2"), add_numbers)
    OperationHistory.add_record(record)
    assert OperationHistory.get_last_record() == record, "Failed to add record to history"

def test_get_all_records(setup_records):
    records = OperationHistory.get_all_records()
    assert len(records) == 2, "Record count mismatch in history"

def test_clear_records(setup_records):
    OperationHistory.clear_records()
    assert len(OperationHistory.get_all_records()) == 0, "History was not cleared"

def test_get_last_record(setup_records):
    last = OperationHistory.get_last_record()
    assert last.x == Decimal("20") and last.y == Decimal("3"), "Incorrect last record"

def test_get_last_record_empty():
    OperationHistory.clear_records()
    assert OperationHistory.get_last_record() is None, "Expected None for last record when history is empty"

def test_operation_history_full_flow():
    from decimal import Decimal
    from calculator.calculation import OperationRecord
    from calculator.operations import add_numbers

    # Clear any existing records.
    from calculator.calculations import OperationHistory
    OperationHistory.clear_records()

    # When empty, get_all_records should return an empty list and get_last_record should return None.
    assert OperationHistory.get_all_records() == [], "Expected empty record list after clear."
    assert OperationHistory.get_last_record() is None, "Expected None as last record when history is empty."

    # Add a record.
    record1 = OperationRecord(Decimal('1'), Decimal('2'), add_numbers)
    OperationHistory.add_record(record1)
    # Now, get_all_records should have one record and get_last_record should return it.
    assert OperationHistory.get_all_records() == [record1], "Record list should contain the added record."
    assert OperationHistory.get_last_record() == record1, "Last record should be the one that was added."

    # Add another record.
    record2 = OperationRecord(Decimal('3'), Decimal('4'), add_numbers)
    OperationHistory.add_record(record2)
    # Now, get_all_records should have both records, and get_last_record should be the new one.
    assert OperationHistory.get_all_records() == [record1, record2], "Record list should contain both records."
    assert OperationHistory.get_last_record() == record2, "Last record should be the most recently added record."

    # Finally, clear the records and check again.
    OperationHistory.clear_records()
    assert OperationHistory.get_all_records() == [], "Record list should be empty after clear."
    assert OperationHistory.get_last_record() is None, "Expected None as last record after clearing history."

def test_operation_history_complete_branches():
    from decimal import Decimal
    from calculator.calculations import OperationHistory
    from calculator.calculation import OperationRecord
    from calculator.operations import add_numbers

    # Ensure history is clear.
    OperationHistory.clear_records()
    # When empty:
    assert OperationHistory.get_all_records() == [], "Expected empty history."
    assert OperationHistory.get_last_record() is None, "Expected None for last record when history is empty."

    # Add first record.
    record1 = OperationRecord(Decimal('1'), Decimal('2'), add_numbers)
    OperationHistory.add_record(record1)
    # Verify get_all_records and get_last_record when there is one record.
    all_records = OperationHistory.get_all_records()
    assert all_records == [record1], "History should contain the first record."
    assert OperationHistory.get_last_record() == record1, "Last record should be the first record."

    # Add second record.
    record2 = OperationRecord(Decimal('3'), Decimal('4'), add_numbers)
    OperationHistory.add_record(record2)
    all_records = OperationHistory.get_all_records()
    assert all_records == [record1, record2], "History should contain both records."
    assert OperationHistory.get_last_record() == record2, "Last record should now be the second record."

    # Finally, clear the records.
    OperationHistory.clear_records()
    assert OperationHistory.get_all_records() == [], "History should be empty after clearing."
    assert OperationHistory.get_last_record() is None, "Last record should be None after clearing."
