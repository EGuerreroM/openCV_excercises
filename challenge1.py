# Bernardo Guerrero 2020010522

# Realice una interfaz gráfica con Tkinter que le permita obtener una imagen a partir de un archivo, luego con ayuda del mouse dar dos clics en la imagen para obtener dos coordenadas que corresponderán a las esquinas de un rectángulo dentro de la imagen y producirá una máscara con la que en otro panel se presentará la imagen enmascarada.

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np


# creando un tipado para las coordenadas
coordinatesType = [{'x': int, 'y': int}, {'x': int, 'y': int}]

# creating a type for the image
imageType = np.ndarray


class MouseControl:
    def __init__(self, button: tk.Button):
        self.button = button
        self.button.bind("<Double-Button-1>", self.double_click)
        # definir una variable para guardar las 4 coordenadas
        self.coordinates = []
        self.image = None
        self.mask = None

    def double_click(self, event: tk.Event):
        # obteniendo la coordenada de la esquina superior izquierda +50 px dentro de la imagen
        # y la inferior derecha +50 px dentro de la imagen del
        # boton
        x1 = self.button.winfo_rootx()+50
        y1 = self.button.winfo_rooty()+50
        x2 = x1 + self.button.winfo_width()-50
        y2 = y1 + self.button.winfo_height()-50
        # guardando las variables en la lista en 2 objetos con llaves x y y
        self.coordinates = [{'x': x1, 'y': y1}, {'x': x2, 'y': y2}]

        self.image = loadImage("assets/fruits.jpg")
        self.mask = maskImage(self.image, self.coordinates)
        cv2.imshow('Mask', self.mask)


# Creando una funcion que se encargue de cargar una imagen por cv2 y transformarla para
# tkinter
def loadImage(path: str):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


# Creando una funcion que se encargue de enmascarar la imagen con las coordenadas
def maskImage(image: imageType, coordinates: coordinatesType):
    firstPoint = coordinates[0]
    secondPoint = coordinates[1]

    # Creando el rectangulo para la mascara
    mask = np.zeros(image.shape[:2], dtype='uint8')
    mask = cv2.rectangle(mask, (firstPoint['x'], firstPoint['y']), (
        secondPoint['x'], secondPoint['y']), 255, -1)
    enmask = cv2.bitwise_and(image, image, mask=mask)

    return enmask


# creando el canvas
root = tk.Tk()
window = tk.Canvas(root, bg='gray', height=1000, width=1000)
window.place(x=0, y=0)


# haciendo la carga de la imagen como boton y agregandolo al canvas
image = ImageTk.PhotoImage(Image.open("assets/fruits.jpg"))
btnImage = tk.Button(root, image=image)
btnImage.place(x=window.winfo_width()/2, y=window.winfo_height()/2)
btnImage.pack()

# creando el objeto mouse para evaluar los clicks
mouse = MouseControl(btnImage)
window.mainloop()
