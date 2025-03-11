#App Class

import inspect
import os
import pkgutil
import importlib
from dotenv import load_dotenv
import logging
import logging.config
from app.commands import Commandlist, Command, Data
from app.plugins.history.viewHistory import ViewCommand
from app.plugins.history.back import BackCommand
from app.plugins.history.deleteHistory import DeleteCommand
from app.plugins.history.getlatest import LatestCommand


class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        Data
        Data.configure_data(self)
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_list = Commandlist()
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s')
        logging.info("Logging configured.")
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command):
                        if inspect.isabstract(item):
                            continue
                        self.command_list.register_command(plugin_name, item())

    def start(self):
        self.command_list.register_command("view history", ViewCommand())
        self.command_list.register_command("back", BackCommand())
        self.command_list.register_command("get latest", LatestCommand())
        self.command_list.register_command("delete history", DeleteCommand())
        self.load_plugins()

        print("Welcome to the Calculator! Enter an operation or type 'exit' to leave the program")
        while True:
            self.command_list.execute_command(input(">>> ").strip())