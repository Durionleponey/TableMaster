import sqlite3


class tableMaster_dbConnexion:
    def __init__(self,dbname="TableMaster.db"):
        self.connexion = sqlite3.connect(dbname)
        self.cursor = self.connexion.cursor()



    def retreaveSingleData(self, table, columForValueToFind, columForKeyToFind, keyToFind, printSQL=False):
        sqlRequest = f'SELECT {columForValueToFind} FROM {table} WHERE {columForKeyToFind} = "{keyToFind}"'
        if printSQL == True:
            print(sqlRequest)
        self.cursor.execute(sqlRequest)
        return (self.cursor.fetchone())[0]

    def retreaveTable (self, table, printSQL=False):
        sqlRequest = f'SELECT * FROM {table}'
        if printSQL == True:
            print(sqlRequest)
        self.cursor.execute(sqlRequest)
        return (self.cursor.fetchall())

    def updateValue(self, table, columForValueToChange, columForKeyToFind, keyToFind, updatedValue, printSQL=False):
        sqlRequest = f'UPDATE {table} SET {columForValueToChange} = "{updatedValue}" WHERE {columForKeyToFind} = "{keyToFind}"'
        if printSQL == True:
            print(sqlRequest)
        self.cursor.execute(sqlRequest)
        self.connexion.commit()
        return ("done")

    def rowSQLrequest(self, SQL, printSQL=False):
        if printSQL == True:
            print(SQL)
        self.cursor.execute(SQL)
        self.connexion.commit()


    def close(self):
        self.connexion.close()



# db = tableMaster_dbConnexion()
# db.updateValue("settings","param_value","param_key","WorkingAreaColor","orange",True)
#
# backgroundColor = (db.retreaveSingleData("settings", "param_value", "param_key","WorkingAreaColor",True))
# db.close()
# print(backgroundColor)


db = tableMaster_dbConnexion()
print(db.retreaveTable("labels" ,True))