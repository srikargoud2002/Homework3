"""
Unit tests for OperationRecord class.
"""
from decimal import Decimal
import pytest
from calculator.calculation import OperationRecord
from calculator.operations import add_numbers, sub_numbers, mul_numbers, div_numbers

@pytest.mark.parametrize("x, y, operation, expected", [
    (Decimal('10'), Decimal('5'), add_numbers, Decimal('15')),
    (Decimal('10'), Decimal('5'), sub_numbers, Decimal('5')),
    (Decimal('10'), Decimal('5'), mul_numbers, Decimal('50')),
    (Decimal('10'), Decimal('2'), div_numbers, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add_numbers, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), sub_numbers, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), mul_numbers, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), div_numbers, Decimal('20')),
])
def test_operation_record_execution(x, y, operation, expected):
    record = OperationRecord(x, y, operation)
    assert record.execute() == expected, f"Failed {operation.__name__} with {x} and {y}"

def test_operation_record_repr():
    record = OperationRecord(Decimal('10'), Decimal('5'), add_numbers)
    expected_repr = "OperationRecord(10, 5, add_numbers)"
    assert record.__repr__() == expected_repr, "OperationRecord __repr__ output mismatch"

def test_division_by_zero():
    record = OperationRecord(Decimal('10'), Decimal('0'), div_numbers)
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        record.execute()
