import pygame


pygame.mixer.init()
class Sounds():
    def __init__(self):
        self.background = pygame.mixer.music.load("sound/background.mp3")
        self.fire = pygame.mixer.music.load("sound/fire.mp3")
        self.hit_enemy = pygame.mixer.music.load("sound/hit_enemy.mp3")
        self.hit_self = pygame.mixer.music.load("sound/hit_self.mp3")