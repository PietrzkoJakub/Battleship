from tkinter import *

alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]

def fieldFillWithLetters(root, letters, startLocation, endLocation):
    j = 0
    for i in range(int(startLocation + 25), int(endLocation + 25), 50):
        label = Label(root, text=letters[j]).place(x=i, y=75)
        j += 1

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