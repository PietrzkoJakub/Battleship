from tkinter import *

class FieldsMark:
    def __init__(self,root,xStart,xEnd,xCord):
        self.root = root
        self.alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]
        self.xStart = xStart
        self.xEnd = xEnd
        self.xCordinate = xCord

    def fieldFillWithLetters(self):
        j = 0
        for i in range(self.xStart + 25, self.xEnd + 25, 50):
            label = Label(self.root, text=self.alphabet[j]).place(x=i, y=75)
            j += 1

    def fieldFillWithNumbers(self):
        j = 1
        for i in range(125, 625, 50):
            label = Label(self.root, text=str(j)).place(x=self.xCordinate, y=i - 5)
            j += 1

