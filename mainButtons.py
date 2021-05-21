from tkinter import *

class MainButtons:
    def __init__(self,root):
        self.button1 = Button(root,text="New Game",command = self.newGame)
        self.button1.place(x=0, y=0, height=25, width=80)

        self.button2 = Button(root,text="Reset Game", command=self.resetGame)
        self.button2.place(x=0, y=25, height=25, width=80)

        self.button3 = Button(root,text="Exit", command=self.exit)
        self.button3.place(x=0, y=50, height=25, width=80)

    def exit(self):
        sys.exit(1)

    def newGame(self):
        pass

    def resetGame(self):
        pass


