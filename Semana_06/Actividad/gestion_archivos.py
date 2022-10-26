# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:49:41 2022

@author: danie
"""
import os

def crear_archivo(nombre_archivo, contenido):
    archivo = open(nombre_archivo,"at")
    archivo.write(contenido)
    archivo.close()
    
def eliminar_archivo(nombre_archivo):
    os.remove(nombre_archivo)
    
def agregar_archivo_contenido(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as noticia:
        noticia.write(contenido)
    
def leer_archivo(nombre_archivo):
    noticia = open(nombre_archivo)
    datos_noticia = noticia.read()
    print(datos_noticia)
    

