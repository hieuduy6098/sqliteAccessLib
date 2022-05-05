import sqlite3
# create class with sqlite
class sqliteAccess:
    def __init__(self, dbName):
        self.dbName = dbName
    
    # connect database file (.db)
    def connectDb(self):
        try:
            connect = sqlite3.connect(self.dbName)
            return connect
        except sqlite3.Error as error:
            print("Error connect to db: ", error)
        
    # get table name from database
    def getTableName(self):
        try:
            connect = self.connectDb()
            sql = "SELECT name FROM sqlite_master WHERE type='table'"
            cursor = connect.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            list = []
            for i in result:
                list.append(i[0])
            return list
        except sqlite3.Error as error:
            print("Error get table name from db: ", error)
        finally:
            connect.close()
            
    # get all data from table
    def getAllDataTable(self, tableName):
        try:
            connect = self.connectDb()
            sql = 'select * from ' + tableName
            cursor = connect.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as error:
            print("Error get data from table: ", error)
        finally:
            connect.close()

    # get column name from table
    def getColumnNameTable(self, tableName):
        try:
            connect = self.connectDb()
            sql = 'select * from ' + tableName
            cursor = connect.cursor()
            cursor.execute(sql)
            result = cursor.description
            list = []
            for i in result:
                list.append(i[0])
            return list
        except sqlite3.Error as error:
            print('error to get column from table: ', error)
        finally:
            connect.close()

    # get id name of table 
    def getIdNameFromTable(self, tableName):
        try:
            connect = self.connectDb()
            sql = 'select distinct id from ' + tableName
            cursor = connect.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            list = []
            for i in result:
                list.append(i[0])
            return list
        except sqlite3.Error as error:
            print("Error get id name from table: ", error)
        finally:
            connect.close()
    
    # get data of table by id column ex: g01eleia ...  
    def getDataById(self, tableName, idName):
        try:
            connect = self.connectDb()
            sql = "select * from " + tableName + " where id = '" + idName + "'"
            # select * from electrical where id = 'g01eleia' 
            cursor = connect.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
            
        except sqlite3.Error as error:
            print("Error get data from table by id: ", error)
        finally:
            connect.close()