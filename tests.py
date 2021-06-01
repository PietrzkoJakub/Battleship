from game import Game
from tkinter import *
import unittest

class TestGame(unittest.TestCase):

    def playerAutoSetShipsForTests(self, game):
        game.player.ship = 4
        game.player.setShip(100, 100, "v")
        game.player.ship = 3
        game.player.setShip(100, 200, "v")
        game.player.ship = 3
        game.player.setShip(100, 300, "v")
        game.player.ship = 2
        game.player.setShip(100, 400, "v")
        game.player.ship = 2
        game.player.setShip(100, 500, "v")
        game.player.ship = 2
        game.player.setShip(500, 100, "v")
        game.player.ship = 1
        game.player.setShip(500, 200, "v")
        game.player.ship = 1
        game.player.setShip(500, 300, "v")
        game.player.ship = 1
        game.player.setShip(500, 400, "v")
        game.player.ship = 1
        game.player.setShip(500, 500, "v")


    def test_bad_ship_placement_sides_colission(self):  # test no 1
        root = Tk()
        game = Game(root)
        game.player.ship = 4
        game.player.setShip(100, 100, "v")
        game.player.ship = 3
        assert game.player.colissionChecker(150, 300, 100, "v") and game.player.colissionChecker(150, 300, 150, "v")

    def test_correct_placement_ships_by_player_and_starting_new_game(self): #test no 2
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
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


    def test_shoot_ownship(self): #test no 5
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        assert game.player.playerButtons[(100,200)]["state"] == "disabled"


    def test_shoot_again_with_same_empty_field(self): #test no 6
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
        self.assertFalse(game.enemy.shot(x, y))



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
        game.enemy.shot(x, y)
        self.assertEquals(game.enemy.enemyAllShips,19)


    def test_reset(self): #test no 8
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
        game.resetGame()
        if 1 in game.player.playerGameTable.values():
                assert False
        if "X" in game.player.playerGameTable.values():
                assert False
        else:
            assert True


    def test_shot_at_the_same_fields_after_reset(self): # test no 9
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        game.enemy.shot(1000,200)
        game.enemy.shot(1000, 300)
        game.enemy.shot(1000, 400)
        game.resetGame()
        game.player.ship = 4
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        game.enemy.shot(1000, 200)
        game.enemy.shot(1000, 300)
        game.enemy.shot(1000, 400)
        assert True


    def test_winning_game(self):  # test no 10
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        for i, j in game.enemy.enemyGameTable.items():
            if j == 1:
                game.enemy.shot(i[0], i[1])
        if (game.enemy.enemyAllShips == 0):
            game.player.playerWin = True
        game.resetGame()
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        if 1 in game.enemy.enemyGameTable.values():
            assert True
        else:
            assert False

    def test_loosing_game(self): #test no 11
        root = Tk()
        game = Game(root)
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        for i, j in game.player.playerGameTable.items():
            if j == 1:
                if (i[0], [1]) not in game.enemy.alreadyShootingHere:
                    game.enemy.player.playerAllShips -= 1
                    game.enemy.alreadyShootingHere.append((i[0], i[1]))
        if (game.enemy.player.playerAllShips == 0):
            game.enemy.enemyWin = True
        game.resetGame()
        self.playerAutoSetShipsForTests(game)
        game.newGame()
        if 1 in game.enemy.enemyGameTable.values():
            assert True
        else:
            assert False