import pygame
import pytmx
import pyscroll

from game import Game

if __name__ == "__main__":

    pygame.init()
    game = Game()
    game.run()