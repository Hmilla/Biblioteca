from models.editorial import Editorial
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question


class EditorialController:
    def __init__(self):
        self.editorial=Editorial()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Editorial
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_editorial()
                elif respuesta == 2:
                    self.buscar_editorial()
                elif respuesta == 3:
                    self.create_editorial()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')


    def all_editorial(self):
        try:
            print('''
            ==========================
                Listar Editorial
            ==========================
            ''')
            editorial = self.editorial.get_editoriales('id_editorial')
            print(print_table(editorial, ['ID', 'Nombre']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def buscar_editorial(self):
        print('''
        ========================
            Buscar Editorial
        ========================
        ''')
        try:
            editorial_id = input_data("Ingrese el ID de la editorial >> ")
            editorial = self.editorial.get_editorial({
                'id_editorial': editorial_id
            })
            print(print_table(editorial, ['ID', 'Nombre']))

            if editorial:
                if question('¿Deseas dar mantenimiento a la editorial?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_editorial(editorial_id)
                    elif respuesta == 2:
                        self.delete_editorial(editorial_id)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def create_editorial(self):
        nombre = input_data('Ingrese el nombre de la editorial >> ')
        self.editorial.insert_editorial({
            'Nombre': nombre
        })
        print('''
        ================================
            Nueva Editorial Agregada
        ================================
        ''')
        self.all_editorial()
    
    def update_editorial(self, id_Editorial):
        nombre = input_data('Ingrese el nuevo nombre de la editorial >> ')
        self.editorial.update_editorial({
            'id_Editorial': id_Editorial
        }, {
            'nombre': nombre,
        })
        print('''
        ============================
            Editorial Actualizado
        ============================
        ''')
    def delete_editorial(self, id_Editorial):
        self.editorial.delete_editorial({
            'id_Editorial': id_Editorial

        })
        print('''
        =========================
            Editorial Eliminado
        =========================
        ''')

