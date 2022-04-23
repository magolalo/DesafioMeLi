import sqlite3

def ConsultoDatos (palabra):
    conector = sqlite3.connect("mini.db")
    cursor = conector.cursor()
    sql = "SELECT cantidad FROM frecuencia WHERE palabra = ?"
    cursor.execute(sql, (palabra,))
    filas = cursor.fetchone()
    conector.close()
    return filas
