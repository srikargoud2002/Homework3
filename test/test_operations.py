"""Unit tests for individual arithmetic operations using OperationRecord."""
from decimal import Decimal
import pytest
from calculator.calculation import OperationRecord
from calculator.operations import add_numbers, sub_numbers, mul_numbers, div_numbers

def test_add_numbers():
    record = OperationRecord(Decimal('10'), Decimal('5'), add_numbers)
    assert record.execute() == Decimal('15'), "Addition failed"

def test_sub_numbers():
    record = OperationRecord(Decimal('10'), Decimal('5'), sub_numbers)
    assert record.execute() == Decimal('5'), "Subtraction failed"

def test_mul_numbers():
    record = OperationRecord(Decimal('10'), Decimal('5'), mul_numbers)
    assert record.execute() == Decimal('50'), "Multiplication failed"

def test_div_numbers():
    record = OperationRecord(Decimal('10'), Decimal('5'), div_numbers)
    assert record.execute() == Decimal('2'), "Division failed"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        record = OperationRecord(Decimal('10'), Decimal('0'), div_numbers)
        record.execute()
