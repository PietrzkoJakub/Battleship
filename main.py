import sys
from tkinter import *
from buttonsChecker import *

"""
This is the main file, with game loop
"""

M = 20
N = 10

gameOver = False
heightRes = 800
widthRes = 1200
sizeConst = 0.035
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]
buttonVerticalSize = 50
buttonHorizontalSize = 50




def rootInit():
    root = Tk()
    root.geometry(str(widthRes) + "x" + str(heightRes))
    root.resizable(width=True, height=True)
    root.title("Battleship")
    return root

def exit():
    sys.exit(1)

def newGame():
    pass

def resetGame():
    pass

def mainWindowInit():
    root = rootInit()
    mainButtonsInit()
    fieldMarks(root,alphabet)
    mapButtonsInit(root)
    root.mainloop()

def mainButtonsInit():
    button1 = Button(text="New Game", command=newGame)
    button1.place(x=0, y=0, height=25, width=80)

    button2 = Button(text="Reset Game", command=resetGame())
    button2.place(x= 0, y=25, height = 25, width =80)

    button3 = Button(text="Exit", command=exit)
    button3.place(x= 0, y=50, height = 25, width =80)

    testButton = Button(text = "test")
    testButton.place(x=500, y=500, height = 50, width =50)

def mapButtonsInit(root):
    checker = Checkers(root)
    buttonCreate(checker,"yellow",100,600)
    buttonCreate(checker,"red",650,1150)

def buttonCreate(checker,color,start,end):
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            checker.create_button(color, i, j)



def fieldFillWithLetters(root, letters, startLocation, endLocation):
    j = 0
    for i in range(int(startLocation + buttonVerticalSize / 2), int(endLocation + buttonVerticalSize / 2), 50):
        label = Label(root, text=letters[j]).place(x=i, y=75)
        j += 1

def fieldFillWithNumbers(root,xCordinate):
    j = 1
    for i in range(int(100 + buttonVerticalSize / 2), int(600 + buttonVerticalSize / 2), 50):
        label = Label(root, text=str(j)).place(x=xCordinate, y=i - 5)
        j += 1


def fieldMarks(root, letters):
    fieldFillWithLetters(root, letters, 100, 600)
    fieldFillWithLetters(root, letters, 650, 1150)
    fieldFillWithNumbers(root, 75)
    fieldFillWithNumbers(root, 625)


if __name__ == '__main__':
    mainWindowInit()







