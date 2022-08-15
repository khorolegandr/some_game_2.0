from config import *

map = []

class Stage():
    def loc_generation(self):
        self.shape = [[0 for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.shape[i][j] = self.room_generation()
        self.loc_mirror = [['| wall |' for j in range(self.width + 2)] for i in range(self.height + 2)]
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.loc_mirror[i][j] = self.shape[i - 1][j - 1]

    def __init__(self, name):
        self.width = STAGE_WIDTH
        self.height = STAGE_HEIGHT
        self.name = name
        map.append(self.name)
        self.loc_generation()

    def room_generation(self):
        if random.choice(WALL_OR_NOT) == 0:
            if random.choice(ENEMY_OR_NOT) == 0:
                if random.choice(LOOT_OR_NOT) == 0:
                    if random.choice(HEAL_OR_NOT) == 0:
                        return '| None |'
                    else:
                        return '| heal |'
                else:
                    return '| loot |'
            else:
                if random.choice(LOOT_OR_NOT) == 0:
                    return '| enemy |'
                else:
                    return '| enemy + loot |'
        else:
            return '| wall |'



def get_stage_name():
    return map[-1]