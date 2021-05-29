from connection.conn import Connection


class Editorial:
    def __init__(self):
        self.model = Connection('Editorial')

    def get_editoriales(self, order):
        return self.model.get_all(order)

    def get_editorial(self, id_object):
        return self.model.get_by_id(id_object)

    def search_editorial(self, data):
        return self.model.get_columns(data)

    def insert_editorial(self, editorial):
        return self.model.insert(editorial)

    def update_editorial(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_editorial(self, id_object):
        return self.model.delete(id_object)
