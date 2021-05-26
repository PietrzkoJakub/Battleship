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

class PopUp(Window):
    def __init__(self, mess):
        super().__init__(250,60,False,False)
        self.label = Label(self.root, text = mess,anchor = "center")
        self.label.pack()
        self.button = Button(self.root, text="OK",command = self.closePopUp)
        self.button.place(x=50,y=30)

    def closePopUp(self):
        self.root.destroy()


