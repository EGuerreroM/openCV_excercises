import numpy as np
import cv2
from PIL import Image, ImageTk
from typing import Union, Literal


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    displacement = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return displacement


def rotateImage(image, angle, center=None, scale=1.0):
    (height, width) = image.shape[:2]
    if center is None:
        center = (width/2, height/2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotatedImage = cv2.warpAffine(image, M, (width, height))
    return rotatedImage


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (imageHeight, imageWidth) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height/float(imageHeight)
        dim = (int(imageWidth*r), height)
    else:
        r = width/float(imageWidth)
        dim = (width, int(imageHeight*r))

    redim = cv2.resize(image, dim, interpolation=inter)
    return redim


loadType = Union[Literal['tkinter'], Literal['PIL']]


def loadImage(path: str, loadType: loadType):
    image = None
    if loadType == 'tkinter':
        image = ImageTk.PhotoImage(Image.open(path))

    if loadType == 'PIL':
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

    return image


maskType = Union[Literal['rectangle'], Literal['circle']]


def maskImage(image: np.ndarray, coordinates: list, maskType: maskType):
    firstPoint = coordinates[0]
    secondPoint = coordinates[1]

    # Creando el rectangulo para la mascara
    mask = np.zeros(image.shape[:2], dtype='uint8')

    if maskType == 'rectangle':
        mask = cv2.rectangle(mask, (firstPoint['x'], firstPoint['y']), (
            secondPoint['x'], secondPoint['y']), 255, -1)
    elif maskType == 'circle':
        radius = int(np.sqrt((firstPoint['x']-secondPoint['x'])
                             ** 2+(firstPoint['y']-secondPoint['y'])**2))
        mask = cv2.circle(img=mask, center=(
            firstPoint['x'], firstPoint['y']), radius=radius, color=255, thickness=-1)

    enmask = cv2.bitwise_and(image, image, mask=mask)
    return enmask
