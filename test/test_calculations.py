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
