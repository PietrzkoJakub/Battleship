import sys
from tkinter import *
from windows import *
from fieldsMarking import *
from player import *
from enemy import *
import random
from ships import Ship

"""
Nie ma algorytmu ktory sprawia ze jak komputer trafi to potem losuje te najblizsze 21.05.2021 21:24 teraz jest ale trzeba go dokladniej potestowac 22.05.2021 no i nie dziala
Na pewno ze strony gracza to dobrze dziala 22.05.2021 no nie wiem czy nie dodac funkcji ktora mu nie strzelania w inne pola niz to wokol, chyba ze wystarczy ze komputer strzela dopki nie chybi i gracz ma ta sama opcje
Pop upy lub zabronienia niektorych rzeczy trzeba dorobic, na pewno zablokwoac uzytkownikowi  strzelac przed wcisneiciem nowej gry
Ukrocic duplikacje kodu, bo narazoe nie wyglada to dobrze
Dodac metody wirtualne
Dodac wyjatki i polaczyc je z pop upami
No i tesy

""'
Aktulizacja na 23.05.2021 
Algorytm losujacy zostal mniej wiecej napisany ale trzeba go przenalizowac
Wygrana i przegrana dziala tak ze trzeba kliknac jescze raz zeby sie napis wyswietlil wiec to mozna poprawic #dziala to juz poprawnie
Przegrana i wygrana dzialaja poprawnie
W klasie gameplayer zostaly dodane metody wirtualne i zainicjowane w player i enemy
Usunalem gettery i settery
"""

"""
Aktualizacja 27.05
No uproscilem ten schemat losowego strzelania przez przeciwnika ale trzeba go potestowac
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
            self.enemy.pleaceEnemyShipsOnMap()
            self.enemy.enableButtons()
            self.whoShitFirst()
            #self.whereIsShip()

        else:
            PopUp("Plaece all yours ships first!!")

    def whoShotFirst(self):
        r = random.randint(0,1)
        if(r==1):
            self.enemy.enemyShot()

    def resetGame(self):
        Game(self.root)
    def whereIsShip(self):
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                if self.enemy.enemyGameTable[(i, j)] == 1:
                   self.enemy.enemyButtons[(i, j)].configure(bg="red")



if __name__ == '__main__':
    display = Display(1920,1080,True,True,"Baattleship")
    root = display.root
    Game(root).mainWindowInit()
























