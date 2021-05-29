from models.autor import Autor
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class AutorController:
    def __init__(self):
        self.autor = Autor()
        self.salir = False


