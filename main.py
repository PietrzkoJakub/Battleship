import sys
from tkinter import *
import mainButtons as mb
from fieldsMarking import *
import random


ship = 0
heightRes = 1080
widthRes = 1920

fourShip = 4
threeShip = 6
twoShip = 6
oneShip = 4

def gameTableInit():
    fields = {}
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            fields[(i, j)] = 0
    return fields

def enemyGameTableInit():
    fields = {}
    for i in range(650, 1150, 50):
        for j in range(100, 600, 50):
            fields[(i, j)] = 0
    return fields

playerGameTable = gameTableInit()
enemyGameTable = enemyGameTableInit()

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
    fieldMarks(root)
    playerButtons = playerButtonsCreate(root, "green", 100, 600)
    enemyButtons = enemyButtonsCreate(root, "yellow", 650, 1150)
    mb.MainButtons()
    ships()
    enemyShips()
    print(enemyGameTable)
    whereIsShip(enemyButtons)
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
        print("Pick up the ship first!!")

    else:
        if(not shipIsAvailable(s)):
            return

        global playerGameTable
        x= button.winfo_x()
        y = button.winfo_y()
        shipSize = s * 50
        if(orientation=="v"):
            if(x<=600-shipSize):
                col = colissionChecker(playerGameTable,shipSize,x,y,orientation)
                for i in range(0,shipSize,50):
                    if(not col):
                        buttons[(x + i, y)].configure(bg="blue")
                        playerGameTable[(x + i, y)] = 1
                        fieldBlocker(playerGameTable, shipSize, x, y, orientation)
                        shipIsUsed(s)
                    else:
                        button.configure(activebackground="red")
                        print("Can't place ship here, ship collision")
                        break
            else:
                button.configure(activebackground = "red")
                print("Can't place ship here, game map out of range")

        if (orientation == "h"):
            if (y <= 600-shipSize and x<= 600):
                col = colissionChecker(playerGameTable, shipSize, x, y, orientation)
                for i in range(0,shipSize,50):
                    if (not col):
                        buttons[(x, y+i)].configure(bg="blue")
                        playerGameTable[(x, y+i)] = 1
                        fieldBlocker(playerGameTable, shipSize, x, y, orientation)
                        shipIsUsed(s)
                    else:
                        button.configure(activebackground="red")
                        print("Can't place ship here, ship collision")
                        break
            else:
                button.configure(activebackground="red")
                print("Can't place ship here, game map out of range")


def colissionChecker(playerGameTable,shipSize,x,y,orient):
    colission = False
    if(orient=="v"):
        for i in range(0, shipSize, 50):
            if(playerGameTable[(x + i, y)]!=0):
                colission = True
        return colission
    elif(orient=="h"):
        for i in range(0, shipSize, 50):
            if(playerGameTable[(x, y+i)]!=0):
                colission = True
        return colission

def fieldBlocker(playerGameTable,shipSize,x,y,o):
    if(o == "v"):
        for i in range(x-50,x+shipSize+50,50): #poziomo
            for j in range(y-50,y+100,50):
                if(i>= 100 and j >=100 and i <=550 and j <=550):
                    if(playerGameTable[(i,j)]== 0):
                        playerGameTable[(i,j)] = "X"

    elif(o == "h"):
        for i in range(x-50,x+100,50): #pionowo
            for j in range(y-50,y+shipSize+50,50):
                if (i >= 100 and j >= 100 and i <= 550 and j <= 550):
                    if(playerGameTable[(i,j)]!= 1 and (i,j) in playerGameTable.keys()):
                        playerGameTable[(i,j)] = "X"


def shipIsUsed(s):
    if(s==1):
        global oneShip
        oneShip -= 1
    elif (s == 2):
        global twoShip
        twoShip -= 1
    elif (s == 3):
        global threeShip
        threeShip -= 1
    elif (s == 4):
        global fourShip
        fourShip -= 1

def shipIsAvailable(s):
    if(s==1):
        global oneShip
        if(oneShip==0):
            return False
        else:
            return True
    elif (s == 2):
        global twoShip
        if (twoShip == 0):
            return False
        else:
            return True
    elif (s == 3):
        global threeShip
        if (threeShip == 0):
            return False
        else:
            return True
    elif (s == 4):
        global fourShip
        if (fourShip == 0):
            return False
        else:
            return True

def enemyShips():
    setEnemyShips(4)
    setEnemyShips(3)
    setEnemyShips(3)
    setEnemyShips(2)
    setEnemyShips(2)
    setEnemyShips(2)
    setEnemyShips(1)
    setEnemyShips(1)
    setEnemyShips(1)
    setEnemyShips(1)


def setEnemyShips(s):
    notPlaced = True
    global enemyGameTable
    while notPlaced:
        x = random.randrange(650,1150,50)
        y = random.randrange(100,550,50)
        o = random.randint(0,1)
        shipSize = s * 50
        if(o==0): #poziomo
            if (x <= 1150 - shipSize):
                col = enemyColissionChecker(enemyGameTable, shipSize, x, y,o)
                for i in range(0, shipSize, 50):
                    if (not col):
                        enemyGameTable[(x + i, y)] = 1
                        enemyFieldBlocker(enemyGameTable, shipSize, x, y,o)
                        notPlaced = False
        else:
            if (y <= 600 - shipSize and x <= 1150):
                col = enemyColissionChecker(enemyGameTable, shipSize, x, y, o)
                for i in range(0, shipSize, 50):
                    if (not col):
                        enemyGameTable[(x, y + i)] = 1
                        enemyFieldBlocker(enemyGameTable, shipSize, x, y, o)
                        notPlaced = False

def enemyColissionChecker(gameTable,shipSize,x,y,o):
    colission = False
    if(o==0):
        for i in range(0, shipSize, 50):
            if(gameTable[(x + i, y)]!=0):
                colission = True
        return colission
    else:
        for i in range(0, shipSize, 50):
            if (gameTable[(x, y + i)] != 0):
                colission = True
        return colission

def enemyFieldBlocker(gameTable,shipSize,x,y,o):
    if (o == 0):
        for i in range(x - 50, x + shipSize + 50, 50):  # poziomo
            for j in range(y - 50, y + 100, 50):
                if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                    if (gameTable[(i, j)] == 0):
                        gameTable[(i, j)] = "X"
    else:
        for i in range(x - 50, x + 100, 50):  # pionowo
            for j in range(y - 50, y + shipSize + 50, 50):
                if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                    if (gameTable[(i, j)] != 1 and (i, j) in gameTable.keys()):
                        gameTable[(i, j)] = "X"

def whereIsShip(buttonTable):
    global enemyGameTable
    for i in range(650,1150,50):
        for j in range(100,600,50):
            if enemyGameTable[(i,j)] == 1:
                buttonTable[(i,j)].configure(bg = "red")



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


"""
def printWhereX(gameTable):
    counter = 0
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            if(gameTable[(i,j)]=="X"):
                print("(x = {}, y = {})".format(i,j))
                counter += 1
    print(counter)




def printWhereOne(gameTable):
    counter = 0
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            if(gameTable[(i,j)]==1):
                print("("+i+","+j+")")
                counter += 1
    print(counter)
"""

