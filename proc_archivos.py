
import re #re = "Regular Expressions"
import os
from carga_masiva import Carga

#Este script corre por única vez al iniciar la app.
#El primer for recorre los archivos uno por uno cargando el contenido del .txt en la variable texto.
#La opción findall del módulo re (re.findall) devuelve una lista de palabras que hagan match con el criterio.
#El criterio [a-záéíóúèàêâôñ] significa todo agrupación de caracteres de de a-z incluyendo vocales con tildes y ñ.
#{1,20} limita a agrupaciones de 1 a 20 caracteres. Jugar con estos números es útilo durante el desarrollo 
# para limitar el procesamiento.
#El segudno for recorre la lista de palabras de cada archivo, y por cada palabra única incremente el contador.
#El diccionario frecuencia lleva la relación de repetición de cada palabra a medida que se recorren los .txt
#Al final se hace la carga en la DB llamando a la función Carga la cual retorna la cantidad de filas insertadas en la DB.

def crear_base():
    directorio = 'archivos_txt'
    frecuencia = {}
    txt = 0
    for archivo in os.listdir(directorio):
        documento = open(directorio +'/' + archivo, 'r', encoding='utf-8')
        texto = documento.read().lower()
        patron = re.findall(r'[a-záéíóúèàêâôñ]{1,20}', texto) 
        for palabra in patron:
            contador = frecuencia.get(palabra,0) #si "palabra" existe dentro de "frecuencia" retorna su valor, sino retorna el valor por defecto (en este caso cero)
            frecuencia[palabra] = contador + 1 #por cada existencia de "palabra", incremento en 1 el contador.
        txt = txt + 1
    lista = dict.items(frecuencia)#convierto el diccionario en tupla.
    filas = Carga(lista)
    if filas: print("\n",filas,"cargadas en DB\n",txt,"archivos leídos.\n")
    return
