from gameplayer import *
from player import *
import random
from windows import PopUp
from fieldsMarking import *
from exceptions import *

class Enemy(GamePlayer):

    def __init__(self, root, player: Player):  # to rozwianie z playerem mi sie nie podoba
        self.player = player
        self.root = root
        self.fourMast = Ship(4, 1)
        self.threeMast = Ship(3, 2)
        self.twoMast = Ship(2, 3)
        self.oneMast = Ship(1, 4)
        self.enemyGameTable = self.gameTableInit(550)
        self.enemyAllShips = 20
        self.enemyButtons = self.buttonsCreate()
        self.notPlaced = True
        self.shipSize = 0
        self.alreadyShootingHere = []
        self.recursionStop = 4
        self.orient = 1
        self.randomOrientation = 0
        self.fieldsMark = FieldsMark(self.root, 650, 1150, 625)
        self.fieldsMark.fieldFillWithLetters()
        self.fieldsMark.fieldFillWithNumbers()
        self.enemyWin = False


    def buttonsCreate(self):
        buttons = {}
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                button = Button(self.root, bg="yellow", state="disabled")
                button.place(x=i, y=j, height=50, width=50)
                button.bind('<Button-1>', lambda event, b=button: self.shot(b.winfo_x(),b.winfo_y()))
                buttons[(i, j)] = button
        return buttons

    def enableButtons(self):
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                self.enemyButtons[(i, j)].configure(state="normal")

    def pleaceEnemyShipsOnMap(self):
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for i in ships:
            self.setShip(i)

    def setShip(self, ship):  # zobaczymy czy przekazanie tej zmiennej tu wystarczy
        self.notPlaced = True
        while self.notPlaced:
            x = random.randrange(650, 1150, 50)
            y = random.randrange(100, 550, 50)
            o = random.randint(0, 1)
            self.shipSize = ship * 50
            if (o == 0):  # poziomo
                if (x <= 1150 - self.shipSize):
                    col = self.colissionChecker(x, y, o)
                    for i in range(0, self.shipSize, 50):
                        if (not col):
                            self.enemyGameTable[(x + i, y)] = 1
                            self.fieldBlocker(x, y, o)
                            self.notPlaced = False
            else:
                if (y <= 600 - self.shipSize and x <= 1150):
                    col = self.colissionChecker(x, y, o)
                    for i in range(0, self.shipSize, 50):
                        if (not col):
                            self.enemyGameTable[(x, y + i)] = 1
                            self.fieldBlocker(x, y, o)
                            self.notPlaced = False

    def colissionChecker(self, x, y, o):
        colission = False
        if (o == 0):
            for i in range(0, self.shipSize, 50):
                if (self.enemyGameTable[(x + i, y)] != 0):
                    colission = True
            return colission
        else:
            for i in range(0, self.shipSize, 50):
                if (self.enemyGameTable[(x, y + i)] != 0):
                    colission = True
            return colission

    def fieldBlocker(self, x, y, o):
        if (o == 0):
            for i in range(x - 50, x + self.shipSize + 50, 50):  # poziomo
                for j in range(y - 50, y + 100, 50):
                    if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                        if (self.enemyGameTable[(i, j)] == 0):
                            self.enemyGameTable[(i, j)] = "X"
        else:
            for i in range(x - 50, x + 100, 50):  # pionowo
                for j in range(y - 50, y + self.shipSize + 50, 50):
                    if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                        if (self.enemyGameTable[(i, j)] != 1 and (i, j) in self.enemyGameTable.keys()):
                            self.enemyGameTable[(i, j)] = "X"

    def shot(self, x,y):
        button = self.enemyButtons[(x,y)]
        if (button["state"] == "disabled"):  # jezeli gracz juz tu strzelal
            PopUp("You already shoot here")  # tylko tu jest taki problem ze przed rozpoczeciem gry tez to sie pojawia
            #raise YouAlreadyShootHereException nie moge tu umiescic wyjatku poniewaz nie obsluze go w lambdzie
            return False
        if self.enemyGameTable[(x, y)] == 1:
            button.configure(bg="blue", state="disabled")
            self.enemyAllShips -= 1
            self.player.playerGoodShot = True
        else:
            button.configure(bg="red", state="disabled")
            self.player.playerGoodShot = False

        if (not self.player.playerGoodShot):  # jezeli trafie gram dalej
            self.enemyShot()

        if (self.enemyAllShips == 0):
            self.player.playerWin = True
            PopUp("You win! Restart or exit the game").root.grab_set_global()
        if (self.player.playerAllShips == 0):
            self.enemyWin = True
            PopUp("You lose! Restart or exit the game").root.grab_set_global()


    def enemyShot(self):
        while True:  # komputer bedzie losowal miejsce do strzalu dopoki nie trafi na takie co nie strzelal
            x = random.randrange(100, 600, 50)
            y = random.randrange(100, 600, 50)
            hardLevel = random.randint(0, 5)
            if (hardLevel < 4):
                if (self.player.playerGameTable[(x, y)] == "X"):
                    continue

            if (x, y) not in self.alreadyShootingHere:
                if self.player.playerGameTable[(x, y)] == 1:  # jezeli trafi
                    self.player.playerButtons[(x, y)].configure(bg="yellow")
                    self.player.playerAllShips -= 1
                    self.alreadyShootingHere.append((x, y))
                    self.recursionStop = 4
                    self.randomOrientation = randint(0,1)  # losowanie oreintacji w jakiej bedzie wykonywany losowy strzal
                    self.tryShootWholeShip(x, y)
                else:
                    self.player.playerButtons[(x, y)].configure(bg="red")  # jezeli nie trafi
                    self.alreadyShootingHere.append((x, y))
                break
            else:
                continue

    def tryShootWholeShip(self, x, y):
        if (self.recursionStop > 0):
            if (self.randomOrientation == 0):  # poziomo
                if (x <= 500 and (x + 50, y) not in self.alreadyShootingHere):
                    self.shotRec(x + 50, y)
                elif (x > 150 and (x - 50, y) not in self.alreadyShootingHere):
                    self.shotRec(x - 50, y)
                else:
                    self.enemyShot()  # przeciwnik ma losowy strzal


            elif (self.randomOrientation == 1):  # pionowo
                if (y > 150 and (x, y - 50) not in self.alreadyShootingHere):
                    self.shotRec(x, y - 50)
                elif (y <= 500 and (x, y + 50) not in self.alreadyShootingHere):
                    self.shotRec(x, y + 50)
                else:
                    self.enemyShot()  # przeciwnik ma losowy strzal

    def shotRec(self, x, y):
        self.recursionStop -= 1
        if self.player.playerGameTable[(x, y)] == 1:  # jezeli przeciwnik  trafi
            self.player.playerButtons[(x, y)].configure(bg="yellow")
            self.player.playerAllShips -= 1
            self.alreadyShootingHere.append((x, y))
            self.tryShootWholeShip(x, y)
        else:
            self.player.playerButtons[(x, y)].configure(bg="red")  # jezeli przeciwnik nie trafi
            self.alreadyShootingHere.append((x, y))




