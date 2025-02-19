# test/test_main.py
import pytest
from main import run_operation  # or your method name

@pytest.mark.parametrize("a_str,b_str,op_str,expected_output", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number."),
])
def test_run_operation(a_str, b_str, op_str, expected_output, capsys):
    """Test the run_operation function for various inputs."""
    run_operation(a_str, b_str, op_str)
    captured = capsys.readouterr().out.strip()
    assert captured == expected_output