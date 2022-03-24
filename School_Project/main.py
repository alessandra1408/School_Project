from school_db import SchoolDB
from db import Connection


connection = Connection.Connector()
schoolDB = SchoolDB(connection)

#['school_name,principal,email,phone,address1,tstreet']


schoolDB.filter()
schoolDB.copy()
result = schoolDB.find()


for school in result:
    print(school[0], ": ", school[1])