from models.lector import Lector
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class LectorController:
    def __init__(self):
        self.lector = Lector()
        self.salir = False

    