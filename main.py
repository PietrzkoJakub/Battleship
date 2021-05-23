import sys
from tkinter import *
from windows import *
from fieldsMarking import *
from player import *
from enemy import *
import random
from ships import Ship

"""
Strzelanie dziala tak ze jak ja strzele, to wykonywana jest funkcja strzelajca(komputer)
Wiec nie ma mozliwosci losowego pierwszego strzalu
Nie ma algorytmu ktory sprawia ze jak komputer trafi to potem losuje te najblizsze 21.05.2021 21:24 teraz jest ale trzeba go dokladniej potestowac 22.05.2021 no i nie dziala
Na pewno ze strony gracza to dobrze dziala 22.05.2021 no nie wiem czy nie dodac funkcji ktora mu nie strzelania w inne pola niz to wokol, chyba ze wystarczy ze komputer strzela dopki nie chybi i gracz ma ta sama opcje
Pop upy lub zabronienia niektorych rzeczy trzeba dorobic, na pewno zablokwoac uzytkownikowi  strzelac przed wcisneiciem nowej gry
Ukrocic duplikacje kodu, bo narazoe nie wyglada to dobrze
Dodac metody wirtualne
Dodac wyjatki i polaczyc je z pop upami
No i tesy


22.95.2021
Jescze przegrana nie dziala jak trzeba, za wczesnie sie chyba odapala
"""


"""
Wywalic gettery i settery
"""


"""
Aktulizacja na 23.05.2021 19:16
Algorytm losujacy zostal mniej wiecej napisany ale trzeba go przenalizowac
Wygrana i przegrana dziala tak ze trzeba kliknac jescze raz zeby sie napis wyswietlil wiec to mozna poprawic
Przegrana i wygrana dzialaja poprawnie
"""


class Game:
    def __init__(self,root):
        self.root = root
        self.player = Player(self.root)
        self.enemy = Enemy(self.root,self.player)

        self.button1 = Button(root, text="New Game", command=self.newGame)
        self.button1.place(x=0, y=0, height=25, width=80)
        self.button2 = Button(root, text="Reset Game", command=self.resetGame)
        self.button2.place(x=0, y=25, height=25, width=80)
        self.button3 = Button(root, text="Exit", command=self.exit)
        self.button3.place(x=0, y=50, height=25, width=80)


        self.fourmast = Button(self.root, text="FOURMAST", bg="purple")
        self.fourmast.place(x=1200, y=200, height=50, width=200)
        self.fourmast.bind('<Button-1>', lambda event, b=self.fourmast: self.player.playerSetShip(4))
        self.threemast = Button(text="THREEMAST", bg="purple")
        self.threemast.place(x=1200, y=250, height=50, width=150)
        self.threemast.bind('<Button-1>', lambda event, b=self.threemast: self.player.playerSetShip(3))
        self.twomast = Button(text="TWOMAST", bg="purple")
        self.twomast.place(x=1200, y=300, height=50, width=100)
        self.twomast.bind('<Button-1>', lambda event, b=self.twomast: self.player.playerSetShip(2))
        self.onemast = Button(text="ONE", bg="purple")
        self.onemast.place(x=1200, y=350, height=50, width=50)
        self.onemast.bind('<Button-1>', lambda event, b=self.onemast: self.player.playerSetShip(1))

    def mainWindowInit(self):
        self.root.mainloop()

    def exit(self):
        sys.exit(1)

    def newGame(self):
        if(self.player.oneMast.quantity + self.player.twoMast.quantity+ self.player.threeMast.quantity + self.player.fourMast.quantity == 0):
            self.enemy.setShips()
            #self.whereIsShip()
        else:
            print("Pickup your ships first!!")

    def resetGame(self):
        Game(self.root) #chyba dziala

    def whereIsShip(self):
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                if self.enemy.enemyGameTable[(i, j)] == 1:
                    self.enemy.enemyButtons[(i, j)].configure(bg="red")


if __name__ == '__main__':
    display = Display(1920,1080,True,True,"Baattleship")
    root = display.getroot()
    Game(root).mainWindowInit()

























