from string import whitespace

import pygame
from pygame import mixer

# initialize pygame
pygame.init()

WIDTH = 1400
HEIGHT = 750

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

label_font = pygame.font.Font('./Fonts/Roboto/Roboto-Bold.ttf', 32)
medium_font = pygame.font.Font('./Fonts/Roboto/Roboto-Bold.ttf', 24)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")

fps = 60
timer = pygame.time.Clock()
beats = 16
instruments = 6
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 400
playing = True
active_length = 0
active_beat = 1
beat_changed = True
boxes = []

# load in sounds
hi_hat = mixer.Sound("./Sounds/Basic808HiHat.wav")
snare = mixer.Sound("./Sounds/Basic808Snare.wav")
kick = mixer.Sound("./Sounds/Basic808Kick.wav")
clap = mixer.Sound("./Sounds/Basic808Clap.wav")
open_hi_hat = mixer.Sound("./Sounds/808OH_2.wav")
crash = mixer.Sound("./Sounds/808Crash_2.wav")
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                kick.play()
            if i == 1:
                clap.play()
            if i == 2:
                snare.play()
            if i == 3:
                hi_hat.play()
            if i == 4:
                crash.play()
            if i == 5:
                open_hi_hat.play()


# load in sounds
hi_hat = mixer.Sound("./Sounds/Basic808HiHat.wav")
snare = mixer.Sound("./Sounds/Basic808Snare.wav")
kick = mixer.Sound("./Sounds/Basic808Kick.wav")
clap = mixer.Sound("./Sounds/Basic808Clap.wav")
open_hi_hat = mixer.Sound("./Sounds/Basic808HiHat.wav")


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                kick.play()
            if i == 1:
                clap.play()
            if i == 2:
                snare.play()
            if i == 3:
                hi_hat.play()
            if i == 4:
                open_hi_hat.play()


def draw_grid(clicks, beat):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 250, HEIGHT - 195], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    colors = [gray, black, white]
    boxes = []

    height = 30
    add_height = 92

    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (18, height))

    height = height + add_height
    clap_text = label_font.render('clap', True, white)
    screen.blit(clap_text, (18, height))

    height = height + add_height
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (18, height))

    height = height + add_height
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (18, height))

    height = height + add_height
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (18, height))

    height = height + add_height
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
            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 250) // beats) + 255, (j * add_height) + 5,
                                                    ((WIDTH - 200) // beats) - 10,
                                                    ((HEIGHT - 200) // instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold,
                             [i * ((WIDTH - 250) // beats) + 250, (j * add_height), ((WIDTH - 200) // beats),
                              ((HEIGHT - 200) // instruments)], 5, 5)

            pygame.draw.rect(screen, black,
                             [i * ((WIDTH - 250) // beats) + 250, (j * add_height), ((WIDTH - 200) // beats),
                              ((HEIGHT - 200) // instruments)], 2, 5)

            boxes.append((rect, (i, j)))

    active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 250) // beats) + 250, 0, ((WIDTH - 200) // beats),
                                             instruments * add_height], 5, 3)
    return boxes


run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)
    # lower menu buttons
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, HEIGHT - 130))
    if playing:
        play_text2 = medium_font.render('Playing', True, dark_gray)
    else:
        play_text2 = medium_font.render('Paused', True, dark_gray)
    screen.blit(play_text2, (70, HEIGHT - 100))

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True

    beat_length = 3600 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()
