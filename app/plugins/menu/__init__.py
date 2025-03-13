#Menu Plug-In

import logging
from app.commands import Command, Data
from app.strategies import MainMenuStrategy, MenuContext
    
class MenuCommand(Command):
    def __init__(self):
        self.menu_context = MenuContext(MainMenuStrategy())

    def execute(self):
        Data.kill_it(self)
        logging.info("Showed user menu options for the program")
        self.menu_context.show_menu()