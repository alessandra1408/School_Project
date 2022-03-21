from school_db import SchoolDB
from db import Connection

connection = Connection.Connector()
schoolDB = SchoolDB(connection)

schoolDB.delete(7)
result = schoolDB.find()


for school in result:
    print(school[0], ": ", school[1])