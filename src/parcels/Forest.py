import random
import pygame

from src.Parcel import Parcel


class Forest (Parcel):
    def __init__(self):
        Parcel.__init__(self, 2)
        self.name = "Foret"
        self.temp = random.randint(20, 30) # Température varie entre 20 et 40 degrés
        self.humidity = random.randint(70, 80) # Humidité allant de 10 à 20%
        self.wold_type = 'flat'
        self.food = 10
        self.image = pygame.image.load("../Graphic/forest.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
