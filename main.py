import sys
from decimal import Decimal, InvalidOperation
from calculator import CalcEngine  # Make sure it points to your code

def run_operation(a_str, b_str, op_str):
    """Converts inputs to Decimal and executes the desired operation."""
    try:
        val_a = Decimal(a_str)
        val_b = Decimal(b_str)
    except InvalidOperation:
        print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
        return

    # Map the string to the actual CalcEngine methods
    operations_map = {
        'add': CalcEngine.sum_values,
        'subtract': CalcEngine.difference,
        'multiply': CalcEngine.product,
        'divide': CalcEngine.quotient,
    }

    if op_str not in operations_map:
        print(f"Unknown operation: {op_str}")
        return

    try:
        result = operations_map[op_str](val_a, val_b)
        print(f"The result of {a_str} {op_str} {b_str} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main entry point for the calculator CLI."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, first_num, second_num, operation_name = sys.argv
    run_operation(first_num, second_num, operation_name)

if __name__ == "__main__":
    main()