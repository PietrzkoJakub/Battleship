from tkinter import *

class Window:
    def __init__(self,height,width,isResW,isResH):
        """
        Inicjalizacja okna o danej rozdzielczosci, z mozliwoscia zablokowania zmiany jego rozmiarow.
        """
        self.root = Tk()
        self.root.geometry(str(height) + "x" + str(width))
        self.root.resizable(width=isResW, height=isResH)

    def mainWindowInit(self):
        self.root.mainloop()


class Display(Window):
    """
    Klasa dziedziczaca po klasie Window.
    Jest ona wywolywana w module main i sluzy do inicjalizacji glownego okna programu.
    """
    def __init__(self,height,width,isResW,isResH,title):
        super().__init__(height,width,isResW,isResH)
        self.root.title(title) #dodanie tytulu okna programu

class PopUp(Window):
    """
    Klasa dziedziczaca po klasie Window.
    Jest ona odpowiedzialna za wyswietlanie okien typu pop up.
    """
    def __init__(self, mess):
        super().__init__(250,60,False,False)
        self.label = Label(self.root, text = mess,anchor = "center")
        self.label.pack()
        self.button = Button(self.root, text="OK",command = self.closePopUp)
        self.button.place(x=110,y=30)

    def closePopUp(self):
        """
        Metoda sluzoca do zamykania okienek pop up.
        """
        self.root.destroy()




