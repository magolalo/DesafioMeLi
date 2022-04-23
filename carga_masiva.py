import sqlite3

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
