from enemy import *
import random

class Game:
    def __init__(self, root):
        self.root = root #przekazanie glownego okna gry
        self.player = Player(self.root) #inicjalizacja obiektu Player
        self.enemy = Enemy(self.root, self.player) #inicjalizacja obiektu Enemy

        #inicjalizcja glownych przyciskow
        self.button1 = Button(self.root, text="New Game", command=self.newGame)
        self.button1.place(x=0, y=0, height=25, width=80)
        self.button2 = Button(self.root, text="Reset Game", command=self.resetGame)
        self.button2.place(x=0, y=25, height=25, width=80)
        self.button3 = Button(self.root, text="Exit", command=self.exit)
        self.button3.place(x=0, y=50, height=25, width=80)

        #inicjalizacja przyciskow sluzacych do wyboru odpowiedniego okretu przez gracza
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
        """
        Metoda przypisana do przycisku Exit, konczaca dzialanie calego programu.
        """
        sys.exit(1)

    def newGame(self):
        """
        Metoda przypisana do przycisku New Game. Odpowiada za rozpoczecie nowej gry.
        Rozpoczecie nowej gry jest mozliwe tylko i wylacznie po rozmiesczeniu wszystkich okretow przez gracza.
        Jezeli wszystkie okrety zostaly rozmiesczone przez gracza, statki przeciwnika sa umiesczane w spoosob losowy na planszy.
        Przyciski przeciwnika zostaje aktywowane.
        Nastepuje losowanie, kto oddaje pierwszy strzal.
        Przycisk nowej gry zostaje dezaktywowany. Nie ma mozlowsci wcisniecia go w trakcie rozgrywki.
        Przyciski gracza zostaja dezaktywowane, w celu zablokowania mozliwosci strzelania we wlasne pola.
        """
        if (self.player.oneMast.quantity + self.player.twoMast.quantity + self.player.threeMast.quantity + self.player.fourMast.quantity == 0):
            self.enemy.placeEnemyShipsOnMap()
            self.enemy.enableButtons()
            self.whoShotFirst()
            self.button1["state"] = "disabled"
            self.player.buttonBlocker()
        else:
            PopUp("Plaece all yours ships first!!")

    def resetGame(self):
        """
        Metoda przypisana do przycisku Reset Game.
        Inicjalizuje ona ponownie obiekt klasy Player oraz Enemy.
        Przycisk nowej gry staje sie ponownie aktywny.
        """
        self.player = Player(self.root)
        self.enemy = Enemy(self.root, self.player)
        self.button1["state"] = "normal"

    def whoShotFirst(self):
        """
        Metoda sluzaca do wylosowania, kto oddaje strzal jako pierwszy, gracz czy przeciwnik.
        """
        r = random.randint(0, 1)
        if (r == 1):
            self.enemy.enemyShot()

    def whereIsShip(self):
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                if self.enemy.enemyGameTable[(i, j)] == 1:
                    self.enemy.enemyButtons[(i, j)].configure(bg="red")
