from tkinter import *
import awesometkinter as atk
from PIL import Image, ImageTk
from Pre_Process import PreProcess
import random


def open_image_resize(path, width, high):
    image = Image.open(path)
    image = image.resize((width, high), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)


def m_motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


class MyButton:
    def __init__(self, app_root, image_path, hover_path, role, ChampI, p_x, p_y, start_idx=2, jump_idx=8):
        self.image_path = image_path
        self.role = role
        self.root = app_root
        self.mButton = atk.Button3d(app_root)
        self.p_x = p_x
        self.p_y = p_y
        self.h_path = hover_path
        self.Image_B = open_image_resize(image_path, p_x, p_y)
        self.ImageX = ChampI
        try:
            self.Pro = PreProcess()
            self.Pro.filter_txt('Roles_DB/'+role+'.txt', role, start_idx, jump_idx)
            self.Champ_List = self.Pro.get_list()
        except:
            print(role + " Loading Error")

    def create(self, b_width, b_high):
        self.mButton = atk.Button3d(self.root, image=self.Image_B, command=self.get_new_rand)
        self.mButton.place(x=b_width, y=b_high)
        self.mButton.bind("<Enter>", self.on_enter)
        self.mButton.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        # print('enter')
        self.Image_B = open_image_resize(self.h_path, self.p_x, self.p_y)
        self.mButton.configure(image=self.Image_B)
        self.mButton.image = self.Image_B

    def on_leave(self, e):
        # print('out')
        self.Image_B = open_image_resize(self.image_path, self.p_x, self.p_y)
        self.mButton.configure(image=self.Image_B)
        self.mButton.image = self.Image_B

    def enable_motion_track(self):
        self.root.bind('<Button 1>', m_motion)

    def get_new_rand(self):
        self.ImageX.change_img(self.root, 'Images/'+random.choice(self.Champ_List)+'.jpg', 960 - 290, 50)

