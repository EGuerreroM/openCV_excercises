# Realice una interfaz gráfica con Tkinter que haga lo mismo que el numeral anterior solamente que la máscara será un círculo donde un clic será el centro y otro clic será el que defina con la distancia hacia la primera coordenada el radio y así tener la máscara para la imagen mostrada en otro panel.

from utils import imUtils
import tkinter as tk
import cv2

coordinates = []
windowHeight = 500
windowWidth = 500


def clickHandler(event: tk.Event):
    if len(coordinates) < 2:
        coordinates.append({'x': event.x, 'y': event.y})
    else:
        coordinates.clear()
        coordinates.append({'x': event.x, 'y': event.y})

    if len(coordinates) == 2:
        cv2Image = cv2.cvtColor(cv2.imread(
            "assets/fruits.jpg"), cv2.COLOR_BGR2RGB)
        maskImage = imUtils.maskImage(
            image=cv2Image, coordinates=coordinates, maskType='circle')
        cv2.imshow("Mask", maskImage)


root = tk.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCenter = (screenWidth/2) - (windowWidth/2)
yCenter = (screenHeight/2) - (windowHeight/2)

root.geometry(f'1000x1000+{int(xCenter)}+{int(yCenter)}')
window = tk.Canvas(root)

image = imUtils.loadImage(path="assets/fruits.jpg", loadType='tkinter')
btnImage = tk.Button(root, image=image)
btnImage.pack()
btnImage.bind("<Button-1>", clickHandler)


window.mainloop()
