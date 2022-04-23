
import re #re = "Regular Expression"
import os

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
