from game import Game
import pytmx
import pyscroll
from player import Player
from monstre import Monstre
import random
import math
import time
import pygame


class Menu:
    # START = 0
    # QUIT = 1
    # START_TEXT = "START"
    # QUIT_TEXT = "QUIT"

    def __init__(self):

        #Création de la fenètre
        pygame.display.set_mode((1400, 750))
        pygame.display.set_caption("Jeu")

        self.lastDirection = None

        tmx_data = pytmx.util_pygame.load_pygame("biome_jungle.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.screen = pygame.display.get_surface()
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        self.player = Player(350, 350)
        self.monstre1 = Monstre(350, 300, typeMonstre="zombie")
        self.monstre2 = Monstre(500, 600, typeMonstre="boss")
        self.group.add(self.player)
        self.group.add(self.monstre1)
        self.group.add(self.monstre2)

        print(self.monstre1.health)

        self.walls = []
    def run(self):
        clock = pygame.time.Clock()

        font = pygame.font.Font(None, 50)

        background = pygame.image.load('bgoff.jpg').convert_alpha()
        # background = pygame.Surface((1400, 750))
        # background.fill((255, 0, 0))
        # background.set_alpha(120)
        background = pygame.transform.scale(background, (1400, 750))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 0
        # background_rect.x = self.screen.get_width()
        # background_rect.y = self.screen.get_height()
        # print(background_rect.topleft)ls

        start_button = pygame.image.load('buttonstart.png')
        start_button = pygame.transform.scale(start_button, (500, 100))
        start_button_rect = start_button.get_rect()
        start_button_rect.x = math.ceil(self.screen.get_width() / 3.5)
        start_button_rect.y = math.ceil(self.screen.get_width() / 4.5)

        play_button = pygame.image.load('buttonplay.png')
        play_button = pygame.transform.scale(play_button, (500, 100))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = math.ceil(self.screen.get_width() / 3.5)
        play_button_rect.y = math.ceil(self.screen.get_width() / 4.5)

        quit_button = pygame.image.load('Quit.png')
        quit_button = pygame.transform.scale(quit_button, (500, 100))
        quit_button_rect = quit_button.get_rect()
        quit_button_rect.x = math.ceil(self.screen.get_width() / 3.5)
        quit_button_rect.y = math.ceil(self.screen.get_width() / 3)

        banner = pygame.image.load('jack_s_adventure-removebg-preview.png')
        banner = pygame.transform.scale(banner, (800, 80))
        banner_rect = banner.get_rect()
        banner_rect.x = math.ceil(self.screen.get_width() / 4)

        continu = True
        playgame = False
        game = Game()

        self.screen.blit(background, background_rect)
        self.screen.blit(start_button, start_button_rect)
        self.screen.blit(quit_button, quit_button_rect)

        while continu:
            # self.screen.blit(background, (1400, 750))
            self.screen.blit(banner, banner_rect)
            self.screen.set_alpha(240)

            pygame.display.update()
            if playgame:
                game.run()
                background = pygame.Surface((1400, 750)).convert_alpha()
                background.fill((0, 0, 0))
                background.set_alpha(140)
                self.screen.blit(background, background_rect)
                self.screen.blit(play_button, play_button_rect)
                self.screen.blit(quit_button, quit_button_rect)
                playgame = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        playgame = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        playgame = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button_rect.collidepoint(event.pos):
                        continu = False

        pygame.quit()