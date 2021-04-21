from tkinter import *
import awesometkinter as atk
from PIL import Image, ImageTk
from Custom_Button import MyButton
from ChampImage import ChampImg


def open_image_resize(path, width, high):
    image = Image.open(path)
    image = image.resize((width, high), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)


root = Tk()
icon = ImageTk.PhotoImage(Image.open("Icons/icon.jpg"))
root.iconphoto(False, icon)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pixels_right = int(screen_height/2.5)
pixels_down = int(screen_width/9)
app_width = int(screen_width/2)
app_high = int(screen_height/2)
size_x_B = int(0.05 * app_width)
size_y_B = int(0.089 * app_high)
root.geometry('{}x{}+{}+{}'.format(app_width, app_high, pixels_right, pixels_down))
root.title('Main')


root.config(background=atk.DEFAULT_COLOR)
root.resizable(False, False)
C = Canvas(root, height=app_high, width=app_width)
im = open_image_resize("Images/BG.png", app_width, app_high)
background_label = Label(root, image=im, borderwidth=0, highlightthickness=0)
background_label.place(x=0, y=0)
C.pack(expand=True)


champ = ChampImg(250, 282)

sup = MyButton(root, "Icons/support_n.png", "Icons/support_h.png", "sup", champ, size_x_B, size_y_B)
sup.create(app_width*0.65, app_high*0.75)


adc = MyButton(root, "Icons/bot_n.png", "Icons/bot_h.png", "adc", champ, size_x_B, size_y_B)
adc.create(app_width*0.65, app_high*0.88)

jg = MyButton(root, "Icons/jungle_n.png", "Icons/jungle_h.png", "jg", champ, size_x_B, size_y_B)
jg.create(app_width*0.25, app_high*0.45)

mid = MyButton(root, "Icons/mid_n.png", "Icons/mid_h.png", "mid", champ, size_x_B, size_y_B)
mid.create(app_width*0.45, app_high*0.45)

top = MyButton(root, "Icons/top_n.png", "Icons/top_h.png", "top", champ, size_x_B, size_y_B)
top.create(app_width*0.15, app_high*0.15)

top.enable_motion_track()
root.mainloop()
