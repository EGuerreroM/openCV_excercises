# Haga una interfaz en Tkinter que permita obtener una imagen desde archivo, y luego mediante dos clics del mouse que representen las esquinas de un rectángulo haga un recorte de la imagen y presente este recorte en otro panel contiguo a la imagen original


from utils import imUtils
import tkinter as tk
import cv2
from PIL import ImageTk, Image

coordinates = []
windowHeight = 500
windowWidth = 500
maskedImageLabel = None


def clickHandler(event: tk.Event):
    global maskedImageLabel
    if len(coordinates) < 2:
        coordinates.append({'x': event.x, 'y': event.y})
    else:
        coordinates.clear()
        coordinates.append({'x': event.x, 'y': event.y})

    if len(coordinates) == 2:
        cv2Image = cv2.cvtColor(cv2.imread(
            "assets/fruits.jpg"), cv2.COLOR_BGR2RGB)
        maskImage = imUtils.maskImage(
            image=cv2Image, coordinates=coordinates, maskType='rectangle')
        # cv2.imshow("Mask", maskImage)

        # Convert the masked image to a format that can be displayed in a label
        maskedImage = Image.fromarray(maskImage)
        maskedImageTk = ImageTk.PhotoImage(maskedImage)

        # Create a new label and display the masked image
        newMaskedImageLabel = tk.Label(root, image=maskedImageTk)
        newMaskedImageLabel.image = maskedImageTk
        newMaskedImageLabel.place(x=windowWidth+20, y=0)

        # Destroy the previous label widget if it exists
        if maskedImageLabel:
            maskedImageLabel.destroy()

        # Set the new label widget as the current one
        maskedImageLabel = newMaskedImageLabel


root = tk.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCenter = (screenWidth/2) - (windowWidth/2)
yCenter = (screenHeight/2) - (windowHeight/2)

root.geometry(f'1000x1000+{int(xCenter)}+{int(yCenter)}')
window = tk.Canvas(root)

image = imUtils.loadImage(path="assets/fruits.jpg", loadType='tkinter')
btnImage = tk.Button(root, image=image)
btnImage.place(x=0, y=0)
btnImage.bind("<Button-1>", clickHandler)


root.mainloop()
