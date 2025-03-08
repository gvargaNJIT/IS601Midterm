#App Class

import pkgutil
import importlib
from app.commands import Commandlist, Command

class App:
    def __init__(self):
        self.command_list = Commandlist()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.','/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_list.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        self.load_plugins()

        print("Welcome to the Calculator! Enter an operation or type 'exit' to leave the program")
        while True:
            self.command_list.execute_command(input(">>> ").strip())