from models.libro import Libro
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class LibroController:
    def __init__(self):
        self.libro = Libro()
        self.salir = False

