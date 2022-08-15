import pygame
from location import *
from config import *
from hero import *

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

def game_window(stage, hero):
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)
    screen.fill(MAIN_WINDOW)

    # Location Surface
    location_surf = pygame.Surface(LOCATION_SURFACE_SIZE)
    location_surf.fill(BACKGROUND)
    location_title = main_font.render(('Location: ' + get_stage_name()), 0, FONT_COLOR)
    location_surf.blit(location_title, (20, 20))
    x = 20
    y = 60

    if hero.x_y == []:
        hero.start_pos(stage)

    hero_icon = pygame.draw.rect(location_surf, HERO, (hero.x_y[0] * 70 + 40, hero.x_y[1] * 70 + 70, 20, 40))

    for i in range(stage.height):
        for j in range(stage.width):
            if stage.shape[i][j] == '| heal |':
                room_rect = pygame.draw.rect(location_surf, HEAL_ROOM, (x, y, 60, 60), 2)
            elif stage.shape[i][j] == '| enemy |':
                room_rect = pygame.draw.rect(location_surf, ENEMY_ROOM, (x, y, 60, 60), 2)
            elif stage.shape[i][j] == '| loot |':
                room_rect = pygame.draw.rect(location_surf, LOOT_ROOM, (x, y, 60, 60), 2)
            elif stage.shape[i][j] == '| enemy + loot |':
                room_rect = pygame.draw.rect(location_surf, ENEMY_AND_LOOT_ROOM, (x, y, 60, 60), 2)
            elif stage.shape[i][j] == '| wall |':
                room_rect = pygame.draw.rect(location_surf, WALL, (x, y, 60, 60), 2)
            elif stage.shape[i][j] == '| None |':
                room_rect = pygame.draw.rect(location_surf, INTERFACE_ELEMENTS, (x, y, 60, 60), 2)
            if [j, i] == hero.x_y:
                stage.shape[i][j] = '| None |'
                room_rect = pygame.draw.rect(location_surf, INTERFACE_ELEMENTS, (x, y, 60, 60), 2)

            if j != stage.width - 1:
                x += 70
            else:
                x = 20
                y += 70

    # Hero Statistics Surface
    stat_surf = pygame.Surface(STATS_SURFACE_SIZE)
    stat_surf.fill(BACKGROUND)
    stat_title = menu_font.render('Stats:', 0, FONT_COLOR)
    stat_surf.blit(stat_title, (160, 20))

    health = ('Health: ' + str(hero.health)).encode('utf-8')
    stat_health = main_font.render(health, 0, FONT_COLOR)
    stat_surf.blit(stat_health, (20, 70))

    level = ('Level: ' + str(hero.level)).encode('utf-8')
    stat_level = main_font.render(level, 0, FONT_COLOR)
    stat_surf.blit(stat_level, (20, 110))

    gold = ('Gold: ' + str(hero.gold)).encode('utf-8')
    stat_gold = main_font.render(gold, 0, FONT_COLOR)
    stat_surf.blit(stat_gold, (20, 150))

    streight = ('Streight: ' + str(hero.streight)).encode('utf-8')
    stat_streight = main_font.render(streight, 0, FONT_COLOR)
    stat_surf.blit(stat_streight, (20, 190))

    # Equipment Surface
    equip_surf = pygame.Surface(EQUIP_SURFACE_SIZE)
    equip_surf.fill(BACKGROUND)
    equip_title = menu_font.render('Equipment: ', 0, FONT_COLOR)
    equip_surf.blit(equip_title, (130, 20))

    head_rect = pygame.draw.rect(equip_surf, INTERFACE_ELEMENTS, (170, 60, 60, 60), 2)
    body_rect = pygame.draw.rect(equip_surf, INTERFACE_ELEMENTS, (170, 125, 60, 60), 2)
    left_hand_rect = pygame.draw.rect(equip_surf, INTERFACE_ELEMENTS, (105, 125, 60, 60), 2)
    right_hand_rect = pygame.draw.rect(equip_surf, INTERFACE_ELEMENTS, (235, 125, 60, 60), 2)
    legs_rect = pygame.draw.rect(equip_surf, INTERFACE_ELEMENTS, (170, 190, 60, 60), 2)

    # Gamelog Surface
    log_surf = pygame.Surface(LOG_SURFACE_SIZE)
    log_surf.fill(BACKGROUND)
    log_title = main_font.render('Game log: ', 0, FONT_COLOR)
    log_surf.blit(log_title, (20, 20))

    screen.blit(location_surf, LOCATION_SURFACE_POS)
    screen.blit(stat_surf, STATS_SURFACE_POS)
    screen.blit(equip_surf, EQUIP_SURFACE_POS)
    screen.blit(log_surf, LOG_SURFACE_POS)

    pygame.display.update()

clock = pygame.time.Clock()
is_started = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if stage1.loc_mirror[hero1.x_y[0] - 1][hero1.x_y[1]] != '| wall |':
                        hero1.move(stage1, hero1.x_y[0], hero1.x_y[1], hero1.x_y[0] - 1, hero1.x_y[1])
                        game_window(stage1, hero1)
                elif event.key == pygame.K_RIGHT:
                    if stage1.loc_mirror[hero1.x_y[0] + 1][hero1.x_y[1]] != '| wall |':
                        hero1.move(stage1, hero1.x_y[0], hero1.x_y[1], hero1.x_y[0] + 1, hero1.x_y[1])
                        game_window(stage1, hero1)
                elif event.key == pygame.K_UP:
                    if stage1.loc_mirror[hero1.x_y[0]][hero1.x_y[1] + 1] != '| wall |':
                        hero1.move(stage1, hero1.x_y[0], hero1.x_y[1], hero1.x_y[0], hero1.x_y[1] + 1)
                        game_window(stage1, hero1)
                elif event.key == pygame.K_DOWN:
                    if stage1.loc_mirror[hero1.x_y[0]][hero1.x_y[1] - 1] != '| wall |':
                        hero1.move(stage1, hero1.x_y[0], hero1.x_y[1], hero1.x_y[0], hero1.x_y[1] - 1)
                        game_window(stage1, hero1)

        if event.type == pygame.QUIT:
            running = False


    clock.tick(FPS)