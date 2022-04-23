
import re #re = "Regular Expression"
import os
from carga_masiva import Carga

def crear_base():
    directorio = 'archivos_txt'
    frecuencia = {}
    txt = 0
    for archivo in os.listdir(directorio):
        documento = open(directorio +'/' + archivo, 'r', encoding='utf-8')
        texto = documento.read().lower()
        patron = re.findall(r'[a-záéíóúèàêâôñ]{1,20}', texto) #entre {} está la longitud de la palabra. 1-20 significa entre 1 y 20 letras de longitud.
        for palabra in patron:
            contador = frecuencia.get(palabra,0) #si "palabra" existe dentro de "frecuencia" retorna su valor, sino retorna el valor por defecto (en este caso cero)
            frecuencia[palabra] = contador + 1 #por cada existencia de "palabra", incremento en 1 el contador.
        txt = txt + 1
    lista = dict.items(frecuencia)#convierto el diccionario en tupla.
    filas = Carga(lista)
    if filas: print("\n",filas,"cargadas en DB\n",txt,"archivos leídos.\n")
    return
