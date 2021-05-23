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

class PopUp(Window): #mozna w sumie zrobic klase display z ktorej ta bedzie dziedziczyc, dobra to dopracowac
    def __init__(self,height,width,isResW,isResH,mess):
        super().__init__(height,width,isResW,isResH)
        self.label = Label(self.root, text = mess)
        self.label.place(x=10, y= 35)
        self.button = Button(self.root, text="OK",command = self.closePopUp)
        self.button.place(x=75,y=45)

    def closePopUp(self):
        self.root.destroy()