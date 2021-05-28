from tkinter import *

class FieldsMark:
    def __init__(self,root,xStart,xEnd,xCord):
        self.root = root
        self.alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]
        self.lettersPosition = [i for i in range(xStart + 25, xEnd + 25, 50)]
        self.numbersPosition = [i for i in range(125, 625, 50)]
        self.xCordinate = xCord

    def fieldFillWithLetters(self):
        j = 0
        for i in self.lettersPosition:
            Label(self.root, text=self.alphabet[j]).place(x=i, y=75)
            j += 1

    def fieldFillWithNumbers(self):
        j = 1
        for i in self.numbersPosition:
            Label(self.root, text=str(j)).place(x=self.xCordinate, y=i - 5)
            j += 1

