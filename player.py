import pygame
import time
from animation import AnimateSprite

class Player(AnimateSprite):

    def __init__(self, x, y, health=100, degats=10, max_health=100, coin=0, level=1, exp=0):
        super().__init__()
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.health = health
        self.coin = coin
        self.max_health = max_health
        self.degats = degats
        self.level = level
        self.exp = exp
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.timerPreviousAttack = 0

    def getter_degats(self):
        return self.degats

    def setter_degats(self, degats):
        self.degats = degats

    def getter_health(self):
        return self.health

    def setter_health(self, health):
        self.health = health

    def getter_niv(self):
        return self.niv

    def setter_niv(self, niv):
        self.niv = niv

    def getter_coin(self):
        return self.coin

    def setter_coin(self, coin):
        self.coin = coin

    def getter_maxHealth(self):
        return self.maxHealth

    def setter_maxHealth(self, maxHealth):
        self.maxHealth = maxHealth

    def getter_EXP(self):
        return self.EXP

    def setter_EXP(self, EXP):
        self.EXP = EXP
    
    def attackMonster(self, monster):
        seconds = time.time()
        if self.timerPreviousAttack == 0:
            monster.health -= self.getter_degats()
            self.timerPreviousAttack = seconds
        elif(seconds - self.timerPreviousAttack >= 0.75):
            monster.health -= self.getter_degats()
            self.timerPreviousAttack = seconds
            print(monster.health)
    
    def xpNeedToUp(self):
        return 100 + (100 * self.level) * 0.5

    def increaseLevel(self):
        if(self.exp >= self.xpNeedToUp()):
            self.exp = 0
            self.level += 1
            self.max_health += 20
            self.health = self.max_health
            self.degats += 1

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveCanceled(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move(self, direction):
        if direction == 'up':
            self.position[1] -= self.speed
        elif direction == 'down':
            self.position[1] += self.speed
        elif direction == 'left':
            self.position[0] -= self.speed
        elif direction == 'right':
            self.position[0] += self.speed