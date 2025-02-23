import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        # List of available commands (you can add more commands dynamically here)
        commands = [
            "greet",       # Greeting command
            "goodbye",     # Goodbye command
            "menu",        # Show menu command
            "add <num1> <num2>",         # Add command
            "subtract <num1> <num2>",    # Subtract command
            "multiply <num1> <num2>",    # Multiply command
            "divide <num1> <num2>",
                "exit",       # Divide command
        ]
        
        # Print the available commands
        print("Available commands:")
        for command in commands:
            print(f"- {command}")