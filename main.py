import sys
import pygame
from pygame.locals import *
from game import*

"""
This is the main file, where with game loop
"""


game = Game()

if __name__ == "__main__":
    while(not game.gameOver):
        game.checkEvents()



