import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprites_sheet = pygame.image.load('player.png')
        self.animation_index = 0
        self.clock = 0
        self.speed = 2
        self.images = {

            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96)
        }

    def changeAnimation(self, direction):
        if direction == 'up':
            self.image = self.images['up'][self.animation_index]
            self.clock += self.speed * 8
            if self.clock >= 100:
                self.animation_index += 1
                if self.animation_index >= len(self.images['up']):
                    self.animation_index = 0
                self.clock = 0

        elif direction == 'down':
            self.image = self.images['down'][self.animation_index]
            self.clock += self.speed * 8
            if self.clock >= 100:
                self.animation_index += 1
                if self.animation_index >= len(self.images['down']):
                    self.animation_index = 0
                self.clock = 0

        elif direction == 'left':
            self.image = self.images['left'][self.animation_index]
            self.clock += self.speed * 8
            if self.clock >= 100:
                self.animation_index += 1
                if self.animation_index >= len(self.images['left']):
                    self.animation_index = 0
                self.clock = 0

        elif direction == 'right':
            self.image = self.images['right'][self.animation_index]
            self.clock += self.speed * 8
            if self.clock >= 100:
                self.animation_index += 1
                if self.animation_index >= len(self.images['right']):
                    self.animation_index = 0
                self.clock = 0

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprites_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image

    def get_images(self, y):
        images = []
        for i in range(0, 3):
            x = i*32
            image = self.get_image(x, y)
            images.append(image)

        return images
