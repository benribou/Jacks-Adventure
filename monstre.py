import pygame
import math
import random

class Monstre(pygame.sprite.Sprite):
    def __init__(self, x, y, typeMonstre, health=100, degats=7, max_health=100):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 1
        self.health = health
        self.max_health = max_health
        self.degats = degats
        self.typeMonstre = typeMonstre
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    #Chercher les coordonnées du joueur et le suivre

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
        player.health -= 50
        print(player.health)

    def returnReward(self):
        if self.typeMonstre == "zombie":
            return random.randint(1, 4)
        if self.typeMonstre == "boss":
            return random.randint(2, 5)

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveCanceled(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom