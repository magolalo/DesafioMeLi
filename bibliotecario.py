
import re #re = "Regular Expressions"
import os

#Se formatea el término poniendo todo en minúsculas y limintando el inicio y fin para poder
# diferenciar, por ejemplo, "lente" de "lentes". El for recorre los archivos buscando y contando 
# en cada uno la palabra buscada. Se devuelve un diccionario con el nombre del archivo como keys 
# el valor de cantidad de repeticiones correspondiente. 
def Buscador(palabra):
    directorio = 'archivos_txt'
    palabra = palabra.lower()
    palabra = '(\W|^)'+palabra+'(\W|$)'
    texts = {}
    for archivo in os.listdir(directorio):
        document_text = open(directorio +'/' + archivo, 'r', encoding='utf-8')
        text_string = document_text.read().lower()
        patron = re.findall(palabra, text_string)
        if len(patron): texts[archivo] = len(patron)
    return texts
