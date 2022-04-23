
from flask import Flask, jsonify
from consulta import ConsultoDatos
from bibliotecario import Buscador
from proc_archivos import crear_base
import os

app=Flask(__name__)

if not os.path.isfile('mini.db'): 
    crear_base()
#else:
#    print('La base aun no fue creada')

@app.route("/<palabra>", methods=["GET"])
def busquemos(palabra): 
    cantidad = ConsultoDatos(palabra)
    if cantidad: 
        return jsonify({'palabra':palabra,'cantidad':cantidad[0]})
    else:
        return jsonify({'palabra':palabra,'cantidad':'NOT FOUND'})


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
            txt = {'arvhivo':fila, 'cantidad':ficheros[fila]}
            txts.append(txt)
        mensaje = (str(veces) + ' repeticiones en ' + str(archivos) + ' archivos')
        return jsonify({'archivos':txts,'mensaje':mensaje})
    else:
        return jsonify({'palabra':palabra,'cantidad':'NOT FOUND'})


if __name__=='__main__':
    app.run(debug=True) #debug=True es para que reinicie solo el servivio luego de cada cambio. 
