
# Haga una interfaz en Tkinter que permita obtener una imagen desde archivo y luego con un botón ordenar que se calcule el histograma y se presente en otro panel (requerirá presentar la imagen de matplotlib en tkinter).


import tkinter as tk
from tkinter import filedialog
from utils import imUtils
import numpy as np
import os
import cv2
from matplotlib import pyplot as plt


windowHeight = 100
windowWidth = 100
filename = ""

# obteniendo la ruta del archivo actual
dir_path = os.path.dirname(os.path.realpath(__file__))


def histogram():
    global filename
    cv2Image = cv2.imread(filename, 0)
    hist = cv2.calcHist([cv2Image], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Histograma de la imagen")
    plt.xlabel("Bins")
    plt.ylabel("# de pixeles")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(1)


def equalizeHist():
    global filename
    cv2Image = cv2.imread(filename, 0)
    eq = cv2.equalizeHist(cv2Image)
    cv2.imshow("Ecualización del histograma", np.hstack([cv2Image, eq]))
    cv2.waitKey(1)
    plt.figure()
    plt.title("Histograma de la imagen")
    plt.xlabel("Bins")
    plt.ylabel("# de pixeles")
    plt.plot(eq)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(1)


def clickHandler():
    global filename, image
    # obteniendo la ruta de la imagen seleccionada
    filename = filedialog.askopenfilename(
        initialdir=dir_path, title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*"))
    )

    # cargando la imagen
    image = imUtils.loadImage(path=filename, loadType='tkinter')
    # load image in canvas
    window.config(width=image.width(), height=image.height())
    window.create_image(0, 0, anchor='nw', image=image)
    window.pack()

    # creando un boton en canvas para la funcion del histograma
    btn = tk.Button(root, text="Histograma", height=5,
                    width=10, command=histogram)
    btn.pack()

    # creando un boton en canvas para la funcion de ecualizacion
    btn = tk.Button(root, text="Ecualizar", height=5,
                    width=10, command=equalizeHist)
    btn.pack()


root = tk.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCenter = (screenWidth/2) - (windowWidth/2)
yCenter = (screenHeight/2) - (windowHeight/2)
root.geometry(f'700x900+{int(xCenter)}+{0}')
window = tk.Canvas(root)

# creando un boton en canvas
btn = tk.Button(root, text="load image", height=5,
                width=10, command=clickHandler)
btn.pack()

# creando un label en canvas
label = tk.Label(root, text="")
label.pack()

root.mainloop()
