from models.editorial import Editorial
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class EditorialController:
    def __init__(self):
        self.editorial=Editorial()
        self.salir = False

   