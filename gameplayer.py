from tkinter import *
from random import *
from ships import  Ship

class GamePlayer: #tu mozna dict compershion
    def gameTableInit(self,pixels):
        fields = {(i,j): 0 for i in range(100+pixels, 600+pixels,50) for  j in range(100, 600, 50)}
        return fields

    def setShip(self):
        pass

    def colissionChecker(self):
        pass

    def fieldBlocker(self):
        pass