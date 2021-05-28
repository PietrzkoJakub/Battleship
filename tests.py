from main import Game
from tkinter import *
import unittest
from exceptions import *


class TestGame(unittest.TestCase):


    def test_correct_placement_ships_by_player_and_starting_new_game(self): #test no 2
        """
        Jezeli wsyzstkie okrety gracza zostaly rozmiesczone to po wcisnieciu nowej gry wszystkie okrety przeciwnika,powinny
        zostac rozmiesczone
        """
        root = Tk()
        game = Game(root)
        game.player.oneMast.quantity = 0
        game.player.twoMast.quantity = 0
        game.player.threeMast.quantity = 0
        game.player.fourMast.quantity = 0
        game.newGame()
        if 1 in game.enemy.enemyGameTable.values():
            assert True
        else:
            assert False


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
        game.enemy.enemyButtons[(x, y)].configure(state="normal")
        game.enemy.shot(x,y)
        self.assertEquals(game.enemy.enemyAllShips, 20)

    def test_player_shot_good_field(self): #test no 4
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
        game.enemy.enemyButtons[(x,y)].configure(state = "normal")
        game.enemy.shot(x,y)
        self.assertEquals(game.enemy.enemyAllShips,19)

    def test_shoot_again_with_same_field_with_ship(self): #test no 7
        x = 0
        y = 0
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        for i, j in game.enemy.enemyGameTable.items():
            if (j == 1):
                x = int(i[0])
                y = int(i[1])
                break
        game.enemy.enemyButtons[(x, y)].configure(state="normal")
        game.enemy.shot(x, y)
        self.assertRaises(YouAlreadyShootHereException,lambda: game.enemy.shot(x, y))

    def test_shoot_again_with_same_empty_field(self): #test no 6 ale to tez mozna inaczej zrobic bez wyjatkow, ale trzeba pomyslec nad tym
        x = 0
        y = 0
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        for i, j in game.enemy.enemyGameTable.items():
            if (j == 0):
                x = int(i[0])
                y = int(i[1])
                break
        game.enemy.enemyButtons[(x, y)].configure(state="normal")
        game.enemy.shot(x, y)
        self.assertRaises(YouAlreadyShootHereException, lambda: game.enemy.shot(x, y))

    def test_reset(self): #test no 8
        root = Tk()
        game = Game(root)
        game.enemy.pleaceEnemyShipsOnMap()
        game.resetGame()
        print(game.enemy.enemyGameTable.values())
        if 1 in game.enemy.enemyGameTable.values():
                assert False
        assert True

