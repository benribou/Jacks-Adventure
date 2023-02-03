import pygame

class Skills():
    
    def __init__(self, player, nomSkill, ):
        self.player = player
        self.skill = {
            'attack': 0,
            'defense': 0,
            'speed': 0,
            'health': 0,
            'mana': 0
        }