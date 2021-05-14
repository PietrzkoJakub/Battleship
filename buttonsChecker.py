import sys
from tkinter import *


class Checkers:
    def __init__(self,root):
        self.buttonsDict = {}
        self.root = root
    def create_button(self, setBg, x, y):
        button = Button(self.root, bg=setBg)
        button.place(x=x, y=y, height=50, width=50)
        self.buttonsDict[(x, y)] = button

    def update_button(self, x, y,command):
        self.buttonsDict[(x, y)]["command"] = command

    def change_color(self,x,y,color):
        self.buttonsDict[(x,y)].configure(bg = color)