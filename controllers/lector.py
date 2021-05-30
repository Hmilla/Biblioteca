from models.libro import Libro
from models.lector import Lector
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class LectorController:
    def __init__(self):
        self.lector = Lector()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Lectores
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_lectores()
                elif respuesta == 2:
                    self.search_lector()
                elif respuesta == 3:
                    self.insert_lector()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_lectores(self):
        try:
            print('''
            ==========================
                Listar Lectores
            ==========================
            ''')
            lectores = self.lector.get_lectores('"Id_lector"')
            print(print_table(lectores, ['Id_lector', 'Nombres', 'Documento', 'Telefono']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_lector(self):
        print('''
        ========================
            Buscar Lector
        ========================
        ''')
        try:
            id_lector = input_data("Ingrese el ID del lector >> ", "int")
            lector = self.lector.get_lector({
                '"Id_lector"': id_lector
            })
            print(print_table(lector, ['Id_lector', 'Nombres', 'Documento', 'Telefono']))

            if lector:
                if question('¿Deseas dar mantenimiento al lector?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_lector(id_lector)
                    elif respuesta == 2:
                        self.delete_lector(id_lector)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_lector(self):
        nombre = input_data('Ingrese el nombre completo del lector >> ')
        documento = input_data('Ingrese el documento del lector >> ')
        telefono = input_data('Ingrese el teléfono del lector >> ', 'int')
        self.lector.insert_lector({
            '"Nombres"': nombre,
            '"Documento"': documento,
            '"Telefono"': telefono
        })
        print('''
        ================================
            Nuevo lector agregado
        ================================
        ''')
        self.all_lectores()

    def update_lector(self, lector_id):
        nombre = input_data('Ingrese el nuevo nombre completo del lector >> ')
        documento = input_data('Ingrese el nuevo documento del lector >> ')
        telefono = input_data('Ingrese el nuevo teléfono del lector >> ', 'int')
        self.lector.update_lector({
            '"Id_lector"': lector_id
        }, {
            '"Nombres"': nombre,
            '"Documento"': documento,
            '"Telefono"': telefono
        })
        print('''
        ============================
            Lector Actualizado
        ============================
        ''')

    def delete_lector(self, lector_id):
        self.lector.delete_letcor({
            '"Id_lector"': lector_id
        })
        print('''
        =========================
            Lector Eliminado
        =========================
        ''')
