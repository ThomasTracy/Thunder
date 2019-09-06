import pygame


class Button():
    def __init__(self, screen):
        self.image = pygame.image.load("image/game_start.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.center = self.screen.get_rect().center

    def show(self):
        self.screen.blit(self.image, self.rect)