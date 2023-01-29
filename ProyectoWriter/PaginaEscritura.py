# Pagina de trabajo o escritura
#
# Librerias

import os
import sys
import openpyxl

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk import sent_tokenize, word_tokenize, pos_tag

import requests 
from bs4 import BeautifulSoup
import html
import selenium

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import tkinter.simpledialog as simpledialog

# Interfaz de escritura tipo word



######################################## VENTANA ########################################
# Crear ventana
ventana = tk.Tk()
ventana.title("Proyecto Writer")
ventana.iconbitmap("icono.ico")



# Crear caja de texto con barra de desplazamiento
texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD)
texto.pack()


######################################### CLASES #########################################
class WriterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Writer")
        self.iconbitmap("icono.ico")
        
        self.toolbar = Toolbar(self)
        self.text = tk.Text(self)
        
        self.toolbar.pack(side='top', fill='x')
        self.text.pack(side='bottom', fill='both', expand=True)
        
class Toolbar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.bold_button = ttk.Button(self, text='Negrita', command=self.make_bold)
        self.bold_button.pack(side='left')
        
    def make_bold(self):
        # obtener el texto seleccionado
        # cambiar el atributo de tipo de letra
        selected_text = self.parent.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.parent.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.parent.text.insert(tk.INSERT, selected_text, 'bold')

###################################### FUNCIONES ######################################
#Funciones para guardar y exportar el archivo
def guardar():
    archivo = open("archivo.txt", "w")
    archivo.write(texto.get(1.0, tk.END))
    archivo.close()
    os.startfile("archivo.txt")

def exportar_docx():
    archivo = open("archivo.docx", "w")
    archivo.write(texto.get(1.0, tk.END))
    archivo.close()
    os.startfile("archivo.docx")

def exportar_pdf():
    archivo = open("archivo.pdf", "w")
    archivo.write(texto.get(1.0, tk.END))
    archivo.close()
    os.startfile("archivo.pdf")

def exportar_html():
    archivo = open("archivo.html", "w")
    archivo.write(texto.get(1.0, tk.END))
    archivo.close()
    os.startfile("archivo.html")

# Funciones para dar formato al texto
def negrita():
    texto.tag_add("negrita", "sel.first", "sel.last")
    texto.tag_config("negrita", font=("Arial", 12, "bold"))

def cursiva():
    texto.tag_add("cursiva", "sel.first", "sel.last")
    texto.tag_config("cursiva", font=("Arial", 12, "italic"))
    
def subrayado():
    texto.tag_add("subrayado", "sel.first", "sel.last")
    texto.tag_config("subrayado", font=("Arial", 12, "underline"))

# Funciones para dar tamaño al texto
def establecer_tamaño(tamaño):
    seleccion = texto.tag_ranges("sel")
    if len(seleccion) != 0:
        texto.tag_add("tamaño", seleccion[0], seleccion[1])
        texto.tag_config("tamaño", font=("Arial", tamaño))
    else:
        texto.config(font=("Arial", tamaño))
        
# Funcion para encabezados
def encabezado():
    texto.tag_add("encabezado", "sel.first", "sel.last")
    texto.tag_config("encabezado", font=("Arial", 12, "bold"))

def h1():
    texto.tag_add("h1", "sel.first", "sel.last")
    texto.tag_config("h1", font=("Arial", 18, "bold"))

def h2():
    texto.tag_add("h2", "sel.first", "sel.last")
    texto.tag_config("h2", font=("Arial", 16, "bold"))

def h3():
    texto.tag_add("h3", "sel.first", "sel.last")
    texto.tag_config("h3", font=("Arial", 14, "bold"))

def h4():
    texto.tag_add("h4", "sel.first", "sel.last")
    texto.tag_config("h4", font=("Arial", 12, "bold"))

def h5():
    texto.tag_add("h5", "sel.first", "sel.last")
    texto.tag_config("h5", font=("Arial", 12, "bold"))

