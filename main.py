
import sys
import os
import time
from PIL import Image, ImageTk
import tkinter as tk

# 🔥 FUNCIÓN CLAVE PARA EL EXE
def ruta_archivo(nombre):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nombre)
    return nombre

# Ventana principal
root = tk.Tk()
root.title("Caine")
root.geometry("400x400")

label = tk.Label(root)
label.pack()

# Función para mostrar imagen
def mostrar_imagen(nombre):
    img = Image.open(ruta_archivo(nombre))
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

# Secuencia de inicio
def inicio():
    mostrar_imagen("caine_inicio.png")
    root.after(2000, feliz)

def feliz():
    mostrar_imagen("caine_feliz1.png")
    root.after(500, lambda: mostrar_imagen("caine_feliz2.png"))
    root.after(1000, lambda: mostrar_imagen("caine_feliz3.png"))
    root.after(2000, enojado)

def enojado():
    mostrar_imagen("caine_enojado1.png")
    root.after(500, lambda: mostrar_imagen("caine_enojado2.png"))
    root.after(1000, lambda: mostrar_imagen("caine_enojado3.png"))
    root.after(2000, dibujo)

def dibujo():
    mostrar_imagen("caine_dibujo1.png")
    root.after(500, lambda: mostrar_imagen("caine_dibujo2.png"))
    root.after(1000, lambda: mostrar_imagen("caine_dibujo3.png"))
    root.after(2000, interesado)

def interesado():
    mostrar_imagen("caine_interesado1.png")
    root.after(500, lambda: mostrar_imagen("caine_interesado2.png"))
    root.after(1000, lambda: mostrar_imagen("caine_interesado3.png"))
    root.after(2000, entretenido)

def entretenido():
    mostrar_imagen("caine_entretenido1.png")
    root.after(2000, aburrido)

def aburrido():
    mostrar_imagen("caine_aburrido1.png")
    root.after(500, lambda: mostrar_imagen("caine_aburrido2.png"))
    root.after(1000, lambda: mostrar_imagen("caine_aburrido3.png"))
    root.after(2000, dormido)

def dormido():
    mostrar_imagen("caine_dormido.png")
    root.after(2000, asustado)

def asustado():
    mostrar_imagen("caine_asustado.png")

# Iniciar animación
inicio()

root.mainloop()