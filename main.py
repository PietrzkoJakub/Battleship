import sys
from tkinter import *

"""
This is the main file, with game loop
"""

def mainWindowInit():
    display = Tk()
    display.resizable(width = True, height = True)

    welcome = Label(display,text = "Welcome")
    welcome.grid(row = 0, column= 0) #text location on the window(table)

    #Frame
    frame = Frame(display,borderwidth = 4)
    frame.grid(row=0, column=1)
    frame.config(background='black')
    lab1 = Label(frame, text='Ramka')
    lab1.grid(sticky=E, row=0, column=0, padx=5, pady=5)
    display.mainloop()



gameOver = False

if __name__ == "__main__":
    while(not gameOver):
        #mainWindowInit()
        input("Press return to exit")
        gameOver = True



