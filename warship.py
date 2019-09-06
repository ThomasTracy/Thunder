import pygame


class Warship(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Warship, self).__init__()
        self.image = pygame.image.load("image/hero.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.top = self.screen.get_rect().bottom - 100
        self.goleft = False
        self.goright = False

    def show_ship(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.goleft:
            if 0 < self.rect.left:
                self.rect.centerx -= 10
        elif self.goright:
            if self.rect.right < self.screen.get_rect().right:
                self.rect.centerx += 10
        self.show_ship()

