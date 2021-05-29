from helpers.menu import Menu
from helpers.helper import input_data, print_table, question
from models.autor import Autor
from models.libro import Libro
from models.libro_autor import Libro_autor



class Libro_autorController:
    def __init__(self):
        self.libro = Libro()
        self.libro_autor = Libro_autor()
        self.autor = Autor()
        self.salir = False

    