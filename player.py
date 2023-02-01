import pygame
import time

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, health=100, degats=7, max_health=100):
        super().__init__()
        self.sprites_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 2
        self.health = health
        self.max_health = max_health
        self.degats = degats
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {

            'down': self.get_image(0, 0),
            'left': [self.get_image(0, 32), self.get_image(32, 32), self.get_image(64, 32)],
            'right': self.get_image(0, 64),
            'up': [self.get_image(0, 96), self.get_image(32, 96), self.get_image(64, 96)]

        }

    def changeAnimation(self, direction):
        if direction == 'up':
            for image in self.images['up']:
                self.image = image
            
        elif direction == 'down':
            self.image = self.images['down']
        elif direction == 'left':
            for image in self.images['left']:
                self.image = image
        elif direction == 'right':
            self.image = self.images['right'] 
    
    def attackMonster(self, monster):
        if self.feet.colliderect(monster.feet):
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