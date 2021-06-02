from gameplayer import *
from windows import *
from fieldsMarking import *


class Player(GamePlayer):
    def __init__(self, root):
        self.root = root #glowne okno gry przekazywane w celu poprawnego wysiwetlenia przyciskow
        self.ship = 0 #pole "mowiace" metodzie setShip jaki okret jest obecnie umiesczany

        #odpowienie okrety
        self.fourMast = Ship(4, 1)
        self.threeMast = Ship(3, 2)
        self.twoMast = Ship(2, 3)
        self.oneMast = Ship(1, 4)

        self.playerWin = False #pole przechowujace informacje o wygranej

        self.playerGameTable = self.gameTableInit(0) #inicjalizacja tablicy gry
        self.playerAllShips = 20 #liczba wszystkich pol z okreatmi gracza, jezeli pole zostanie trafione przez przeciwnika, zmniejsza sie o 1
        self.playerButtons = self.buttonsCreate() #inicjalizacja slownika przyciskow
        self.playerGoodShot = False #pole informujace o trafienu przez gracza w statek przeciwnika

        #oznaczanie pol gracza cyframi i literami
        self.fieldsMark = FieldsMark(self.root, 100, 600, 75)
        self.fieldsMark.fieldFillWithLetters()
        self.fieldsMark.fieldFillWithNumbers()

    def buttonsCreate(self):
        """
        Nadpisana metoda wirtualna z klasy GamePlayer sluzoca do stworzenia slownika, przyciskow i umiesczenia ich na mapie.
        Kluczem w slowniku sa wspolrzedne x,y danego przycisku, a wartoscia dany przycisk.
        Do kazdego przycisku jest przypisana metoda setShip pozwalajaca na ustawienie statku, horyzontalnie (klikniecie lewego
        myszy) lub wertykalnie (klikniecie prawego przycisku myszy)
        """
        buttons = {}
        for i in range(100, 600, 50):
            for j in range(100, 600, 50):
                button = Button(self.root, bg="green")
                button.place(x=i, y=j, height=50, width=50)
                buttons[(i, j)] = button
                button.bind('<Button-1>', lambda event, b=button: self.setShip(b.winfo_x(), b.winfo_y(), "v"))
                button.bind('<Button-3>', lambda event, b=button: self.setShip(b.winfo_x(), b.winfo_y(), "h"))
        return buttons

    def setShip(self, x, y, orientation):
        """
        Metoda sluzaca do umiesczenia statku na mapie, z wykorzystaniem nizej umiesczonych metod klasy
        """
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
                            PopUp("Can't place ship here, ship collision")
                            break
                else:
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
                            PopUp("Can't place ship here, ship collision")
                            break
                else:
                    PopUp("Can't place ship here, game map out of range")

    def colissionChecker(self, shipSize, x, y, orient):
        """
        Przed umiesczeniem kazdego statku na planszy, tablica gry jest sprawdzana.
        Jezeli na polach, na ktorych ma byc umiesczony statek, w tablicy gry znajduje sie "X" lub 1
        nie bedzie to mozliwe i funkcja zwroci True
        """
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
        """
        Jezeli dany okret zostanie umiesczany na planszy, to pola wokol niego w tablicy gry zostaja
        ustawione na wartosc "X", aby nie bylo mozliwe umiesczenie okretu, ktory bedzie sie stykal z wlasnie
        umiesczonym bokami lub rogami
        """
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
        """
        Jezeli dany typ statku zostanie umiesczony na planszy to jego dostepna ilosc, zmniejsza sie o 1.
        """
        if (self.ship == 1):
            self.oneMast.quantity -= 1
        elif (self.ship == 2):
            self.twoMast.quantity -= 1
        elif (self.ship == 3):
            self.threeMast.quantity -= 1
        elif (self.ship == 4):
            self.fourMast.quantity -= 1

    def shipIsAvailable(self):
        """
        Kazdy statek ma ograniczona ilosc, np czteromasztowiec wystepuje w ilosci 1.
        Jezeli wszystkie statki danego typu zostaly juz rozmiesczone, metoda ta blokuje ich
        dalsze rozmiesczanie.
        """
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
        """
        Metoda sluzoaca do ustawienia pola ship, na odpowieni liczbe 1-4, ktora odpowiada kazdemy ze statkow.
        Jest ona przypisana do przyciskow, z konkretnymi statkami do rozmiesczenia w klasie Game.
        Dzieki temu po klikniecu w odpowiedni statek, pole ship jest ustawiana na odpowiednia wartosc i metoda
        setShip wie, o ktory statek chodzi
        """
        self.ship = ship

    def buttonBlocker(self):
        """
        Metoda sluzaca do blokowania przyciskow, jest ona wywolywana, po wcisniecu nowej gry, zapobiega ona
        oddaniu strzalu przez gracza w swoej wlasne pole
        """
        for i in self.playerButtons.values():
            i["state"] = "disabled"
