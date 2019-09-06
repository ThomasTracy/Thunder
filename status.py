import pygame


class Status():
    def __init__(self):
        self.background = pygame.image.load("image/background.png")
        self.start = False
        self.screen_loc = 0
        self.background_loc = -1280
        self.shoot = 0
        self.lives = 3
    def stat_reset(self):
        self.start = False
        self.screen_loc = 0
        self.background_loc = -1280
        self.shoot = 0
        self.lives = 3