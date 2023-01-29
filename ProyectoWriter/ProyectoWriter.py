# Este programa ayuda a automaticar las tareas de escritura de una web
#
# Librerias

import os
import sys
import openpyxl
import tkinter as tk
import nltk
import requests 
from bs4 import BeautifulSoup
import selenium
import subprocess

# Diseñar la interfaz gráfica del programa con Tkinter, al iniciar el programa me habra una ventana que se ProyectoWriter, con icono personalizado y en ella aparecerá explicado como usar la aplicación, con el fondo de una imagen y debajo aparecerá el boton START, cuando le de a start se abrirá un como una pagina tipo word, donde poder escribir pero con un menu extra, en el que aparecerá, Encabezados automáticos, hiperenlaces automáticos,  Titulo automatico, etiquetas automaticas, Escritor automatico,  guardar y exportar el texto generado en varios formatos como .docx, .pdf, .html, etc. También se podría agregar una función de búsqueda de imágenes y vídeos relacionados con el tema, para agregar al artículo.

# Funciones provistas por la librería Tkinter para crear widgets como ventanas, botones, menús, etc.
ventana = tk.Tk()
ventana.title("Proyecto Writer")
ventana.iconbitmap("icono.ico")

label = tk.Label(ventana, text="Explicación de cómo usar la aplicación:\n1.- Selecciona el tema que quieres escribir.\n2.- Selecciona el tipo de artículo que quieres escribir.\n3.- Selecciona el tipo de formato que quieres exportar el artículo.\n4.- Exporta el artículo.")
label.pack()

#Funcion para abrir la pagina de escritura al darle al boton START
def abrir_pagina_escritura():
    subprocess.run(["python", "PaginaEscritura.py"])
    

boton_start = tk.Button(ventana, text="START", command=abrir_pagina_escritura)
boton_start.pack()

ventana.mainloop()

