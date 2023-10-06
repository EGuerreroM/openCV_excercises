import cv2
import tkinter as tk
from PIL import Image, ImageTk


class ImageResizer:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Image Resizer")

        # Load the image
        self.image = cv2.imread("assets/lena.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image_tk = ImageTk.PhotoImage(Image.fromarray(self.image))

        # Create the image label
        self.image_label = tk.Label(master, image=self.image_tk)
        self.image_label.pack()

        # Create the slider
        self.slider = tk.Scale(master, from_=25, to=100,
                               orient=tk.HORIZONTAL, command=self.resize_image)
        # self.slider.pack()
        self.slider.place(relx=0.5, rely=1.0, anchor=tk.S)
        self.slider.set(50)

    def resize_image(self, scale):
        # Resize the image and update the label
        resized_image = cv2.resize(
            self.image, (0, 0), fx=float(scale)/100, fy=float(scale)/100)
        resized_image_tk = ImageTk.PhotoImage(Image.fromarray(resized_image))
        self.image_label.configure(image=resized_image_tk)
        self.image_label.image = resized_image_tk


root = tk.Tk()
root.geometry("700x700")
resizer = ImageResizer(root)
root.mainloop()
