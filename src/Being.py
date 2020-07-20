import random

class Being:
    def __init__(self, idB, x, y):
        self.id = idB
        self.x = x
        self.y = y
        self.health = 20
        self.satiety = 20
        # generate Genom
        self.generateADN()

    def generateADN(self, parent1='', parent2=''):
        if not parent1 and not parent2:
            return 'ACGT'
        else:
            res = ''
            for ind, n in enumerate(parent1):
                res = res + parent1[ind] if random.randint(1, 2) == 1 else parent1[ind]