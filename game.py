from enemy import *
import random

class Game:
    def __init__(self, root):
        self.root = root
        self.player = Player(self.root)
        self.enemy = Enemy(self.root, self.player)

        self.button1 = Button(self.root, text="New Game", command=self.newGame)
        self.button1.place(x=0, y=0, height=25, width=80)
        self.button2 = Button(self.root, text="Reset Game", command=self.resetGame)
        self.button2.place(x=0, y=25, height=25, width=80)
        self.button3 = Button(self.root, text="Exit", command=self.exit)
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
        if (self.player.oneMast.quantity + self.player.twoMast.quantity + self.player.threeMast.quantity + self.player.fourMast.quantity == 0):
            self.enemy.pleaceEnemyShipsOnMap()
            self.enemy.enableButtons()
            self.whoShotFirst()
            self.button1["state"] = "disabled"  # zabezpieczenie zeby w trakcie gry nie mozna bylo wcisanc tego przycisku, dopiero po resecie
        else:
            PopUp("Plaece all yours ships first!!")

    def resetGame(self):
        self.player = Player(self.root)
        self.enemy = Enemy(self.root, self.player)
        self.button1["state"] = "normal"

    def whoShotFirst(self):
        r = random.randint(0, 1)
        if (r == 1):
            self.enemy.enemyShot()

    def whereIsShip(self):
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                if self.enemy.enemyGameTable[(i, j)] == 1:
                    self.enemy.enemyButtons[(i, j)].configure(bg="red")
