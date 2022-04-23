import sqlite3

#Esta función es convocada por única vez al iniciar la app.
#Se conecta a la DB y crea la tabla "frecuencia"
#Se hace una carga masiva con la opción executemany ingresando como argumentos la sintaxis SQL y la tupla "datos"
#Devuelve la cantidad de filas insertadas en la DB.

def Carga(datos):
    conector = sqlite3.connect("mini.db")
    cursor = conector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS frecuencia (Id INTEGER PRIMARY KEY, palabra TEXT, cantidad INTEGER)")
    sql = 'INSERT INTO frecuencia (palabra, cantidad) VALUES(?,?)'
    cursor.executemany(sql, datos)
    conector.commit()
    filas = cursor.rowcount
    conector.close()
    return filas
