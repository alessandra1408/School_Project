import psycopg2


class Connection:
    def Connector():
        DB_HOST = "localhost"
        DB_NAME = "postgres"
        DB_USER = "postgres"
        DB_PASS = "12345678"

        connection = psycopg2.connect(dbname = DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

        return connection



