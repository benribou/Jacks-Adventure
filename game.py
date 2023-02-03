import math
import pytmx
import pyscroll
import time
from monstre import Monstre
from player import Player
from objets import Chest
import  pygame
lastDirection = None

pygame.init()

class Game:

    def __init__(self):

        #Création de la fenètre
        pygame.display.set_mode((1400, 750))
        pygame.display.set_caption("Jeu")
        pygame.font.init()

        self.lastDirection = None

        tmx_data = pytmx.util_pygame.load_pygame("biome_jungle.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.screen = pygame.display.get_surface()
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)

        self.player = Player(350, 350)
        self.monstre1 = Monstre(350, 300, typeMonstre="gorille", degats=7, max_health=30)
        self.monstre2 = Monstre(500, 600, typeMonstre="gorille", degats=7, max_health=30)
        self.monstre3 = Monstre(877, 182, typeMonstre="grenouille", degats=5, max_health=20)
        self.monstre4 = Monstre(823, 741, typeMonstre="grenouille", degats=5, max_health=20)
        self.monstre5 = Monstre(277, 804, typeMonstre="grenouille", degats=5, max_health=20)
        self.group.add(self.player)
        self.group.add(self.monstre1)
        self.group.add(self.monstre2)
        self.group.add(self.monstre3)
        self.group.add(self.monstre4)
        self.group.add(self.monstre5)

        self.monstresListCheckjungle = [self.monstre1, self.monstre2, self.monstre3, self.monstre4, self.monstre5]

        # biome glace

        self.monstre6 = Monstre(220, 1149, typeMonstre="cerf", degats=9, max_health=40)
        self.monstre7 = Monstre(454, 1481, typeMonstre="loup", degats=12, max_health=50)
        self.monstre8 = Monstre(224, 1713, typeMonstre="loup", degats=12, max_health=50)
        self.monstre9 = Monstre(865, 1361, typeMonstre="cerf", degats=9, max_health=40)
        self.monstre10 = Monstre(824, 1080, typeMonstre="cerf", degats=9, max_health=40)
        self.monstre11 = Monstre(640, 1688, typeMonstre="loup", degats=12, max_health=50)
        self.group.add(self.monstre6)
        self.group.add(self.monstre7)
        self.group.add(self.monstre8)
        self.group.add(self.monstre9)
        self.group.add(self.monstre10)
        self.group.add(self.monstre11)

        self.monstresListCheckglace = [self.monstre6, self.monstre7, self.monstre8, self.monstre9, self.monstre10, self.monstre11]

        # Biome Plage

        self.monstre12 = Monstre(1094, 1575, typeMonstre="crabe", degats=15, max_health=70)
        self.monstre13 = Monstre(1236, 1339, typeMonstre="tortue", degats=13, max_health=60)
        self.monstre14 = Monstre(1254, 1091, typeMonstre="crabe", degats=15, max_health=70)
        self.monstre15 = Monstre(1765, 1065, typeMonstre="crabe", degats=15, max_health=70)
        self.monstre16 = Monstre(1619, 1506, typeMonstre="tortue", degats=13, max_health=60)
        self.monstre17 = Monstre(1559, 1752, typeMonstre="tortue", degats=13, max_health=60)
        self.group.add(self.monstre12)
        self.group.add(self.monstre13)
        self.group.add(self.monstre14)
        self.group.add(self.monstre15)
        self.group.add(self.monstre16)
        self.group.add(self.monstre17)

        self.monstresListCheckplage = [self.monstre12, self.monstre13, self.monstre14, self.monstre15, self.monstre16, self.monstre17]

        # biome desert

        self.monstre18 = Monstre(1111, 731, typeMonstre="singe", degats=19, max_health=70)
        self.monstre19 = Monstre(1179, 469, typeMonstre="pumba", degats=22, max_health=80)
        self.monstre20 = Monstre(1438, 188, typeMonstre="pumba", degats=22, max_health=80)
        self.monstre21 = Monstre(1706, 72, typeMonstre="singe", degats=19, max_health=70)
        self.monstre22 = Monstre(1794, 810, typeMonstre="pumba", degats=22, max_health=80)
        self.monstre23 = Monstre(1785, 310, typeMonstre="singe", degats=19, max_health=70)
        self.group.add(self.monstre18)
        self.group.add(self.monstre19)
        self.group.add(self.monstre20)
        self.group.add(self.monstre21)
        self.group.add(self.monstre22)
        self.group.add(self.monstre23)

        self.monstresListCheckdesert = [self.monstre18, self.monstre19, self.monstre20, self.monstre21, self.monstre22, self.monstre23]

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move('up')
            self.lastDirection = 'up'
            self.player.changeAnimation('up')
        if pressed[pygame.K_DOWN]:
            self.player.move('down')
            self.lastDirection = 'down'
            self.player.changeAnimation('down')
        if pressed[pygame.K_LEFT]:
            self.player.move('left')
            self.lastDirection = 'left'
            self.player.changeAnimation('left')
        if pressed[pygame.K_RIGHT]:
            self.player.move('right')
            self.lastDirection = 'right'
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
            self.update()
            self.group.draw(self.screen)
            self.group.center(self.player.rect.center)

            TextXp = font.render(f"{self.player.level} ({self.player.exp}/{round(self.player.xpNeedToUp())})", True, (255, 255, 255))
            xpLogo = pygame.image.load("level.png")
            xpLogo = pygame.transform.scale(xpLogo, (48, 48))
            self.screen.blit(xpLogo, (1320, 680))
            self.screen.blit(TextXp, (1150, 690))

            text = font.render(f"{self.player.health}", True, (255, 255, 255))
            logo = pygame.image.load("heart.png")
            logo = pygame.transform.scale(logo, (48, 48))
            self.screen.blit(logo, (1320, 500))
            self.screen.blit(text, (1250, 510)) 

            coinText = font.render(f"{self.player.coin}", True, (255, 255, 255))
            coinLogo = pygame.image.load("coin.png")
            coinLogo = pygame.transform.scale(coinLogo, (48, 48))
            self.screen.blit(coinLogo, (1320, 620))
            self.screen.blit(coinText, (1270, 630))

            # Affichage des dégats d'attaque

            TextSword = font.render(f"{self.player.degats}", True, (255, 255, 255))
            swordLogo = pygame.image.load("sword.png")
            swordLogo = pygame.transform.scale(swordLogo, (48, 48))
            self.screen.blit(swordLogo, (1320, 560))
            self.screen.blit(TextSword, (1270, 570))

            # Affichage de l'experience du joueur
            
            for sprite in self.group.sprites():
                if isinstance(sprite, Monstre):
                    numberOfSprite = sprite
                    if(math.sqrt((sprite.position[0] - self.player.position[0])**2 + (sprite.position[1] - self.player.position[1])**2) <= 200):
                        sprite.targetPlayer(self.player)
                    if(math.sqrt((sprite.position[0] - self.player.position[0])**2 + (sprite.position[1] - self.player.position[1])**2) <= 50):
                        sprite.attackPlayer(self.player)

                    if(sprite.health <= 0):
                        
                        self.monstresListCheckjungle.remove(sprite)
                        if(len(self.monstresListCheckjungle) == 0):

                            self.monstre1 = Monstre(350, 300, typeMonstre="gorille", degats=7, max_health=30)
                            self.monstre2 = Monstre(500, 600, typeMonstre="gorille", degats=7, max_health=30)
                            self.monstre3 = Monstre(877, 182, typeMonstre="gorille", degats=7, max_health=30)
                            self.monstre4 = Monstre(823, 741, typeMonstre="gorille", degats=7, max_health=30)
                            self.monstre5 = Monstre(277, 804, typeMonstre="gorille", degats=7, max_health=30)
                            self.group.add(self.monstre1)
                            self.group.add(self.monstre2)
                            self.group.add(self.monstre3)
                            self.group.add(self.monstre4)
                            self.group.add(self.monstre5)
                            self.monstresListCheckjungle = [self.monstre1, self.monstre2, self.monstre3, self.monstre4, self.monstre5]

                        self.monstresListCheckglace.remove(sprite)
                        if len(self.monstresListCheckglace) == 0:
                            self.monstre6 = Monstre(220, 1149, typeMonstre="cerf", degats=9, max_health=40)
                            self.monstre7 = Monstre(454, 1481, typeMonstre="loup", degats=12, max_health=50)
                            self.monstre8 = Monstre(224, 1713, typeMonstre="loup", degats=12, max_health=50)
                            self.monstre9 = Monstre(865, 1361, typeMonstre="cerf", degats=9, max_health=40)
                            self.monstre10 = Monstre(824, 1080, typeMonstre="cerf", degats=9, max_health=40)
                            self.monstre11 = Monstre(640, 1688, typeMonstre="loup", degats=12, max_health=50)
                            self.group.add(self.monstre6)
                            self.group.add(self.monstre7)
                            self.group.add(self.monstre8)
                            self.group.add(self.monstre9)
                            self.group.add(self.monstre10)
                            self.group.add(self.monstre11)

                            self.monstresListCheckglace = [self.monstre6, self.monstre7, self.monstre8, self.monstre9, self.monstre10, self.monstre11]

                        self.monstresListCheckplage.remove(sprite)
                        if len(self.monstresListCheckplage) == 0:
                            self.monstre12 = Monstre(1094, 1575, typeMonstre="crabe", degats=15, max_health=70)
                            self.monstre13 = Monstre(1236, 1339, typeMonstre="tortue", degats=13, max_health=60)
                            self.monstre14 = Monstre(1254, 1091, typeMonstre="crabe", degats=15, max_health=70)
                            self.monstre15 = Monstre(1765, 1065, typeMonstre="crabe", degats=15, max_health=70)
                            self.monstre16 = Monstre(1619, 1506, typeMonstre="tortue", degats=13, max_health=60)
                            self.monstre17 = Monstre(1559, 1752, typeMonstre="tortue", degats=13, max_health=60)
                            self.group.add(self.monstre12)
                            self.group.add(self.monstre13)
                            self.group.add(self.monstre14)
                            self.group.add(self.monstre15)
                            self.group.add(self.monstre16)
                            self.group.add(self.monstre17)

                            self.monstresListCheckplage = [self.monstre12, self.monstre13, self.monstre14, self.monstre15, self.monstre16, self.monstre17]

                        self.monstresListCheckdesert.remove(sprite)
                        if len(self.monstresListCheckdesert) == 0:
                            self.monstre18 = Monstre(1111, 731, typeMonstre="singe", degats=19, max_health=70)
                            self.monstre19 = Monstre(1179, 469, typeMonstre="pumba", degats=22, max_health=80)
                            self.monstre20 = Monstre(1438, 188, typeMonstre="pumba", degats=22, max_health=80)
                            self.monstre21 = Monstre(1706, 72, typeMonstre="singe", degats=19, max_health=70)
                            self.monstre22 = Monstre(1794, 810, typeMonstre="pumba", degats=22, max_health=80)
                            self.monstre23 = Monstre(1785, 310, typeMonstre="singe", degats=19, max_health=70)
                            self.group.add(self.monstre18)
                            self.group.add(self.monstre19)
                            self.group.add(self.monstre20)
                            self.group.add(self.monstre21)
                            self.group.add(self.monstre22)
                            self.group.add(self.monstre23)

                            self.monstresListCheckdesert = [self.monstre18, self.monstre19, self.monstre20, self.monstre21, self.monstre22, self.monstre23]

                        self.player.coin += sprite.returnRewardCoin()
                        self.player.exp += sprite.returnRewardXp()
                        self.player.increaseLevel()
                        self.coffre1 = Chest(500, 500)

                        if(self.player.health + 30 <= self.player.max_health):
                            self.player.health += 30

                        self.group.add(self.coffre1)
                        self.update()

                    if(math.sqrt((sprite.position[0] - self.player.position[0])**2 + (sprite.position[1] - self.player.position[1])**2) <= 75):
                        if(self.lastDirection == 'up' and sprite.position[1] < self.player.position[1] or self.lastDirection == 'down' and sprite.position[1] > self.player.position[1] or self.lastDirection == 'left' and sprite.position[0] < self.player.position[0] or self.lastDirection == 'right' and sprite.position[0] > self.player.position[0]):

                            textHealthMonstre = font.render(f"{sprite.health}", True, (255, 255, 255))
                            healthMonstreLogo = pygame.image.load("heart.png")
                            healthMonstreLogo = pygame.transform.scale(healthMonstreLogo, (48, 48))
                            self.screen.blit(textHealthMonstre, (75, 690))
                            self.screen.blit(healthMonstreLogo, (10, 680))

                            textDamageMonstre = font.render(f"{sprite.degats}", True, (255, 255, 255))
                            damageMonstreLogo = pygame.image.load("sword.png")
                            damageMonstreLogo = pygame.transform.scale(damageMonstreLogo, (48, 48))
                            self.screen.blit(damageMonstreLogo, (10, 620))
                            self.screen.blit(textDamageMonstre, (75, 630))

                            if(sprite.degats < self.player.degats and sprite.max_health < self.player.max_health):
                                difficulty = "Facile"
                            elif(sprite.degats > self.player.degats and sprite.max_health > self.player.max_health):
                                difficulty = "Difficile"
                            elif(sprite.degats > self.player.degats and sprite.max_health < self.player.max_health):
                                difficulty = "Modérée"
                            elif(sprite.degats < self.player.degats and sprite.max_health > self.player.max_health):
                                difficulty = "Modérée"
                            elif(sprite.degats == self.player.degats and sprite.max_health == self.player.max_health):
                                difficulty = "Normale"
                            elif(sprite.degats == self.player.degats and sprite.max_health < self.player.max_health):
                                difficulty = "Facile"
                            elif(sprite.degats == self.player.degats and sprite.max_health > self.player.max_health):
                                difficulty = "Difficile"
                            elif(sprite.degats > self.player.degats and sprite.max_health == self.player.max_health):
                                difficulty = "Difficile"
                            elif(sprite.degats < self.player.degats and sprite.max_health == self.player.max_health):
                                difficulty = "Facile"
                            if(difficulty == "Facile"):    
                                textDifficultyMonstre = font.render(f"{difficulty}", True, (255, 255, 255))
                            if(difficulty == "Normale"):
                                textDifficultyMonstre = font.render(f"{difficulty}", True, (61, 195, 104))
                            if(difficulty == "Modérée"):
                                textDifficultyMonstre = font.render(f"{difficulty}", True, (255, 167, 47))
                            if(difficulty == "Difficile"):
                                textDifficultyMonstre = font.render(f"{difficulty}", True, (255, 9, 9))
                            difficultyMonstreLogo = pygame.image.load("difficulty.png")
                            difficultyMonstreLogo = pygame.transform.scale(difficultyMonstreLogo, (48, 48))
                            self.screen.blit(difficultyMonstreLogo, (10, 560))
                            self.screen.blit(textDifficultyMonstre, (75, 570))

                if isinstance (sprite, Chest):
                    if(math.sqrt((sprite.position[0] - self.player.position[0])**2 + (sprite.position[1] - self.player.position[1])**2) <= 50):
                        textChest = pygame.font.Font(None, 35).render("Ouvrir [A]", True, (255, 255, 255))
                        self.screen.blit(textChest, (570, 700))

            if self.player.health <= 0:
                self.player.remove(self.group)
                self.player = Player(700, 350)
                self.group.add(self.player)
                self.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False
            
                for sprite in self.group.sprites():
                    if isinstance(sprite, Monstre):
                        if pygame.key.get_pressed()[pygame.K_SPACE] and math.sqrt((sprite.position[0] - self.player.position[0])**2 + (sprite.position[1] - self.player.position[1])**2) <= 50:
                            if(self.lastDirection == 'up' and sprite.position[1] < self.player.position[1]):
                                self.player.attackMonster(sprite)
                            if(self.lastDirection == 'down' and sprite.position[1] > self.player.position[1]):
                                self.player.attackMonster(sprite)
                            if(self.lastDirection == 'left' and sprite.position[0] < self.player.position[0]):
                                self.player.attackMonster(sprite)
                            if(self.lastDirection == 'right' and sprite.position[0] > self.player.position[0]):
                                self.player.attackMonster(sprite)

                #if(self.player.feet.colliderect(self.monstre1.feet) and self.monstre1 is not None):
                #    self.player.health -= 10
                #if(self.player.health <= 0):
                #    self.player.remove(self.group)
                #    self.player = Player(350, 350)
                #    self.group.add(self.player)
                #    self.update()

                #Si la vie du monstre est à 0, il meurt et ne respawn pas
            
            pygame.display.flip()

            clock.tick(60)

pygame.quit()