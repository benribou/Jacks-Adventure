import pygame

class Monstre(pygame.sprite.Sprite):
    def __init__(self, x, y, health=100, degats=7, max_health=100):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 1
        self.health = health
        self.max_health = max_health
        self.degats = degats
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    #Chercher les coordonnées du joueur et le suivre

    def targetPlayer(self, player):
        if player.rect.x > self.rect.x:
            self.rect.x += self.speed
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        if player.rect.y > self.rect.y:
            self.rect.y += self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveCanceled(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def __del__(self):
        # Code pour détruire les objets de la classe Monstre
        pass