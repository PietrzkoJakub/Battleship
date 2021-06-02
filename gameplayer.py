from tkinter import *
from random import *
from ships import  Ship

class GamePlayer:
    def gameTableInit(self,pixels):
        """
        Metoda sluzaca do stworzenia tablicy gry przeciwnika i gracza.
        Tablica gry jest slownik, w ktorym klucze to wspolrzedne przyciskow, a wartosci
        to reprezantacja przyciskow:
        0 - puste pole
        1- pole ze statkiem
        X - puste pole, blokujace mozliwosc wystapienia kolizji
        Po uruchomieniu programu, kazdy przycisk jest inicjowana wartoscia 0.
        """
        fields = {(i,j): 0 for i in range(100+pixels, 600+pixels,50) for  j in range(100, 600, 50)}
        return fields

    def buttonsCreate(self):
        pass

    def setShip(self):
        pass

    def colissionChecker(self):
        pass

    def fieldBlocker(self):
        pass
