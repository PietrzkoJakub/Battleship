import sys
import pygame
from pygame.locals import *
"""
This is the main file, where with game loop
"""

gameOver = False


if __name__ == "__main__":

    while(not gameOver):
        print("Welcome to my game")
        print("Press 1 to exit")
        a = int(input())
        if a == 1:
            gameOver = True
