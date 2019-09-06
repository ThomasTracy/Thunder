import pygame


class Boom():
    def __init__(self, screen, alien):
        self.screen = screen
        self.images = []
        for i in range(21):
            image = "image/boom%s.png" % str(i + 1)
            self.images.append(pygame.image.load(image))
        self.rect = self.images[0].get_rect()
        self.rect.top = alien[0].rect.top
        self.rect.left = alien[0].rect.left

    def show(self):
        if len(self.images):
            self.screen.blit(self.images.pop(0), self.rect)