"""
if __name__ == '__main__':
    display = Display(1920,1080,True,True,"Baattleship")
    root = display.getroot()
    Game(root).mainWindowInit()
    #root.mainloop() #temporary
    #MainButtons(root)
    #playerFieldMarks = FieldsMark(root,100,600,75) # nie wiem czy to wszystko nie jest zbedne po prostu
    #playerFieldMarks.fieldFillWithNumbers()
    #playerFieldMarks.fieldFillWithLetters() to sprawdzic
    #enemyFieldMarks = FieldsMark(root, 550, 1150,625)
    #enemyFieldMarks.fieldFillWithNumbers()
    #enemyFieldMarks.fieldFillWithLetters()
    #tu zaraz bedzie nowe


class Game:
    def __init__(self,root):
        self.root = root
        self.ship = 0
        self.fourMast = Ship(4,1)
        self.threeMast = Ship(3,2)
        self.twoMast = Ship(2,3)
        self.oneMast = Ship(1,4)
        self.enemyAllShips = 20
        self.playerAllShips = 20
        self.playerGameTable = self.gameTableInit(0)
        self.enemyGameTable = {} #init in newgame method
        self.playerButtons = self.playerButtonsCreate()
        self.enemyButtons = self.enemyButtonsCreate()
        self.alreadyShootingHere = []
        self.horizontal = "h"
        self.vertical = "v"

        #To na pewno przepisac do metod
        self.fourmast = Button(self.root,text="FOURMAST", bg="purple")
        self.fourmast.place(x=1200, y=200, height=50, width=200)
        self.fourmast.bind('<Button-1>', lambda event, b=self.fourmast: self.whichShip(self.fourMast))
        self.threemast = Button(text="THREEMAST", bg="purple")
        self.threemast.place(x=1200, y=250, height=50, width=150)
        self.threemast.bind('<Button-1>', lambda event, b=self.threemast: self.whichShip(self.threeMast))
        self.twomast = Button(text="TWOMAST", bg="purple")
        self.twomast.place(x=1200, y=300, height=50, width=100)
        self.twomast.bind('<Button-1>', lambda event, b=self.twomast: self.whichShip(self.twoMast))
        self.onemast = Button(text="ONE", bg="purple")
        self.onemast.place(x=1200, y=350, height=50, width=50)
        self.onemast.bind('<Button-1>', lambda event, b=self.onemast: self.whichShip(self.oneMast))

        #przyciski glowne przeniesione z innej klasy
        self.button1 = Button(root, text="New Game", command=self.newGame)
        self.button1.place(x=0, y=0, height=25, width=80)

        self.button2 = Button(root, text="Reset Game", command=self.resetGame)
        self.button2.place(x=0, y=25, height=25, width=80)

        self.button3 = Button(root, text="Exit", command=self.exit)
        self.button3.place(x=0, y=50, height=25, width=80)

    def exit(self):
        sys.exit(1)

    def newGame(self):
        if (self.fourMast.getQuantity() + self.threeMast.getQuantity() + self.twoMast.getQuantity() + self.oneMast.getQuantity() == 0):
            self.enemyGameTable = self.gameTableInit(550)
            #enemyShips()
            #whereIsShip(enemyButtons)
        else:
            print("Put all Your ships on the map first")

    def resetGame(self):
        pass

    def mainWindowInit(self):
        self.root.mainloop()

    def whichShip(self,ship:Ship):
        self.ship = ship.getSize()

    def playerButtonsCreate(self):
        buttons = {}
        for i in range(100, 600, 50):
            for j in range(100, 600, 50):
                button = Button(root, bg="green")
                button.place(x=i, y=j, height=50, width=50)
                buttons[(i, j)] = button
                button.bind('<Button-1>', lambda event, b=button: self.setShip(b, self.vertical))
                button.bind('<Button-3>', lambda event, b=button: self.setShip(b, self.horizontal))
        return buttons

    def enemyButtonsCreate(self):
        buttons = {}
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                button = Button(root, bg="yellow")
                button.place(x=i, y=j, height=50, width=50)
                button.bind('<Button-1>', lambda event, b=button: self.shot(b))
                buttons[(i, j)] = button
        return buttons

    def shot(self,button:Button):
        pass

    def gameTableInit(self,pixels):
        fields = {}
        for i in range(100+pixels, 600+pixels,50):
            for j in range(100, 600, 50):
                fields[(i, j)] = 0
        return fields

    def setShip(self,button,orientation):

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

"""
