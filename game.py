import pygame
import pytmx
import pyscroll
from player import Player
from monstre import Monstre

pygame.init()

class Game:

    def __init__(self):

        #Création de la fenètre
        pygame.display.set_mode((1400, 750))
        pygame.display.set_caption("Jeu")

        tmx_data = pytmx.util_pygame.load_pygame("biome_jungle.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.screen = pygame.display.get_surface()
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)

        self.player = Player(350, 350)
        self.monstre1 = Monstre(350, 300)
        self.monstre2 = Monstre(250, 400)
        self.group.add(self.player)
        self.group.add(self.monstre1)
        self.group.add(self.monstre2)

        print(self.monstre1.health)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move('up')
            self.player.changeAnimation('up')
        if pressed[pygame.K_DOWN]:
            self.player.move('down')
            self.player.changeAnimation('down')
        if pressed[pygame.K_LEFT]:
            self.player.move('left')
            self.player.changeAnimation('left')
        if pressed[pygame.K_RIGHT]:
            self.player.move('right')
            self.player.changeAnimation('right')

    def update(self):
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.moveCanceled()

    def run(self):

        clock = pygame.time.Clock()

        font = pygame.font.Font(None, 50)

        running = True

        while running:
            
            self.player.save_location()
            self.handle_input()
            self.monstre1.targetPlayer(self.player)
            self.update()
            self.group.draw(self.screen)
            self.group.center(self.player.rect.center)
            text = font.render(f"{self.player.health}", True, (231, 70, 42, 255))
            logo = pygame.image.load("heart.png")
            logo = pygame.transform.scale(logo, (50, 50))
            self.screen.blit(logo, (1320, 680))
            self.screen.blit(text, (1250, 690))
            pygame.display.flip()
            for sprite in self.group.sprites():
                if isinstance(sprite, Monstre):
                    print(self.group.sprites().count)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #Si le joueur touche le monstre, il perd de la vie
                #Si la vie du joueur est à 0, il respawn
                
                if(self.player.feet.colliderect(self.monstre1.feet) and self.monstre1 is not None):
                    self.player.health -= 10
                if(self.player.health <= 0):
                    self.player.remove(self.group)
                    self.player = Player(350, 350)
                    self.group.add(self.player)
                    self.update()

                #Si la vie du monstre est à 0, il meurt et ne respawn pas

                if(self.monstre1.health <= 0):
                    self.monstre1.remove(self.group)
                    self.update()

            clock.tick(60)

pygame.quit()