from tkinter import *
from PIL import Image, ImageTk




class ChampImg:
    def __init__(self, width, high):
        self.width = width
        self.high = high

    def change_img(self, root, path, xp, yp=0):
        image = Image.open(path)
        image = image.resize((self.width, self.high), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(image)
        Imagelabel = Label(root, image=im, borderwidth=0, highlightthickness=0)
        Imagelabel.place(x=xp, y=yp)
        Imagelabel.image = im
