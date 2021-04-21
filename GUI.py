import tkinter as tk
from tkinter import ttk
import awesometkinter as atk
from PIL import Image, ImageTk
import main
import random

def test_cmd():
   image_path = 'Download/' + main.final_list[random.randint(0, len(main.final_list)-1)] + '.jpg'
   print(image_path)

   newx = Image.open(image_path)
   newx = newx.resize((250, 282), Image.ANTIALIAS)

   newtest = ImageTk.PhotoImage(newx)
   label1.configure(image = newtest)
   label1.image = newtest
   label1.pack()


main.preprocces_('jg.txt')
image_path = 'Download/' + main.final_list[random.randint(0, len(main.final_list)-1)] + '.jpg'

# our root
root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.title('Random_Pick')
icon = ImageTk.PhotoImage(Image.open("icon.jpg"))
root.iconphoto(False, icon)
root.config(background=atk.DEFAULT_COLOR)
root.resizable(False, False)
# select tkinter theme required for things to be right on windows,
# only 'alt', 'default', or 'classic' can work fine on windows 10
s = ttk.Style()
s.theme_use('classic')

image1 = Image.open(image_path)
image1 = image1.resize((250, 282), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image = test,borderwidth=0, highlightthickness=0)
label1.pack(side='top', expand=True)
# Position image


# 3d frame
f1 = atk.Frame3d(root)
f1.pack(side='bottom', expand=True, fill='both', padx=3, pady=0)

# 3d progressbar
#bar = atk.RadialProgressbar3d(f1, fg='cyan', size=120)
#bar.pack(padx=20, pady=20)
#bar.start()



# 3d button
x = atk.Button3d(f1, text='Random!!!',w =30, command = test_cmd)
x.pack(pady=10)





root.mainloop()
