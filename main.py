import pygame
from location import *
from config import *
from hero import *
from windows import *

pygame.init()

clock = pygame.time.Clock()
is_started = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not is_started:
            start_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_started = True
        else:
            if 'Stage 1' not in map:
                stage1 = Stage('Stage 1')
            hero1 = Hero()
            game_window(stage1, hero1)

    clock.tick(FPS)