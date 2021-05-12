import sys
from tkinter import *

"""
This is the main file, with game loop
"""

display = Tk()
gameOver = False
heightRes = 1080
widthRes = 1920
sizeConst = 0.035
alphabet = [chr(i) for i in range(ord('A'),ord('J')+1)]

def exit():
    sys.exit(1)

def newGame():
    pass

def resetGame():
    pass

def mainWindowInit():
    display.geometry(str(widthRes) + "x" + str(heightRes))
    display.resizable(width = True, height = True)
    mainButtonsInit()
    mapButtonsInit()
    fieldMarks(alphabet)
    display.mainloop()

def mainButtonsInit():
    button1 = Button(text="New Game", command=newGame)
    button1.place(x=0, y=0, height=25, width=80)

    button2 = Button(text="Reset Game", command=resetGame())
    button2.place(x= 0, y=25, height = 25, width =80)


    button3 = Button(text="Exit", command=exit)
    button3.place(x= 0, y=50, height = 25, width =80)

    testButton = Button(text = "test")
    testButton.place(x=500, y=500, height = 50, width =50)



buttonVerticalSize = 50
buttonHorizontalSize = 50

def mapButtonsInit():
    for i in range(100,600,50):
        for j in range(100,600,50):
            button = Button(bg = "yellow")
            button.place(x=i, y=j, height=50, width=50)

    for i in range(650, 1150, 50):
        for j in range(100, 600, 50):
            button = Button(bg="red")
            button.place(x=i, y=j, height=50, width=50)

def fieldMarks(letters):
    j = 0
    for i in range(int(100+buttonVerticalSize/2),int(600+buttonVerticalSize/2),50):
        label = Label(display,text = letters[j]).place(x=i,y=75)
        j += 1
    j = 0
    for i in range(int(650 + buttonVerticalSize / 2), int(1150 + buttonVerticalSize / 2), 50):
        label = Label(display, text=letters[j]).place(x=i, y=75)
        j += 1
    j = 1
    for i in range(int(100 + buttonVerticalSize / 2), int(600 + buttonVerticalSize / 2), 50):
        label = Label(display, text=str(j)).place(x=75, y=i-5)
        j += 1
    j = 1
    for i in range(int(100 + buttonVerticalSize / 2), int(600 + buttonVerticalSize / 2), 50):
        label = Label(display, text=str(j)).place(x=625, y=i-5)
        j += 1




if __name__ == "__main__":
    mainWindowInit()




