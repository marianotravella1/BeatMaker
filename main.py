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
green = (0,255,0)
gold = (212, 175, 55)

label_font = pygame.font.Font('./Fonts/Roboto/Roboto-Bold.ttf', 32)
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Beat Maker")

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

def draw_grid(clicks):
    left_box = pygame.draw.rect(screen, gray, [0,0,250, HEIGHT-195], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT-200, WIDTH, 200], 5)
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

    for i in range(instruments):
        pygame.draw.line(screen, gray, (5, (i * add_height) + add_height), (245, (i * add_height) + add_height), 5)

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color, [i * ((WIDTH-250)//beats) + 255, (j*add_height) + 5, ((WIDTH - 200) // beats) - 10, ((HEIGHT-200)//instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold, [i * ((WIDTH-250)//beats) + 250, (j*add_height), ((WIDTH - 200)//beats), ((HEIGHT-200)//instruments)], 5, 5)

            pygame.draw.rect(screen, black, [i * ((WIDTH-250)//beats) + 250, (j*add_height), ((WIDTH - 200)//beats), ((HEIGHT-200)//instruments)], 2, 5)

            boxes.append((rect, (i,j)))
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
    pygame.display.flip()
pygame.quit()
