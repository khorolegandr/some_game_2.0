from config import *

map = []

class Stage():
    def loc_generation(self):
        self.shape = [[0 for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.shape[i][j] = self.room_generation()
        '''
        self.loc_mirror = [['wall' for j in range(self.width + 2)] for i in range(self.height + 2)]
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                self.loc_mirror[i + 2][j + 2] = self.shape[i][j]
        self.shape = self.loc_mirror.copy()
        '''

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