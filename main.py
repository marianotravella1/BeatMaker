from string import whitespace

import pygame
from pygame import mixer
#initialize pygame
pygame.init()


WIDTH = 1400
HEIGHT = 750

black = (0,0,0)
white = (255,255,255)
gray = (128, 128, 128)

label_font = pygame.font.Font('./Fonts/Roboto/Roboto-Bold.ttf', 32)
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Beat Maker")

fps = 60
timer = pygame.time.Clock()

def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0,0,250, HEIGHT-195], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT-200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, black, white]

    height = 30
    add_height = 92

    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (18, height))

    height = height+add_height
    clap_text = label_font.render('clap', True, white)
    screen.blit(clap_text, (18, height))

    height = height+add_height
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (18, height))

    height = height+add_height
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (18,height))

    height = height+add_height
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (18, height))

    height = height+add_height
    op_hi_hat_text = label_font.render('Open Hi-Hat', True, white)
    screen.blit(op_hi_hat_text, (18, height))

    for i in range(6):
        pygame.draw.line(screen, gray, (5, (i * add_height) + add_height), (245, (i * add_height) + add_height), 5)



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
