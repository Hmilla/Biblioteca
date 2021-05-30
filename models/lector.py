from connection.conn import Connection


class Lector:
    def __init__(self):
        self.model = Connection('"Lector"')

    def get_lectores(self, order):
        return self.model.get_all(order)

    def get_lector(self, id_object):
        return self.model.get_by_id(id_object)

    def search_lector(self, data):
        return self.model.get_columns(data)

    def insert_lector(self, lector):
        return self.model.insert(lector)

    def update_lector(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_letcor(self, id_object):
        return self.model.delete(id_object)
