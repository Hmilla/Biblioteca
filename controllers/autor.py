from models.autor import Autor
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class AutorController:
    def __init__(self):
        self.autor = Autor()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Autores
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Nuevo", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_autores()
                elif respuesta == 2:
                    self.search_autor()
                elif respuesta == 3:
                    self.insert_autor()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}') 

    def all_autores(self):
        try:
            print('''
            ==========================
                Listar Autor
            ==========================
            ''')
            autores = self.autor.get_autores('id_autor')
            print(print_table(autores, ['ID', 'Nombre']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_autor(self):
        print('''
        ========================
            Buscar Autor
        ========================
        ''')
        try:
            id_autor = input_data("Ingrese el ID del Autor >> ", "int")
            autor = self.autor.get_autor({
                'id_Autor': id_autor
            })
            print(print_table(autor, ['ID', 'Nombre']))

            if autor:
                if question('¿Deseas dar mantenimiento al autor?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_autor(id_autor)
                    elif respuesta == 2:
                        self.update_autor(id_autor)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def update_autor(self, id_autor):
        nombre = input_data('Ingrese el nuevo nombre del autor >> ')

        self.autor.update_autor({
            'id_Autor': id_autor
        }, {
            'Nombres': nombre
        })
        print('''
        ============================
            Autor Actualizado
        ============================
        ''')

    def insert_autor(self):
        nombre = input_data('Ingrese el nombre del autor >> ')
        self.autor.insert_autor({
            'Nombres': nombre
        })
        print('''
        ================================
            Nuevo autor agregado
        ================================
        ''')
        self.all_autores()   