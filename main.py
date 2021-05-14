import sys
from tkinter import *
import mainButtons as mb
from fieldsMarking import *

ship = 0
heightRes = 1080
widthRes = 1920

def gameTableInit():
    fields = {}
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            fields[(i, j)] = 0
    return fields

playerGameTable = gameTableInit()

def whichShip(shipSize):
   global ship
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
    playerButtons = playerButtonsCreate(root, "green", 100, 600)
    enemyButtons = enemyButtonsCreate(root, "yellow", 650, 1150)
    print(playerGameTable)
    mb.MainButtons()
    ships()
    root.mainloop()

def enemyButtonsCreate(root, color, start, end):
    buttons = {}
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            button = Button(root, bg=color)
            button.place(x=i, y=j, height=50, width=50)
            buttons[(i, j)] = button
    return buttons

def playerButtonsCreate(root, color, start, end):
    buttons = {}
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            button = Button(root, bg=color)
            button.place(x=i, y=j, height=50, width=50)
            buttons[(i, j)] = button
            button.bind('<Button-1>', lambda event, b=button: setShip(b,buttons,"v",ship))
            button.bind('<Button-3>', lambda event, b=button: setShip(b, buttons,"h",ship))
    return buttons


def setShip(button:Button,buttons:dict,orientation,s):
    if(s == 0):
        print("Pick up the ship!!")
    else:
        global playerGameTable
        x= button.winfo_x()
        y = button.winfo_y()
        shipSize = s * 50
        if(orientation=="v"):
            if(x<=600-shipSize):
                for i in range(0,shipSize,50):
                    if(playerGameTable[(x+i,y)]==1):
                        print("Cant place ship here, ships collision")
                        button.configure(activebackground="red")
                        continue
                    else:
                        buttons[(x+i,y)].configure(bg = "blue")
                        playerGameTable[(x+i,y)] = 1
            else:
                button.configure(activebackground = "red")
                print("Can't place ship here, game map out of range")
        if (orientation == "h"):
            if (y <= 600-shipSize and x<= 600):
                for i in range(0,shipSize,50):
                    buttons[(x,y+i)].configure(bg = "blue")
                    playerGameTable[(x, y+i)] = 1
            else:
                button.configure(activeforeground="red")
                print("Can't place ship here")


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







