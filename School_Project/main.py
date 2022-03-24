from school_db import SchoolDB
from db import Connection


connection = Connection.Connector()
schoolDB = SchoolDB(connection)

projectFolder = '/home/alessandra-goncalves/Documents/Python/School_Project/'
inputTable = projectFolder + 'Old_Data_School.csv'
outputTable =  projectFolder + 'Data_School.csv'
tableDB = 'data_school'


schoolDB.filter(inputTable,'-', '', outputTable)
schoolDB.copy(tableDB, outputTable)
schoolDB.find(tableDB)