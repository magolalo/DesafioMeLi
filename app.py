from flask import Flask, jsonify
from consulta import ConsultoDatos
from bibliotecario import Buscador
from proc_archivos import crear_base
from Readme import readme
import os

app=Flask(__name__)

#Por única vez, al iniciar la app se procesan todos los .txt y se carga la DB. 
if not os.path.isfile('mini.db'): 
    crear_base()

#URL del proyecto
@app.route("/", methods=["GET"])
def index():
    inicio = ('<html><h2>Click <a href="https://github.com/magolalo/DesafioMeLi">aquí</a> para comenzar.</h2></html>')
    return inicio

#Ruta 1: Recibe el término que se desea cosultar como parte de la URL en <palabra> y
#se dispara la búsqueda en la DB. Devuelve la cantidad de repeticiones del término. 
@app.route("/<palabra>", methods=["GET"])
def busquemos(palabra): 
    cantidad = ConsultoDatos(palabra)
    if cantidad: 
        return jsonify({'cantidad':cantidad[0]})
    else:
        return jsonify({'cantidad':'NOT FOUND'})

#Ruta 2: Recibe el término que se desea cosultar como parte de la URL en <palabra> y
#se dispara la búsqueda directamente en los txt. Devuelve el nombre de los archivos
#donde se encontró la palabra y la cantidad de repeticiones del término.
@app.route('/archivos/<palabra>', methods=["GET"])
def fichero(palabra):
    ficheros = Buscador(palabra)
    if ficheros:
        txts = []
        veces = 0
        archivos = 0
        for fila in ficheros:
            archivos = archivos + 1
            veces = veces + ficheros[fila]
            txt = {'archivo':fila, 'cantidad':ficheros[fila]}
            txts.append(txt)
        #mensaje = (str(veces) + ' repeticiones en ' + str(archivos) + ' archivos')
        mensaje = str(veces)
        return jsonify({'archivos':txts,'cantidad':mensaje})
    else:
        return jsonify({'palabra':palabra,'cantidad':'NOT FOUND'})

#Activo app. Se indica que tome el puerto de la variable para no generar conflico 
#en Heroku al hacer el push. En caso de no existir la variable (cuando lo corro local)
#toma el puerto TCP 5000
if __name__=='__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=puerto)
