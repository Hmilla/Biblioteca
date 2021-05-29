from connection.conn import Connection


class Libro_autor:
    def __init__(self):
        self.model = Connection('Libro_Autor')

    def get_libro_autores(self, order):
        return self.model.get_all(order)

    def get_libro_autor(self, id_object):
        return self.model.get_by_id(id_object)

    def search_libro_autor(self, data):
        return self.model.get_columns(data)

    def insert_libro_autor(self, libro_Autor):
        return self.model.insert(libro_Autor)

    def update_libro_autor(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_libro_autor(self, id_object):
        return self.model.delete(id_object)
