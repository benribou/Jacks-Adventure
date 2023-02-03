import pygame
import time

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        for i in range (1, 5):
            self.sprites_sheet = pygame.image.load(f"./chest/chest-{i}.png")
            self.image = self.get_image(0 , 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprites_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveCanceled(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        