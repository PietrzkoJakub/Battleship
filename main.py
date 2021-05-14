import sys
from tkinter import *
from buttonsChecker import *
import mainButtons as mb

heightRes = 800
widthRes = 1200
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]

def rootInit():
    root = Tk()
    root.geometry(str(widthRes) + "x" + str(heightRes))
    root.resizable(width=True, height=True)
    root.title("Battleship")
    return root


def mainWindowInit():
    root = rootInit()
    fieldMarks(root,alphabet)
    playerButtons = buttonCreate(root, "green", 100, 600)
    enemyButtons = buttonCreate(root, "yellow", 650, 1150)
    mb.MainButtons()
    root.mainloop()


def buttonCreate(root,color,start,end):
    buttons = {}
    for i in range(start, end, 50):
        for j in range(100, 600, 50):
            button = Button(root, bg=color)
            button.bind('<Button-1>',lambda event,b = button:changeColor(b))
            button.place(x=i, y=j, height=50, width=50)
            buttons[(i, j)] = button
    return buttons

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







