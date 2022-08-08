from config import *


class Hero():
    def __init__(self, level=1, health=100, gold=20, streight=10):
        self.health = health
        self.gold = gold
        self.streight = streight

    def move(self, old_pos, new_pos):
        pass

    def take_loot(self, loot):
        pass