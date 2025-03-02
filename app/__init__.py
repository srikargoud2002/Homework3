from app.commands import CommandHandler
import pkgutil
import importlib
from app.commands import Command
import os
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.settings = {}
        self.load_environment()
        
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment(self):
        load_dotenv()  # Load environment variables from .env file
        self.settings = dict(os.environ)
        environment = self.get_environment_variable()
        logging.info("Environment variables loaded.")
        print(f"Environment loaded: {environment}")

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)


    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        
        logging.info(f"Loading plugins from {plugins_package}")
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                try:
                    logging.debug(f"Attempting to import plugin: {plugin_name}")
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    logging.info(f"Successfully imported plugin: {plugin_name}")
                    
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, Command) and item != Command:
                                if item_name == 'MenuCommand':
                                    logging.debug(f"Registering MenuCommand for plugin: {plugin_name}")
                                    self.command_handler.register_command(plugin_name, item(self.command_handler))
                                else:
                                    logging.debug(f"Registering command {item_name} for plugin: {plugin_name}")
                                    self.command_handler.register_command(plugin_name, item())
                                logging.info(f"Successfully registered command {item_name} for plugin: {plugin_name}")
                        except TypeError:
                            logging.debug(f"Skipping non-command item: {item_name} in plugin: {plugin_name}")
                            continue
                except Exception as e:
                    logging.error(f"Error loading plugin {plugin_name}: {str(e)}")
        
        logging.info("Finished loading plugins")


    def start(self):
        # Register commands
        self.load_plugins()
        
        logging.info("Application started")
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            logging.debug(f"User input: {user_input}")
            
            if user_input.lower() == 'exit':
                logging.info("Exit command received")
                self.command_handler.execute_command('exit')
                logging.info("Application exiting")
                break  
            
            # Handle commands with arguments like 'add 3 5'
            parts = user_input.split()
            command_name = parts[0]
            args = parts[1:]

            logging.debug(f"Parsed command: {command_name}, args: {args}")

            # Execute the command with arguments if needed
            if command_name in self.command_handler.commands:
                command = self.command_handler.commands[command_name]
                logging.info(f"Executing command: {command_name}")
                # If the command requires arguments
                if args:
                    logging.debug(f"Executing {command_name} with args: {args}")
                    command.execute(*args)
                else:
                    logging.debug(f"Executing {command_name} without args")
                    command.execute()
            else:
                logging.warning(f"Unknown command attempted: {command_name}")
                print(f"No such command: {command_name}")

        logging.info("Application shutdown complete")
