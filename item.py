import  pygame

class ItemSoin():
    def __int__(self, attribut, soin, sprite):
        self.attribut = attribut
        self.soin = soin
        self.sprites_sheet = sprite

    def getter_soin(self):
        return self.soin


# pomme = ItemSoin("pomme", 25, pygame.image.load('pomme.png'))
# tomate = ItemSoin("tomate", 50, pygame.image.load('tomate.png') )
# banane = ItemSoin("banane", 75, pygame.image.load('banane.png'))
