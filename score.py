import pygame


class Score():
    def __init__(self, screen, stat):
        self.stat = stat
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)
        self.color = [0, 0, 0]

    def rend(self):
        scr = "{:,}".format(int(self.score))
        self.image = self.font.render(scr, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.right = [self.screen.get_rect().top + 10, \
                                          self.screen.get_rect().right - 10]

    def show(self):
        self.rend()
        self.screen.blit(self.image, self.rect)
