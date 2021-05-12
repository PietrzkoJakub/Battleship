import sys
from tkinter import *

"""
This is the main file, with game loop
"""
gameOver = False

def exit():
    sys.exit(1)

def newGame():
    pass

def resetGame():
    pass

def mainWindowInit():
    display = Tk()
    display.resizable(width = True, height = True)

    #welcome = Label(display,text = "Battleship")
    #welcome.grid(row = 0, column= 0) #text location on the window(table)

    #Frame
    #frame = Frame(display,borderwidth = 4)
    #frame.grid(row=0, column=1)
    #frame.config(background='black')
    #lab1 = Label(frame, text='Ramka')
    #lab1.grid(sticky=E, row=0, column=0, padx=100, pady=100)

    #Buttons
    mainButtonsInit()
    mapButtonsInit()
    display.mainloop()


def mainButtonsInit():
    button1 = Button(text="Exit", command=exit)
    button1.grid(row=4, column=0)
    button1.config(height=1, width=10)
    button1.pack
    button2 = Button(text="New Game", command=newGame)
    button2.grid(row=2, column=0)
    button2.config(height=1, width=10)
    button2.pack
    button3 = Button(text="Reset Game", command=resetGame())
    button3.grid(row=3, column=0)
    button3.config(height=1, width=10)
    button3.pack

def mapButtonsInit():
    for i in range(5,15):
        for j in range(20,30):
            button = Button(bg = "blue")
            button.grid(row = i, column = j)
            button.config(height = 2, width = 5)
            button.pack
    for i in range(5,15):
        for j in range(30,40):
            button = Button(bg = "red")
            button.grid(row = i, column = j)
            button.config(height=2, width=5)
            button.pack




if __name__ == "__main__":
    while(not gameOver):
        mainWindowInit()




