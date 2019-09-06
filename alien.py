import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen, speed):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image/enemy1.png")
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # if self.rect.right >= 1080 or self.rect.left <= 0:
        #     self.speed[0] = -1 * self.speed[0]
        #     self.rect.top += 100
        if self.rect.top > 640:
            self.kill()
        self.rect = self.rect.move(self.speed)
        self.show()

    def show(self):
        self.screen.blit(self.image, self.rect)

