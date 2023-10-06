import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load the image
img = cv2.imread("assets/lena.jpg")

# Create a function to flip the image horizontally


def flip_image():
    global img
    img = cv2.flip(img, 1)
    update_image()

# Create a function to update the image in the GUI


def flip_vertical():
    global img
    img = cv2.flip(img, 0)
    update_image()


def update_image():
    global img
    # Convert the image to RGB format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Convert the image to a PIL Image object
    img_pil = Image.fromarray(img_rgb)
    # Convert the PIL Image object to a Tkinter PhotoImage object
    img_tk = ImageTk.PhotoImage(img_pil)
    # Update the label with the new image
    label.config(image=img_tk)
    label.image = img_tk


# Create the GUI window
root = tk.Tk()

# Create a label to display the image
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_pil = Image.fromarray(img_rgb)
img_tk = ImageTk.PhotoImage(img_pil)
label = tk.Label(root, image=img_tk)
label.pack()

# Create a button to flip the image
button = tk.Button(root, text="Flip Image", command=flip_image)
button.pack()

# Create a button to flip the image vertically
button = tk.Button(root, text="Flip Image Vertically", command=flip_vertical)
button.pack()

# Start the GUI loop
root.mainloop()
