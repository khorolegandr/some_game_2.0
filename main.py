import pygame
from location import *
from config import *

pygame.init()

def start_menu():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)
    screen.fill(MAIN_WINDOW)

    start_menu_surf = pygame.Surface(START_MENU_SURFACE_SIZE)
    start_menu_surf.fill(BACKGROUND)
    start_menu_title = menu_font.render('MENU', 0, FONT_COLOR)
    start_menu_surf.blit(start_menu_title, (270, 50))

    get_started_letter = main_font.render('Press [SPACE] to start', 0, FONT_COLOR)
    start_menu_surf.blit(get_started_letter, (185, 260))

    screen.blit(start_menu_surf, (300, 100))

    pygame.display.update()

def game_window():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)
    screen.fill(MAIN_WINDOW)

    location_surf = pygame.Surface(LOCATION_SURFACE_SIZE)
    location_surf.fill(BACKGROUND)
    location_title = main_font.render(('Location: ' + get_stage_name()), 0, FONT_COLOR)
    location_surf.blit(location_title, (20, 20))
    x = 20
    y = 40
    for i in range(stage1.height):
        for j in range(stage1.width):
            room = main_font.render(stage1.shape[i][j], 0, FONT_COLOR)
            location_surf.blit(room, (x, y))
            if j != stage1.width - 1:
                x += 70
            else:
                x = 20
                y += 30

    stat_surf = pygame.Surface(STATS_SURFACE_SIZE)
    stat_surf.fill(BACKGROUND)
    stat_title = main_font.render('Stats:', 0, FONT_COLOR)
    stat_surf.blit(stat_title, (20, 20))

    log_surf = pygame.Surface(LOG_SURFACE_SIZE)
    log_surf.fill(BACKGROUND)
    log_title = main_font.render('Game log: ', 0, FONT_COLOR)
    log_surf.blit(log_title, (20, 20))

    screen.blit(location_surf, LOCATION_SURFACE_POS)
    screen.blit(stat_surf, STATS_SURFACE_POS)
    screen.blit(log_surf, LOG_SURFACE_POS)

    pygame.display.update()

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
            game_window()

    clock.tick(FPS)