from main import Game
from tkinter import *
import unittest


class TestGame(unittest.TestCase):
    def test_reset(self): #test no 8 #ten nie dziala, nie wiem czy nie trzeba bedzie resetu gry naprawic
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        game.resetGame()
        print(game.enemy.enemyGameTable.values())
        if 1 in game.enemy.enemyGameTable.values():
                assert False
        assert True

    def test_player_shot_empty_field(self): #test no 3
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        x= 0
        y = 0
        for i,j in game.enemy.enemyGameTable.items():
            if(j==0):
                x = i[0]
                y = i[1]
                break
        game.enemy.shotForTests(x,y)
        assert game.enemy.enemyAllShips == 20

    def test_player_shot_good_field(self): #test no 4 ten tez nie dziala, nie wiem czemu sie statki nie odejmuja
        x = 0
        y = 0
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        for i,j in game.enemy.enemyGameTable.items():
            if(j==1):
                x = int(i[0])
                y = int(i[1])
                break
        print("Dlaczego y =",game.enemy.enemyButtons.get((700,200)).winfo_y()) #jakim prawem to nie dziala xD
        game.enemy.enemyButtons[(x,y)].configure(state = "normal") #jak to dziala, czyli pobieramy ten przycisk
        game.enemy.shot(game.enemy.enemyButtons[(x,y)])
        self.assertEquals(game.enemy.enemyAllShips,19)

