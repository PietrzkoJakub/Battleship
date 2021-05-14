import sys
from tkinter import *
from buttonsChecker import *
import mainButtons as mb

ship = 0

heightRes = 1080
widthRes = 1920
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]

def whichShip(shipSize):
   ship = shipSize

def rootInit():
    root = Tk()
    root.geometry(str(widthRes) + "x" + str(heightRes))
    root.resizable(width=True, height=True)
    root.title("Battleship")
    return root


def mainWindowInit():
    root = rootInit()
    fieldMarks(root,alphabet)
    playerButtons = buttonCreate(root, "green", 100, 600)
    enemyButtons = buttonCreate(root, "yellow", 650, 1150)
    mb.MainButtons()
    ships()
    root.mainloop()


def buttonCreate(root,color,start,end):
    buttons = {}
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            button = Button(root, bg=color)
            button.place(x=i, y=j, height=50, width=50)
            buttons[(i, j)] = button
            button.bind('<Button-1>', lambda event, b=button: setShip(b,buttons,"v",3))
            button.bind('<Button-3>', lambda event, b=button: setShip(b, buttons,"h",3))
    return buttons

def setShip(button:Button,buttons:dict,orientation,s):
    x= button.winfo_x()
    y = button.winfo_y()
    shipSize = s * 50
    if(orientation=="v"):
        if(x<=600-shipSize):
            for i in range(0,shipSize,50):
                buttons[(x+i,y)].configure(bg = "blue")
        else:
            button.configure(activebackground = "red")
            print("Can't place ship here")
    if (orientation == "h"):
        if (y <= 600-shipSize and x<= 600):
            for i in range(0,shipSize,50):
                buttons[(x,y+i)].configure(bg = "blue")
        else:
            button.configure(activeforeground="red")
            print("Can't place ship here")


def fieldFillWithLetters(root, letters, startLocation, endLocation):
    j = 0
    for i in range(int(startLocation + 25), int(endLocation + 25), 50):
        label = Label(root, text=letters[j]).place(x=i, y=75)
        j += 1

def fieldFillWithNumbers(root,xCordinate):
    j = 1
    for i in range(int(100 + 25), int(600 + 25), 50):
        label = Label(root, text=str(j)).place(x=xCordinate, y=i - 5)
        j += 1


def fieldMarks(root, letters):
    fieldFillWithLetters(root, letters, 100, 600)
    fieldFillWithLetters(root, letters, 650, 1150)
    fieldFillWithNumbers(root, 75)
    fieldFillWithNumbers(root, 625)

def gameTable():
    gameTable = [[0 for j in range(10)] for i in range(10)]
    return gameTable


def ships():
    fourmast = Button(text="FOURMAST", bg = "purple")
    fourmast.place(x=1200, y=200, height=50, width=200)
    fourmast.bind('<Button-1>', lambda event, b=fourmast: whichShip(4))
    threemast = Button(text="THREEMAST", bg="purple")
    threemast.place(x=1200, y=250, height=50, width=150)
    threemast.bind('<Button-1>', lambda event, b=threemast: whichShip(3))
    twomast = Button(text="TWOMAST", bg="purple")
    twomast.place(x=1200, y=300, height=50, width=100)
    twomast.bind('<Button-1>', lambda event, b=twomast: whichShip(2))
    onemast = Button(text="ONE", bg="purple")
    onemast.place(x=1200, y=350, height=50, width=50)
    onemast.bind('<Button-1>', lambda event, b=onemast: whichShip(1))


if __name__ == '__main__':
    mainWindowInit()







