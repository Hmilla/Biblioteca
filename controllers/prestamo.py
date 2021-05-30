from helpers.menu import Menu
from helpers.helper import input_data, print_table, question
from models.libro import Libro
from models.lector import Lector
from models.prestamo import Prestamo
from models.editorial import Editorial
import datetime


class NotasController:
    def __init__(self):
        self.libro=Libro()
        self.lector=Lector()
        self.prestamo=Prestamo()
        self.editorial=Editorial()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                ===================
                    Prestamos
                ===================
                ''')
                lista_menu = ["Listar", "Buscar", "Registrar", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_prestamos()
                elif respuesta == 2:
                    self.search_prestamo()
                elif respuesta== 3:
                    self.insert_prestamo()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def all_prestamos(self):
        try:
            print('''
            ==========================
                Listar Prestamos
            ==========================
            ''')
            prestamos = self.prestamo.get_prestamos('"id_prestamo"')
            listas_prestamos=[]

            for prestamo in prestamos:
                id_lector = prestamo[4]
                lector = self.lector.get_lector({
                '"Id_lector"': id_lector
                })
                id_libro = prestamo[3]
                libro = self.libro.get_libro({
                '"Id_Libro"': id_libro
                })
                prestamo_1=list(prestamo)
                prestamo_1[4]=lector[1]
                prestamo_1[3]=libro[1]
                
                
                listas_prestamos.append(tuple(prestamo_1))

            print(print_table(listas_prestamos, ['Id_prestamo', 'Fecha de Entrega', 'Fecha de Devolucion', 'Libro','Lector','Estado']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def insert_prestamo(self):
        try:
            print('''
            ==========================
                Insertar Prestamo
            ==========================
            ''')
            disponible_libro=False
            id_libro = input_data("Ingrese el ID del libro prestado >> ", "int")
            libro = self.libro.get_libro({
                '"Id_Libro"': id_libro
                })
            editorial=self.editorial.get_editorial({
                '"id_Editorial"':libro[5]
            })
            lista_libro=list(libro)
            lista_libro[5]=editorial[1]
            lista_libro=tuple(lista_libro)
            print(print_table(lista_libro, ['Id libro', 'Nombre', 'Autor', 'Disponibilidad','Estado','Editorial']))
            
            lista_libro[3].upper
            if lista_libro[3]=="0" or lista_libro[3].upper()=="NO DISPONIBLE" or lista_libro[3]=="no disponible":
                print('Libro no disponible')
                print('No es posible registrar el préstamo')
            elif lista_libro[3].upper()=="INACTIVO" or lista_libro[3]=="inactivo":
                print('Libro inactivo')
                print('No es posible registrar el préstamo')
            else:
                disponible_libro=True
            if disponible_libro==True:
                id_lector = input_data("Ingrese el ID del lector >> ", "int")
                lector = self.lector.get_lector({
                    '"Id_lector"':id_lector
                })
                print(print_table(lector,['Id Lector','Nombres','Documento','Telefono']))
                entrega = datetime.datetime.utcnow()
                devolver = entrega + datetime.timedelta(days=15)
                estado="Por entregar"
                self.libro.update_libro({
                '"Id_Libro"': id_libro
                }, {
                '"Disponibilidad"':'0'
                })
                self.prestamo.insert_prestamo({
                    '"Fecha de Entrega"':entrega,
                    '"Fecha de Devolucion"':devolver,
                    '"fk_Libro"':id_libro,
                    '"fk_Lector"':id_lector,
                    '"Estado_prestamo"':estado


                })
                print(f'Se registró el prestamo, la fecha de devolución es en 15 días ({devolver})')
        except Exception as e:
            print (e)
    
    def search_prestamo(self):
        print('''
        ========================
            Buscar Prestamo
        ========================
        ''')
        try:
            id_prestamo = input_data("Ingrese el ID del prestamo >> ", "int")
            prestamo = self.prestamo.get_prestamo({
               '"id_prestamo"': id_prestamo
            })
            id_lector = prestamo[4]
            lector = self.lector.get_lector({
            '"Id_lector"': id_lector
            })
            id_libro = prestamo[3]
            libro = self.libro.get_libro({
            '"Id_Libro"': id_libro
            })
            prestamo_1=list(prestamo)
            prestamo_1[4]=lector[1]
            prestamo_1[3]=libro[1]
            
            prestamo_1=tuple(prestamo_1)
            print(print_table(prestamo_1, ['Id_prestamo', 'Fecha de Entrega', 'Fecha de Devolucion', 'Libro','Lector','Estado']))

            if prestamo:
                if question('¿Deseas dar mantenimiento al prestamo?'):
                    opciones = ['Confirmar entrega del libro', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.confirmar_entrega(id_prestamo,prestamo)
                    elif respuesta == 2:
                        self.delete_prestamo(id_prestamo)
        except Exception as e:
            print(f'{str(e)}')
            print("Error al tratar de acceder al prestamo, es probable que haya ingresado un id no existente")
        input('\nPresiona una tecla para continuar...')

    def confirmar_entrega(self,id_prestamo,prestamo):
        if prestamo[5]=="Por entregar":
            id_libro=prestamo[3]
            self.libro.update_libro({
                '"Id_Libro"': id_libro
                }, {
                '"Disponibilidad"':'1'
                })
            self.prestamo.update_prestamo({
                '"id_prestamo"': id_prestamo
                }, {
                '"Estado_prestamo"':'Entregado'
                })
            print('''
            =========================
              Se confirmo la entrega
            =========================
            ''')
            
            
        elif prestamo[5]=="Entregado":
            print("Este libro ya ha sido entregado")
    def delete_prestamo(self,id_prestamo):
        self.prestamo.delete_prestamo({
            '"id_prestamo"': id_prestamo
        })
        print('''
        =========================
            Prestamo Eliminado
        =========================
        ''')
        
        
    