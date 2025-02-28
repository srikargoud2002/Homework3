from app.commands import CommandHandler
import pkgutil
import importlib
from app.commands import Command
import os
from dotenv import load_dotenv


class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_environment()


    def load_environment(self):
        load_dotenv()  
        self.environment = os.getenv('ENVIRONMENT', 'production')
        print(f"Running in {self.environment} environment")


    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item != Command:
                            # Pass command_handler to MenuCommand
                            if item_name == 'MenuCommand':  # Check if it's the MenuCommand class
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else:
                                self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        # Register commands
        self.load_plugins()

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