def h6():
    texto.tag_add("h6", "sel.first", "sel.last")
    texto.tag_config("h6", font=("Arial", 12, "bold"))
    
# Funcion para hipervinculos
def hipervinculo():
    direccion = simpledialog.askstring("Ingrese la dirección del hiperenlace", "Ingrese la dirección del hiperenlace:")
    texto.tag_add("hipervinculo", "sel.first", "sel.last")
    texto.tag_config("hipervinculo", foreground="blue", underline=1, url=direccion)
    
# Funcion para cambiar vista
def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_html(texto):
    return html.escape(texto)

# Funciones para cambiar entre vistas
# Guardar contenido original del texto
texto_original = texto.get("1.0", "end-1c")

# Funciones para cambiar entre vistas
def vista_escrita():
    texto.config(wrap=tk.WORD) # deshabilita el ajuste automático de línea
    texto.config(state=tk.NORMAL) # habilita la edición de texto
    texto.delete("1.0", tk.END) # borra el contenido actual del texto
    texto.insert(tk.END, texto_original) # inserta el contenido original del texto

def vista_html():
    texto.config(wrap=tk.NONE) # habilita el ajuste automático de línea
    texto.config(state=tk.DISABLED) # deshabilita la edición de texto
    texto.delete("1.0", tk.END) # borra el contenido actual del texto
    texto.insert(tk.END, parse_html(texto_original)) # inserta el código HTML generado

    
# Funcion para encabezados automaticos

def encabezados_automaticos(texto):
    sentencias = sent_tokenize(texto)
    for sentencia in sentencias:
        palabras = word_tokenize(sentencia)
        etiquetas = pos_tag(palabras)
        for etiqueta in etiquetas:
            if etiqueta[1] == "NNP" or etiqueta[1] == "NN":
                if etiqueta[0] == "Sin" or etiqueta[0] == "sin":
                    print("<h1>" + sentencia + "</h1>")
                else:
                    print("<h2>" + sentencia + "</h2>")
            else:
                print(sentencia)


##################################### BARRA DE HERRAMIENTAS #######################################
# Crear barra de herramientas
barra_herramientas = tk.Menu(ventana)
ventana.config(menu=barra_herramientas)

# Crear elementos de la barra de herramientas
archivo_menu = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_command(label="Exportar como .docx", command=exportar_docx)
archivo_menu.add_command(label="Exportar como .pdf", command=exportar_pdf)
archivo_menu.add_command(label="Exportar como .html", command=exportar_html)

vista_html = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Vista", menu=vista_html)
vista_html.add_command(label="Escrita", command=lambda: vista_escrita("Escrita"))
vista_html.add_command(label="HTML", command=lambda: vista_html("HTML"))

formato_menu = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Formato", menu=formato_menu)
formato_menu.add_command(label="Negrita", command=negrita)
formato_menu.add_command(label="Cursiva", command=cursiva)
formato_menu.add_command(label="Subrayado", command=subrayado)

encabezado_menu = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Encabezado", menu=encabezado_menu)
encabezado_menu.add_command(label="H1", command=h1)
encabezado_menu.add_command(label="H2", command=h2)
encabezado_menu.add_command(label="H3", command=h3)
encabezado_menu.add_command(label="H4", command=h4)
encabezado_menu.add_command(label="H5", command=h5)
encabezado_menu.add_command(label="H6", command=h6)

tamaño_menu = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Tamaño de Letra", menu=tamaño_menu)
for i in range(1,101):
    tamaño_menu.add_command(label=str(i), command=lambda i=i: establecer_tamaño(i))

herramientas_menu = tk.Menu(barra_herramientas)
barra_herramientas.add_cascade(label="Herramientas", menu=herramientas_menu)
herramientas_menu.add_command(label="Hiperenlace", command=hipervinculo)
herramientas_menu.add_command(label="Encabezados Automáticos", command=encabezados_automaticos)
herramientas_menu.add_command(label="Hiperenlaces Automáticos")
herramientas_menu.add_command(label="Buscar y Reemplazar")










ventana.mainloop()