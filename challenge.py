# Use Tkinter to make a GUI that loads an image
# and allows the user to rotate it by 359 degrees
# with a slider

import cv2
import tkinter as tk
from PIL import Image, ImageTk


class ImageRotator:
    def __init__(self, master):
        self.master = master
        master.title("Image Rotator")

        # Load the image
        self.image = Image.open("assets/lena.jpg")
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Create the image label
        self.image_label = tk.Label(master, image=self.image_tk)
        self.image_label.pack()

        # Create the slider
        self.slider = tk.Scale(master, from_=0, to=359,
                               orient=tk.HORIZONTAL, command=self.rotate_image)
        self.slider.pack()

    def rotate_image(self, angle):
        # Rotate the image and update the label
        rotated_image = self.image.rotate(int(angle))
        rotated_image_tk = ImageTk.PhotoImage(rotated_image)
        self.image_label.configure(image=rotated_image_tk)
        self.image_label.image = rotated_image_tk


root = tk.Tk()
rotator = ImageRotator(root)
root.mainloop()
