import pygame
import pytmx
import pyscroll

from menu import Menu

if __name__ == "__main__":

    pygame.init()
    menu = Menu()
    menu.run()