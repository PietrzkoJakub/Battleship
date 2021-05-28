from tkinter import *
from gameplayer import *
from windows import *
from fieldsMarking import *

class Player(GamePlayer):
    def __init__(self,root):
        self.root = root

        self.ship = 0
        self.fourMast = Ship(4, 1)
        self.threeMast = Ship(3, 2)
        self.twoMast = Ship(2, 3)
        self.oneMast = Ship(1, 4)

        self.playerWin = False

        self.playerGameTable = self.gameTableInit(0)
        self.playerAllShips = 20
        self.playerButtons = self.buttonsCreate()
        self.playerGoodShot = False

        self.fieldsMark = FieldsMark(self.root, 100, 600, 75)
        self.fieldsMark.fieldFillWithLetters()
        self.fieldsMark.fieldFillWithNumbers()


    def buttonsCreate(self):
        buttons = {}
        for i in range(100, 600, 50):
            for j in range(100, 600, 50):
                button = Button(self.root, bg="green")
                button.place(x=i, y=j, height=50, width=50)
                buttons[(i, j)] = button
                button.bind('<Button-1>', lambda event, b=button: self.setShip(b.winfo_x(),b.winfo_y(), "v"))
                button.bind('<Button-3>', lambda event, b=button: self.setShip(b.winfo_x(),b.winfo_y(), "h"))
        return buttons


    def setShip(self,x,y,orientation):
        if (self.ship == 0):
            PopUp("Pick up the ship first!")
        else:
            if (not self.shipIsAvailable()):
                return
            shipSize = self.ship * 50
            if (orientation == "v"):
                if (x <= 600 - shipSize):
                    col = self.colissionChecker(shipSize, x, y, orientation)
                    for i in range(0, shipSize, 50):
                        if (not col):
                            self.playerButtons[(x + i, y)].configure(bg="blue")
                            self.playerGameTable[(x + i, y)] = 1
                            self.fieldBlocker(shipSize, x, y, orientation)
                            self.shipIsUsed()
                        else:
                            #button.configure(activebackground="red")
                            PopUp("Can't place ship here, ship collision")
                            break
                else:
                    #button.configure(activebackground="red")
                    PopUp("Can't place ship here, game map out of range")

            if (orientation == "h"):
                if (y <= 600 - shipSize and x <= 600):
                    col = self.colissionChecker(shipSize, x, y, orientation)
                    for i in range(0, shipSize, 50):
                        if (not col):
                            self.playerButtons[(x, y + i)].configure(bg="blue")
                            self.playerGameTable[(x, y + i)] = 1
                            self.fieldBlocker(shipSize, x, y, orientation)
                            self.shipIsUsed()
                        else:
                            #button.configure(activebackground="red")
                            PopUp("Can't place ship here, ship collision")
                            break
                else:
                    #button.configure(activebackground="red")
                    PopUp("Can't place ship here, game map out of range")

    def colissionChecker(self,shipSize, x, y, orient):
        colission = False
        if (orient == "v"):
            for i in range(0, shipSize, 50):
                if (self.playerGameTable[(x + i, y)] != 0):
                    colission = True
            return colission
        elif (orient == "h"):
            for i in range(0, shipSize, 50):
                if (self.playerGameTable[(x, y + i)] != 0):
                    colission = True
            return colission

    def fieldBlocker(self, shipSize, x, y, o):
        if (o == "v"):
            for i in range(x - 50, x + shipSize + 50, 50):  # poziomo
                for j in range(y - 50, y + 100, 50):
                    if (i >= 100 and j >= 100 and i <= 550 and j <= 550):
                        if (self.playerGameTable[(i, j)] == 0):
                            self.playerGameTable[(i, j)] = "X"

        elif (o == "h"):
            for i in range(x - 50, x + 100, 50):  # pionowo
                for j in range(y - 50, y + shipSize + 50, 50):
                    if (i >= 100 and j >= 100 and i <= 550 and j <= 550):
                        if (self.playerGameTable[(i, j)] != 1 and (i, j) in self.playerGameTable.keys()):
                            self.playerGameTable[(i, j)] = "X"


    def shipIsUsed(self):
        if (self.ship == 1):
            self.oneMast.quantity -= 1
        elif (self.ship == 2):
            self.twoMast.quantity -= 1
        elif (self.ship == 3):
            self.threeMast.quantity -= 1
        elif (self.ship == 4):
            self.fourMast.quantity -= 1



    def shipIsAvailable(self):
        if (self.ship == 1):
            if (self.oneMast.quantity == 0):
                return False
            else:
                return True
        elif (self.ship == 2):
            if (self.twoMast.quantity == 0):
                return False
            else:
                return True
        elif (self.ship == 3):
            if (self.threeMast.quantity == 0):
                return False
            else:
                return True
        elif (self.ship == 4):
            if (self.fourMast.quantity == 0):
                return False
            else:
                return True

    def playerSetShip(self, ship):
        self.ship = ship
