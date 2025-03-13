# History PlugIn

import logging
from app.commands import Command, Data
from app.strategies import HistoryMenuStrategy, MenuContext

class HistoryCommand(Command):
    def __init__(self):
        self.menu_context = MenuContext(HistoryMenuStrategy())

    def execute(self):
        logging.info("Showed history management options")
        Data.kill_it(self)
        self.menu_context.show_menu()