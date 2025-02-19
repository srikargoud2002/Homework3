# test/test_randomized.py
"""
Tests that use random data generation from conftest.py.
"""
from decimal import Decimal
import pytest

def test_random_operations(a, b, op_name, op_func, expected):
    """Test the randomly generated operations."""
    if expected == "ZeroDivisionError":
        with pytest.raises(Exception, match="zero|Zero"):
            op_func(a, b)
    elif expected == "Error":
        with pytest.raises(Exception):
            op_func(a, b)
    else:
        result = op_func(a, b)
        assert result == expected, (
            f"Operation {op_name} failed for {a} and {b}: "
            f"expected {expected}, got {result}"
        )