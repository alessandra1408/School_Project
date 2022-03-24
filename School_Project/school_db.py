import csv
from pathlib import Path
import pandas as pd
import re


class SchoolDB:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def find(self, tableBD):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM %s", (tableBD,))
        result = cursor.fetchall()
        cursor.close()
        print(result)
        return result

    def delete(self,tableBD, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from %s where id = %s", (tableBD, id,))
        self.connection.commit()

    def insert(self, tableBD, columns_table, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO %s (%s) VALUES(%s)", (tableBD, columns_table, name,))
        self.connection.commit()
    
    def update(self, table):
        #TO DO
        cursor = self.connection.cursor()
        cursor.execute("")
        self.connection.commit()

    def filter(self, input_table, old_characters, new_characters, output_table):
        inputFile = open(input_table, 'r')
        #inputFile = ''.join([i for i in inputFile]).replace("character to be replaced", "character to be replaced with")
        inputFile = ''.join([i for i in inputFile]).replace(old_characters, new_characters)
        #Replacing character from replaced text
        outputFile = ''.join([i for i in inputFile]).replace(old_characters, new_characters)
        x = open(output_table,'w')
        x.writelines(outputFile)
        x.close()


    def copy(self, tableDB, table_path, columns=''):
        cursor = self.connection.cursor()

        cursor.execute("COPY " + tableDB + columns + " from '" + table_path + "' with delimiter as ',' CSV HEADER;")

        self.connection.commit()
        