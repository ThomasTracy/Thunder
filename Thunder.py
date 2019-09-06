import pygame
import game_functions as gf
import warship
import button
import status
import score
import sound


def game_on():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([1080, 640])
    pygame.display.set_caption("Thunder Game")

    ship = warship.Warship(screen)
    but = button.Button(screen)
    stat = status.Status()
    sco = score.Score(screen, stat)
    sounds = sound.Sounds()

    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    gf.init_aliens(screen, aliens)
    booms = []

    pygame.mixer.music.load("sound/background.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    while True:

        gf.check_events(ship, but, stat)
        gf.check_hit_alien(screen, bullets, aliens, booms, sco)
        gf.check_hit_warship(ship, aliens, bullets, stat)
        gf.show_all(screen, ship, bullets, aliens, booms, but, stat, sco)

game_on()