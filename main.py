from helpers.menu import Menu
from controllers.autor import AutorController
from controllers.editorial import EditorialController
from controllers.lector import LectorController
from controllers.libro import LibroController
from controllers.prestamo import NotasController


def app():
    try:
        print('''
        ==========================
            Sistema de Biblioteca
        ==========================
        ''')
        menu_principal = ["Lectores", "Realizar Prestamo", "Libros", "Autores", "Editoriales", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            lector = LectorController()
            lector.menu()
            if lector.salir:
                app()
        elif respuesta == 2:
            prestamo = PrestamoController()
            prestamo.menu()
            if prestamo.salir:
                app()
        elif respuesta == 3:
            libro = LibroController()
            libro.menu()
            if libro.salir:
                app()
        elif respuesta == 4:
            autor = AutorController()
            autor.menu()
            if autor.salir:
                app()
        elif respuesta == 5:
            editorial = EditorialController()
            editorial.menu()
            if editorial.salir:
                app()

        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()