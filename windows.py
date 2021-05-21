from tkinter import *

class Window:
    def __init__(self,height,width,isResW,isResH):
        self.root = Tk()
        self.root.geometry(str(height) + "x" + str(width))
        self.root.resizable(width=isResW, height=isResH)

    def mainWindowInit(self):
        self.root.mainloop()


class Display(Window):
    def __init__(self,height,width,isResW,isResH,title):
        super().__init__(height,width,isResW,isResH)
        self.root.title(title)

    def getroot(self):
        return self.root

class PopUp(Window): #mozna w sumie zrobic klase display z ktorej ta bedzie dziedziczyc
    def __init__(self,height,width,isResW,isResH,mess):
        super().__init__(height,width,isResW,isResH)
        self.button = Button(self.root, text=mess, command=exit)
        self.button.place(x=0, y=0, height=75, width=150)
