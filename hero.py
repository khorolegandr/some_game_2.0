from location import *
from config import *


class Hero():
    def __init__(self, level=1, health=100, gold=20, streight=10):
        self.level = level
        self.health = health
        self.gold = gold
        self.streight = streight
        self.x_y = []

    def set_equipment(self):
        self.equipment = {'head': [],
                          'body': [],
                          'left_hand': [],
                          'right_hand': [],
                          'legs': []}

    def start_pos(self, stage):
        counter = 0
        for i in range(len(stage.shape)):
            for j in range(len(stage.shape[i])):
                if counter == START_ROOM_NUM:
                    stage.loc_mirror[i + 1][j + 1] = '| Hero |'
                    self.x_y.append(j)
                    self.x_y.append(i)
                counter += 1

    def heal_room(self):
        pass

    def enemy_room(self):
        pass

    def loot_room(self):
        pass

    def enemy_loot_room(self):
        pass

    def move(self, stage, old_x, old_y, new_x, new_y):
        stage.shape[old_y][old_x] = '| None |'
        self.x_y = []
        self.x_y.append(new_x)
        self.x_y.append(new_y)
        if stage.shape[new_y][new_x] == '| heal |':
            self.heal_room()
        elif stage.shape[new_y][new_x] == '| enemy |':
            self.enemy_room()
        elif stage.shape[new_y][new_x] == '| loot |':
            self.loot_room()
        elif stage.shape[new_y][new_x] == '| enemy + loot |':
            self.enemy_loot_room()