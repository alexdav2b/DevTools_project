import random

from src import Parcel


class Being:
    def __init__(self, idB, x, y):
        self.id = idB
        self.x = x
        self.y = y
        self.health = 20
        self.satiety = 20
        # generate Genom
        self.generateADN()

    def eat(self):
        self.satiety = self.satiety - 10

    def survive(self, population):
        self.satiety -= 10
        if self.satiety <= 0:
            self.health -= 10
        if self.health <= 0:
            population.pop(population.index(self))

    def move(self):
        # need world and squares
        position_x = 0
        position_y = 0
        if self.health >= 3 and self.satiety >= 10:
            for i in range(self.x):
                position_x = random.randint(0, self.x)
                for j in range(self.y):
                    position_y = random.randint(0, self.y)

    def eating(self):
        if self.satiety != 0 and self.health >= 5:
            if Parcel.food == 1:
                self.health += 1
                self.satiety += 1
            elif Parcel.food == 5:
                self.health += 1
                self.satiety += 1
            elif Parcel.food == 10:
                print("Jackpot")
                self.health += 10
                self.satiety += 10

    def generateADN(self, parent1='', parent2=''):
        if not parent1 and not parent2:
            return 'ACGT'
        else:
            res = ''
            for ind, n in enumerate(parent1):
                res = res + parent1[ind] if random.randint(1, 2) == 1 else parent1[ind]