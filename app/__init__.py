from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                self.command_handler.execute_command('exit')
                break  
            
            # Handle commands with arguments like 'add 3 5'
            parts = user_input.split()
            command_name = parts[0]
            args = parts[1:]

            # Execute the command with arguments if needed
            if command_name in self.command_handler.commands:
                command = self.command_handler.commands[command_name]
                # If the command requires arguments
                if args:
                    command.execute(*args)
                else:
                    command.execute()
            else:
                print(f"No such command: unknown_command")
