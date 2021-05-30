from models.libro import Libro
from models.editorial import Editorial
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question
from connection.conn import Connection

class LibroController:
    def __init__(self):
        self.libro = Libro()
        self.editorial = Editorial()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ==========================
                    Registro de Libros
                ==========================
                ''')
                lista_menu = ["Listar Libros", "Buscar Libros","Registrar Libros", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.name_complete()
                elif respuesta == 2:
                    self.buscar_libro()
                elif respuesta == 3:
                    self.create_libro()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def all_libros(self):
        try:
            print('''
            ==========================
                Listar Libros
            ==========================
            ''')
            libros = self.libro.get_libros('id_libro')
            print(print_table(libros, ['ID', 'Nombre', 'Autor', 'Disponibilidad','Estado de Libro', 'Editorial']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def buscar_libro(self):
        print('''
        ========================
            Buscar Libro
        ========================
        ''')
        try:
            id_libro = input_data("Ingrese el ID del libro >> ")
            libro = self.libro.get_libro({
                'id_libro': id_libro
            })
            
            print(print_table(libro, ['ID', 'Nombre', 'Autor', 'Disponibilidad','Estado de Libro', 'Editorial']))
            
            if libro:
                if question('¿Deseas dar mantenimiento al libro?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_libro(id_libro)
                    elif respuesta == 2:
                        self.delete_libro(id_libro)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def create_libro(self):

        print('Lista de Editoriales')
        editorial = self.editorial.get_editoriales('id_editorial')
        print(print_table(editorial, ['ID', 'Nombre']))


        
        nombre = input_data('\nIngrese el nombre del libro >> ')
        autor = input_data('Ingrese el nombre del autor >> ')
        disponibilidad = input_data('Ingrese la disponibilidad del libro  >> ')
        estado_libro = input_data('Ingrese el estado del libro >> ')
        editorial_id = input_data('Escriba el ID de la editorial >> ')
        self.libro.insert_libro({
            'nombre': nombre,
            'autor': autor,
            'disponibilidad': disponibilidad,
            'estado_libro': estado_libro,
            'fk_editorial': editorial_id
        })
        print('''
        ================================
            Nuevo Libro agregado
        ================================
        ''')

        self.name_complete()

    def update_libro(self, id_libro):
        print('¿Qué dato desea editar?')
        try:
   
            opciones = ['Nombre', 'Autor', 'Disponibilidad','Estado de Libro', 'Editorial']
            respuesta = Menu(opciones).show()
            if respuesta == 1:
                self.update_nombre(id_libro)
            elif respuesta == 2:
                self.update_autor(id_libro)
            elif respuesta == 3:
                self.update_disponibilidad(id_libro)
            elif respuesta == 4:
                self.update_estado(id_libro)
            elif respuesta == 5:
                self.update_editorial(id_libro)  
        except Exception as e:
            print(f'{str(e)}')

    def update_nombre(self,id_libro):

        nombre = input_data('Ingrese el nuevo nombre del libro >> ')
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'nombre': nombre,
        })
        print('''
        ============================
            Nombre Actualizado
        ============================
        ''')

    def update_autor(self,id_libro):

        autor = input_data('Ingrese el nuevo nombre del libro >> ')
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'autor': autor,
        })
        print('''
        ============================
            Autor Actualizado
        ============================
        ''')
    
    def update_disponibilidad(self,id_libro):

        disponibilidad = input_data('Ingrese la disponibilidad del libro >> ')
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'disponibilidad': disponibilidad,
        })
        print('''
        ============================
            Disponibilidad Actualizado
        ============================
        ''')
    
    def update_estado(self,id_libro):

        estado = input_data('Ingrese elestado del libro >> ')
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'estado_libro': estado,
        })
        print('''
        ============================
            Estado Actualizado
        ============================
        ''')

    def update_editorial(self,id_libro):

        print('Lista de Editoriales')
        editoriales = self.editorial.get_editoriales('id_editorial')
        print(print_table(editoriales, ['ID', 'Nombre']))
        id_editorial = input_data('\nEscriba el ID de la Editorial >> ')
        
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'fk_editorial': id_editorial,
        })
        print('''
        ============================
            Editorial Actualizado
        ============================
        ''')

    def delete_libro(self, id_libro):
        self.libro.delete_libro({
            'id_libro': id_libro

        })
        print('''
        =========================
            Libro Eliminado
        =========================

        ''')


    def name_complete(self):

        try:
            conn = Connection('libro')
            query = '''
                SELECT l.id_libro, l.nombre , 
                l.autor, l.disponibilidad,
                l.estado_libro,e.nombre as Nombre_Editorial
                FROM public.libro l , editorial e
                WHERE l.id_libro = e.id_editorial;
            '''
            cursor =conn.execute_query(query)
            editoriales = cursor.fetchall()
            self.editorial.get_editoriales('id_editorial')
            print(print_table(editoriales, ['ID', 'Nombre', 'Autor', 'Disponibilidad','Estado de Libro', 'Editorial']))
        except Exception as e:
            print(f'{str(e)}')



    """ for editorial in editoriales:
                print('---------------------------')
                print(f'\nID: {editorial[0]}')
                print(f'Nombres del libro: {editorial[1]}')
                print(f'Nombres del autor: {editorial[2]}')
                print(f'Disponibilidad del libro: {editorial[3]}')
                print(f'Estado del libro: {editorial[4]}')
                print(f'Editorial del libro: {editorial[5]}')
                print('----------------------------------') """
    """ def asignacion_editorial(self,libro,id_libro):

        print(f'\n Asignación de editoriales para el libro : {libro[1]}')
        print('''
        =================================
             Editoriales Disponibles
        =================================
        ''')

        editoriales = self.editorial.get_editoriales('id_editorial')
        editoriales_disponibles = []
        if editoriales:
            for editorial in editoriales:
                id_libro = editorial[0]
                nombre = editorial[1]
                editorial_libro = self.libro.search_libro({
                    'id_libro': id_libro,
                    'nombre': nombre
                })
                if not editorial_libro:
                    editoriales_disponibles.append({
                        'ID':id_libro,
                        'editorial':nombre
                    })
        print(print_table(editoriales_disponibles))
        editorial_elegido = input_data(f'\nIngrese el ID de la editorial a asignar >> ')
        buscar_editorial = self.editorial.get_editorial({'curso_id': editorial_elegido})
        if not buscar_editorial:
            print('\nEste curso no existe !')
            return


        editorial_libro = self.libro.search_libro({
            'id_libro': id_libro,
            'id_editorial':editorial_elegido
        })

        if editorial_libro:
            print(f'\nEsta editorial ya se asigno a la editorial {editorial[1]}')
            return

        self.libro.insert_libro({
            'id_libro': id_libro,
            'id_editorial': editorial_elegido
        })
        print('''
        ========================
            Editorial Asignado
        ========================
        ''') """