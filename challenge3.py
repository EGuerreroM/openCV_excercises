# Haga una interfaz en Tkinter que permita obtener una imagen desde archivo y luego mediante tres radio button obtener la visualización en otro panel de los canales R, G y B.


import tkinter as tk
from tkinter import filedialog
from utils import imUtils
import numpy as np
import os
import cv2

windowHeight = 100
windowWidth = 100
filename = ""

# obteniendo la ruta del archivo actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# creating redChannel function


def redChannel():
    global filename
    cv2Image = cv2.imread(filename)
    (b, g, r) = cv2.split(cv2Image)
    zeros = np.zeros(cv2Image.shape[:2], dtype='uint8')
    cv2.imshow('Red', r)
    cv2.waitKey(0)
    cv2.imshow('Red', cv2.merge([zeros, zeros, r]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# creating greenChannel function


def greenChannel():
    global filename
    cv2Image = cv2.imread(filename)
    (b, g, r) = cv2.split(cv2Image)
    cv2.imshow('Green', g)
    zeros = np.zeros(cv2Image.shape[:2], dtype='uint8')
    cv2.waitKey(0)
    cv2.imshow('Green', cv2.merge([zeros, g, zeros]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# creating blueChannel function


def blueChannel():
    global filename
    cv2Image = cv2.imread(filename)
    (b, g, r) = cv2.split(cv2Image)
    cv2.imshow('Blue', b)
    cv2.waitKey(0)
    zeros = np.zeros(cv2Image.shape[:2], dtype='uint8')
    cv2.imshow('Blue', cv2.merge([b, zeros, zeros]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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

    # creating 3 buttons of medium dimensions for the channels
    selection = tk.StringVar()
    selection.set("Red")
    btnRed = tk.Radiobutton(root, text="Red", height=5, width=10,
                            variable=selection, value="Red", command=redChannel)
    btnRed.pack()
    btnGreen = tk.Radiobutton(root, text="Green", height=5,
                              width=10, variable=selection, value="Green", command=greenChannel)
    btnGreen.pack()
    btnBlue = tk.Radiobutton(root, text="Blue", height=5, width=10,
                             variable=selection, value="Blue", command=blueChannel)
    btnBlue.pack()


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
