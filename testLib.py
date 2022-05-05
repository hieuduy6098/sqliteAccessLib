from sqliteAccess import *

sqlite = sqliteAccess(dbName='generator_data_2022_1.db')
data = sqlite.getColumnNameTable('electrical')
print(data)