import random

import pygame.font

pygame.init()

FPS = 30

# Surfaces
SCREEN_SIZE = (1200, 800)
SCREEN_TITLE = 'Some Title'
START_MENU_SURFACE_SIZE = (600, 600)
START_MENU_SURFACE_POS = (300, 100)
LOCATION_SURFACE_SIZE = (600, 580)
LOCATION_SURFACE_POS = (20, 20)
STATS_SURFACE_SIZE = (400, 580)
STATS_SURFACE_POS = (780, 20)
LOG_SURFACE_SIZE = (1160, 160)
LOG_SURFACE_POS = (20, 620)

# Colors
MAIN_WINDOW = (30, 30, 30)
BACKGROUND = (0, 0, 0)
FONT_COLOR = (255, 255, 255)
WALL = (183, 183, 183)
ENEMY_ROOM = (255, 0, 0)
LOOT_ROOM = (255, 255, 0)
HEAL_ROOM = (0, 255, 0)

# Fonts
main_font = pygame.font.SysFont('ubuntumono', 20)
menu_font = pygame.font.SysFont('ubuntumono', 28)

# Stage
STAGE_WIDTH = random.randint(5, 7)
STAGE_HEIGHT = random.randint(4, 7)

WALL_OR_NOT = [0, 0, 0, 0, 1]
ENEMY_OR_NOT = [0, 0, 1, 1, 1]
LOOT_OR_NOT = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
HEAL_OR_NOT = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
