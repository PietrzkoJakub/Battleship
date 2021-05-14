import sys
from tkinter import *
from buttonsChecker import *

"""
This is the main file, with game loop
"""
"""
gameOver = False
heightRes = 800
widthRes = 1200
sizeConst = 0.035
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]
buttonVerticalSize = 50
buttonHorizontalSize = 50

"""
"""
def rootInit():
    root = Tk()
    root.geometry(str(widthRes) + "x" + str(heightRes))
    root.resizable(width=True, height=True)
    root.title("Battleship")
    return root

"""

"""
root = Tk()
root.geometry(str(widthRes) + "x" + str(heightRes))
root.resizable(width=True, height=True)
root.title("Battleship")
checker = Checkers(root)


def exit():
    sys.exit(1)

def newGame():
    pass

def resetGame():
    pass

def mainWindowInit():
    #root = rootInit()
    #checker = Checkers(root)
    enemyTable = gameTable()
    playerTable = gameTable()
    fieldMarks(root,alphabet)
    mapButtonsInit(root, checker)
    mainButtonsInit(checker)
    root.mainloop()


def mainButtonsInit(checker:Checkers):
    button1 = Button(text="New Game", command=newGame)
    button1.place(x=0, y=0, height=25, width=80)

    button2 = Button(text="Reset Game", command =resetGame)
    button2.place(x= 0, y=25, height = 25, width =80)

    button3 = Button(text="Exit", command=exit)
    button3.place(x= 0, y=50, height = 25, width =80)


def something():
    checker.change_color(200,200,"blue")


def mapButtonsInit(root, checker):
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

def gameTable():
    gameTable = [[0 for j in range(10)] for i in range(10)]
    return gameTable

if __name__ == '__main__':
    mainWindowInit()


"""
def buttonCreate(root,color,start,end):
    buttons = {}
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            button = Button(root, bg=color)
            button.bind('<Button-1>',lambda event,b = button:changeColor(b))
            button.place(x=i, y=j, height=50, width=50)
            buttons[(i, j)] = button
    return buttons

gameOver = False
heightRes = 800
widthRes = 1200
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]

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
    fieldMarks(root,alphabet)
    playerButtons = buttonCreate(root, "yellow", 100, 600)
    enemyButtons = buttonCreate(root, "red", 650, 1150)
    mainButtonsInit()
    root.mainloop()


def mainButtonsInit():
    button1 = Button(text="New Game")
    button1.place(x=0, y=0, height=25, width=80)

    button2 = Button(text="Reset Game", command =resetGame)
    button2.place(x= 0, y=25, height = 25, width =80)

    button3 = Button(text="Exit", command=exit)
    button3.place(x= 0, y=50, height = 25, width =80)

def leftClick():
    print("Test")


def fieldFillWithLetters(root, letters, startLocation, endLocation):
    j = 0
    for i in range(int(startLocation + 25), int(endLocation + 25), 50):
        label = Label(root, text=letters[j]).place(x=i, y=75)
        j += 1

def changeColor(button:Button):
    button.configure(bg="blue")

def fieldFillWithNumbers(root,xCordinate):
    j = 1
    for i in range(int(100 + 25), int(600 + 25), 50):
        label = Label(root, text=str(j)).place(x=xCordinate, y=i - 5)
        j += 1


def fieldMarks(root, letters):
    fieldFillWithLetters(root, letters, 100, 600)
    fieldFillWithLetters(root, letters, 650, 1150)
    fieldFillWithNumbers(root, 75)
    fieldFillWithNumbers(root, 625)

def gameTable():
    gameTable = [[0 for j in range(10)] for i in range(10)]
    return gameTable

if __name__ == '__main__':
    mainWindowInit()







