

from multiprocessing import connection


class SchoolDB:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def find(self):
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM school;")
        result = cursor.fetchall()
        cursor.close()
        
        return result

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from school where id = %s", (id,))
        self.connection.commit()

    def insert(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO school (name) VALUES(%s)", (name,))
        self.connection.commit()
    