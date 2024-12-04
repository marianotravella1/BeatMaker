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

label_font = pygame.font.Font('./Fonts/Poppins/Poppins-Bold.ttf', 32)
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Beat Maker")

fps = 60
timer = pygame.time.Clock()

def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0,0,250, HEIGHT-200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT-200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, black, white]

    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (18, 30))

    clap_text = label_font.render('clap', True, white)
    screen.blit(clap_text, (18, 120))

    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (18, 210))

    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (18,300))

    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (18, 390))

    op_hi_hat_text = label_font.render('Open Hi-Hat', True, white)
    screen.blit(op_hi_hat_text, (18, 480))

    for i in range


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
