#!/usr/bin/python
# -*- coding:utf8 -*-
import pygame
import sys
import bullet
import  alien
import boom
import random


def check_events(warship, button, stat):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                warship.goright = True
                warship.image = pygame.image.load("image/hero1.png")
            elif event.key == pygame.K_LEFT:
                warship.goleft = True
                warship.image = pygame.image.load("image/hero1.png")
        elif event.type == pygame.KEYUP:
            warship.goleft = False
            warship.goright = False
            warship.image = pygame.image.load("image/hero.png")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y= pygame.mouse.get_pos()
            check_click_start(button, x, y, stat)


def check_click_start(button, x, y, stat):
    if button.rect.collidepoint(x, y):
        stat.start = True


def fire(group, warship):
    bullet_left = bullet.Bullet(warship.screen, warship)
    bullet_left.rect.centerx = warship.rect.centerx - 28
    bullet_right = bullet.Bullet(warship.screen, warship)
    bullet_right.rect.centerx = warship.rect.centerx + 24
    group.add(bullet_left, bullet_right)
    # pygame.mixer.music.load("sound/fire.mp3")
    # pygame.mixer.music.set_volume(0.5)
    # pygame.mixer.music.play()


def init_aliens(screen, aliens):
    locations = []
    for i in range(10):
        col = random.randint(0, 12)
        row = random.randint(0, 18)
        pos = [col, row]
        if pos not in locations:
            locations.append(pos)
            new_alien = alien.Alien(screen, [0, 5])
            new_alien.rect.top, new_alien.rect.left = [-pos[0] * 50 - 50, pos[1] * 60 + 10]
            aliens.add(new_alien)


    # if not len(aliens):
    #     for i in range(row):
    #         for j in range(col):
    #             new_alien = alien.Alien(screen, [5, 0])
    #             new_alien.rect.left, new_alien.rect.top = [100 + i * 120, 100 + j * 120]
    #             aliens.add(new_alien)
    #     bullets.empty()


def check_hit_alien(screen, bullets, aliens, booms, score):
    collides = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for alien in collides.values():
        hit_enemy = pygame.mixer.Sound("sound/hit_enemy.wav")
        hit_enemy.set_volume(0.3)
        hit_enemy.play()
        new_boom = boom.Boom(screen, alien)
        booms.append(new_boom)
        for the_alien in alien:
            score.score += 100


def check_hit_warship(warship, aliens, bullets, stat):
    if pygame.sprite.spritecollide(warship, aliens, True):
        hit_self = pygame.mixer.Sound("sound/hit_self.wav")
        hit_self.set_volume(0.3)
        hit_self.play()
        pygame.time.delay(1000)
        warship.kill()
        aliens.empty()
        bullets.empty()
        stat.lives -= 1
        if stat.lives == 0:
            stat.start = False


def background_move(screen, stat):
    screen.blit(stat.background, [0, stat.background_loc])
    if stat.background_loc >= 0:
        stat.background_loc = -1280
    else:
        stat.background_loc += 2


def show_lives(screen, stat):
    lives = stat.lives
    image = pygame.image.load("image/life.png")
    for i in range(lives):
        screen.blit(image, [i * 60 + 10, 10])


def show_all(screen, warship, bullets, aliens, booms, button, stat, score):
    # pygame.time.delay(10)

    # 背景滚动
    background_move(screen, stat)
    if not stat.start and stat.lives != 0:
        button.show()
    elif not stat.start and stat.lives == 0:
        greeting = pygame.font.Font(None, 80)
        greeting_image = greeting.render("YOUR SCORE IS : " + str(score.score), \
                                         True, [0, 0, 0])
        greeting_pos = [button.rect.left - 100, button.rect.top - 100]
        screen.blit(greeting_image, greeting_pos)
        button.show()
        stat.stat_reset()
    else:
        button.image = pygame.image.load("image/game_Reagain.png")

        # 飞船移动
        warship.move()

        # 监控屏幕是否滚动到底了
        if stat.screen_loc >= 640:
            init_aliens(screen, aliens)
            stat.screen_loc = 0
        else:
            stat.screen_loc += 5

        # 控制子弹射出频率
        if stat.shoot % 4 == 0:
            fire(bullets, warship)
            stat.shoot += 1
        else:
            stat.shoot += 1

        # 子弹出屏幕后删除
        for bullet in bullets.sprites():
            bullet.move()
            if bullet.rect.top <= 0:
                bullets.remove(bullet)

        # 敌方飞船向下移动
        aliens.update()

        # 显示分数
        score.show()

        # 显示生命
        show_lives(screen, stat)

        # 爆炸
        for the_boom in booms:
            the_boom.show()

    pygame.display.flip()