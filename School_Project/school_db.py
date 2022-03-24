import csv
import pandas as pd
import re


class SchoolDB:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def find(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM data_school;")
        result = cursor.fetchall()
        cursor.close()
        print(result)
        return result

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from school where id = %s", (id,))
        self.connection.commit()

    def insert(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO school (name) VALUES(%s)", (name,))
        self.connection.commit()
    
    def update(self, table):
        cursor = self.connection.cursor()
        cursor.execute("")
        self.connection.commit()

    def filter(self):
        text = open("/home/alessandra-goncalves/Documents/Python/School_Project/Old_Data_School.csv", "r")
        #text = ''.join([i for i in text]).replace("character to be replaced", "character to be replaced with")
        text = ''.join([i for i in text]).replace("-", "")
        #Replacing character from replaced text
        text1 = ''.join([i for i in text]).replace("-", "")
        x = open("/home/alessandra-goncalves/Documents/Python/School_Project/Data_School.csv","w")
        x.writelines(text1)
        x.close()


    def copy(self):
        cursor = self.connection.cursor()

        cursor.execute("COPY data_school (school_name, principal, email, phone, address1, tstreet) from '/home/alessandra-goncalves/Documents/Python/School_Project/Data_School.csv' with delimiter as ',' CSV HEADER;")

        self.connection.commit()
        