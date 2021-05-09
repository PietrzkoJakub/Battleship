import pygame
import sys
from pygame.locals import *

class Game():
    def __init__(self):
        pygame.init()
        self.gameOver = False
        self.upKey = False
        self.downKey = False
        self.startKey = False
        self.backKey = False
        self.HEIGHT = 720
        self.WIDTH = 1280
        self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))#main window with resolution setting in height and weight wvariables
        self.font = pygame.font.get_default_font()
        self.blackColor = (0,0,0) #RGB Format
        self.whiteColor = (255,255,255) #RGB Format
        self.gameOver = False

    def checkEvents(self):
        for event in pygame.event.get():  # handling events
            if event.type == QUIT: #if we clicked on the x button on out screen the game will end
                pygame.quit()
                self.gameOver = True
                sys.exit()

                # For events that occur upon clicking the mouse (left click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


            # Event handling for a range of different key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.gameOver = True
                    sys.exit()
                if event.key == pygame.K_BACKSPACE:
                    self.backKey = True
                if event.key == pygame.K_RETURN:
                    self.startKey = True
                if event.key == pygame.K_UP:
                    self.upKey = True
                if event.key == pygame.K_DOWN:
                    self.downKey = True

    def keysReset(self):
        self.gameOver = False
        self.upKey = False
        self.downKey = False
        self.startKey = False
        self.backKey = False



