import pygame
import random as rd
import time
import redis

import Being


class Simulation:
    def __init__(self):
        # create graphic interface
        pygame.init()
        self.width = 1400
        self.height = 700
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Natural Selection")

        # generate World
        self.grid = self.generateLand(self.width, self.height)

        # generate population
        self.population = self.generatePop(r, 15)

    def run(self):
        print("Jet lag ?? AU GOULAG!")
        self.refresh()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or not self.population:
                    pygame.quit()
                    return
                for b in self.population:
                    b.survive(self.population)
                self.refresh()
                pygame.display.update()
                time.sleep(1)

    def generatePop(self, base,  nb):
        pop = []
        for i in range(nb):
            # dependant of world squares
            x = rd.randint(1, int(self.width / 100))
            y = rd.randint(1, int(self.height / 100))
            id = i * 42
            being = Being.Being(id, x * 100, y * 100)
            base.set(str(being.id), being.generateADN())
            pop.append(being)
        return pop

    def refresh(self):
        beingImg = pygame.image.load("../Graphic/Being.png")
        beingImg = pygame.transform.scale(beingImg, (100, 100))
        black = (0, 0, 0)
        self.display.fill(black)
        for i in range(int(self.width / 100)):
            for j in range(int(self.height / 100)):
                self.display.blit(self.grid[i][j].image, (i * 100, j * 100))

        for b in self.population:
            self.display.blit(beingImg, (b.x, b.y))

