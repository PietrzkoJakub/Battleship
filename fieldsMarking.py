from tkinter import *

class FieldsMark:
    def __init__(self,root,xStart,xEnd,xCord):
        self.root = root
        self.alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]
        self.xS = xStart
        self.xE = xEnd
        self.xCordinate = xCord

    def fieldFillWithLetters(self):
        j = 0
        for i in range(self.xS + 25, self.xE+25, 50):
            label = Label(self.root, text=self.alphabet[j]).place(x=i, y=75)
            j += 1

    def fieldFillWithNumbers(self):
        j = 1
        for i in range(125, 625, 50):
            label = Label(self.root, text=str(j)).place(x=self.xCordinate, y=i - 5)
            j += 1




"""
def fieldMarks(root):
    letters = alphabetInit()
    fieldFillWithLetters(root, letters, 100, 600)
    fieldFillWithLetters(root, letters, 650, 1150)
    fieldFillWithNumbers(root, 75)
    fieldFillWithNumbers(root, 625)


def printWhereX(gameTable):
    counter = 0
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            if(gameTable[(i,j)]=="X"):
                print("(x = {}, y = {})".format(i,j))
                counter += 1
    print(counter)




def printWhereOne(gameTable):
    counter = 0
    for i in range(100, 600, 50):
        for j in range(100, 600, 50):
            if(gameTable[(i,j)]==1):
                print("("+i+","+j+")")
                counter += 1
    print(counter)
"""
