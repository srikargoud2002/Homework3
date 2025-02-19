# test/conftest.py
import pytest
from faker import Faker
from decimal import Decimal
import random
from calculator import CalcEngine  # or from your code that has sum_values, etc.

faker_gen = Faker()

def pytest_addoption(parser):
    """Add a custom command-line option for specifying the number of records."""
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to auto-generate for calculator tests"
    )

def random_operation_func():
    """Randomly select one of the operations from CalcEngine."""
    operations = {
        "add": CalcEngine.sum_values,
        "subtract": CalcEngine.difference,
        "multiply": CalcEngine.product,
        "divide": CalcEngine.quotient,
    }
    op_name = random.choice(list(operations.keys()))
    return op_name, operations[op_name]

def generate_test_records(num):
    """
    Yield tuples of (a, b, operation_name, operation_func, expected_result or None if error).
    We'll handle division by zero as a special case.
    """
    for _ in range(num):
        a_dec = Decimal(faker_gen.random_number(digits=2))
        b_dec = Decimal(faker_gen.random_number(digits=2))

        op_str, op_func = random_operation_func()

        # Handle zero division if the chosen op is 'divide' and b == 0
        if op_str == "divide" and b_dec == 0:
            yield (a_dec, b_dec, op_str, op_func, "ZeroDivisionError")
        else:
            # Compute expected result safely (catch if dividing by zero)
            try:
                result = op_func(a_dec, b_dec)
                yield (a_dec, b_dec, op_str, op_func, result)
            except Exception:
                # If any error is raised, set expected to a string
                yield (a_dec, b_dec, op_str, op_func, "Error")

def pytest_generate_tests(metafunc):
    """
    Parametrize tests with generated data if the test function needs a,b,operation,expected.
    """
    if {"a", "b", "op_name", "op_func", "expected"}.issubset(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        test_data = list(generate_test_records(num_records))
        metafunc.parametrize("a,b,op_name,op_func,expected", test_data)