from tkinter import *
from gameplayer import *

class Player(GamePlayer):
    def __init__(self,root):
        self.ship = 0
        self.root = root
        self.fourMast = Ship(4, 1)
        self.threeMast = Ship(3, 2)
        self.twoMast = Ship(2, 3)
        self.oneMast = Ship(1, 4)
        self.playerGameTable = self.gameTableInit(0)
        self.playerAllShips = 20
        self.playerButtons = self.playerButtonsCreate()
        self.playerGoodShot = False

    def playerButtonsCreate(self):
        buttons = {}
        for i in range(100, 600, 50):
            for j in range(100, 600, 50):
                button = Button(self.root, bg="green")
                button.place(x=i, y=j, height=50, width=50)
                buttons[(i, j)] = button
                button.bind('<Button-1>', lambda event, b=button: self.setShip(b, "v"))
                button.bind('<Button-3>', lambda event, b=button: self.setShip(b, "h"))
        return buttons


    def setShip(self,button:Button,orientation):
        if (self.ship == 0):
            print("Pick up the ship first!!")
        else:
            if (not self.shipIsAvailable()):
                return
            x = button.winfo_x()
            y = button.winfo_y()
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
                            button.configure(activebackground="red")
                            print("Can't place ship here, ship collision")
                            break
                else:
                    button.configure(activebackground="red")
                    print("Can't place ship here, game map out of range")

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
                            button.configure(activebackground="red")
                            print("Can't place ship here, ship collision")
                            break
                else:
                    button.configure(activebackground="red")
                    print("Can't place ship here, game map out of range")

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
            self.oneMast.setQuantity(self.oneMast.getQuantity() - 1)
        elif (self.ship == 2):
            self.twoMast.setQuantity(self.twoMast.getQuantity() - 1)
        elif (self.ship == 3):
            self.threeMast.setQuantity(self.threeMast.getQuantity() - 1)
        elif (self.ship == 4):
            print(self.fourMast.getQuantity())
            self.fourMast.setQuantity(self.fourMast.getQuantity() - 1)



    def shipIsAvailable(self):
        if (self.ship == 1):
            if (self.oneMast.getQuantity() == 0):
                return False
            else:
                return True
        elif (self.ship == 2):
            if (self.twoMast.getQuantity() == 0):
                return False
            else:
                return True
        elif (self.ship == 3):
            if (self.threeMast.getQuantity() == 0):
                return False
            else:
                return True
        elif (self.ship == 4):
            if (self.fourMast.getQuantity() == 0):
                return False
            else:
                return True

    def playerSetShip(self,ship):
        self.ship = ship