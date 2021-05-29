from helpers.menu import Menu
from helpers.helper import input_data, print_table, question
from models.libro import Libro
from models.lector import Lector
from models.prestamo import Prestamo


class NotasController:
    def __init__(self):
        self.libro=Libro()
        self.lector=Lector()
        self.prestamo=Prestamo()
        self.salir = False

