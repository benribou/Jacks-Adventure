import pygame
import time
import item
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, health=100, degats=7, max_health=100, coin=0):
        super().__init__()
        self.sprites_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 2
        self.health = health
        self.coin = coin
        self.max_health = max_health
        self.degats = degats
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {

            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)

        }

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
        # if self.EXP == 100:
        #     self.lvlup()

    # def prend_un_coup(self, ennemie):
    #     self.health - ennemie.getter_degats()
    def update(self):
        self.rect.topleft = self.position

    def soin(self, item):
        self.health += item.getter_soin
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def changeAnimation(self, direction):
        if direction == 'up':
            self.image = self.images['up']
        elif direction == 'down':
            self.image = self.images['down']
        elif direction == 'left':
            self.image = self.images['left'] 
        elif direction == 'right':
            self.image = self.images['right'] 
    
    def attackMonster(self, monster):
        monster.health -= 50
        print(monster.health)

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

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprites_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image