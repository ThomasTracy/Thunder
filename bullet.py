import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, warship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.warship = warship
        self.speed = [0, -15]
        self.image = pygame.image.load("image/bullet2.png")
        # self.image = pygame.surface.Surface([3, 15]).convert()
        self.rect = self.image.get_rect()
        self.rect.top = self.warship.rect.top + 25

    def move(self):
        self.rect = self.rect.move(self.speed)
        self.show_bullet()

    def show_bullet(self):
        self.screen.blit(self.image, self.rect)

