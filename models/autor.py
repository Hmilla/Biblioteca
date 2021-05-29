from connection.conn import Connection


class Autor:
    def __init__(self):
        self.model = Connection('Autor')

    def get_autores(self, order):
        return self.model.get_all(order)

    def get_autor(self, id_object):
        return self.model.get_by_id(id_object)

    def search_autor(self, data):
        return self.model.get_columns(data)

    def insert_autor(self, autor):
        return self.model.insert(autor)

    def update_autor(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_autor(self, id_object):
        return self.model.delete(id_object)
