import pygame
import math
import random
import time

class Monstre(pygame.sprite.Sprite):
    def __init__(self, x, y, typeMonstre, degats, max_health):
        super().__init__()
        self.typeMonstre = typeMonstre
        self.sprites_sheet = pygame.image.load(f"{self.typeMonstre}.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 1
        self.max_health = max_health
        self.health = max_health
        self.degats = degats
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.timerPreviousAttack = 0

    #Chercher les coordonnées du joueur et le suivre
    def getter_degats(self):
        return self.degats
    def targetPlayer(self, player):
        if player.position[0] > self.position[0] and (math.sqrt((self.position[0] - player.position[0])**2 + (self.position[1] - player.position[1])**2)) > 35:
            self.position[0] += self.speed
        if player.position[0] < self.position[0] and (math.sqrt((self.position[0] - player.position[0])**2 + (self.position[1] - player.position[1])**2)) > 35:
            self.position[0] -= self.speed
        if player.position[1] > self.position[1] and (math.sqrt((self.position[0] - player.position[0])**2 + (self.position[1] - player.position[1])**2)) > 35:
            self.position[1] += self.speed
        if player.position[1] < self.position[1] and (math.sqrt((self.position[0] - player.position[0])**2 + (self.position[1] - player.position[1])**2)) > 35:
            self.position[1] -= self.speed

    def attackPlayer(self, player):
        seconds = time.time()
        if self.timerPreviousAttack == 0:
            player.health -= self.getter_degats()
            self.timerPreviousAttack = seconds
        elif(seconds - self.timerPreviousAttack >= 0.75):
            player.health -= self.getter_degats()
            self.timerPreviousAttack = seconds
            print(player.health)

    def returnRewardCoin(self):
        if self.typeMonstre == "gorille":
            return random.randint(1, 4)
        if self.typeMonstre == "boss":
            return random.randint(2, 5)

    def returnRewardXp(self):
        if self.typeMonstre == "gorille":
            return 20
        if self.typeMonstre == "grenouille":
            return 20

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveCanceled(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprites_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image