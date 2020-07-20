import random
import pygame

from src.Parcel import Parcel


class Meandow (Parcel):
    def __init__(self):
        Parcel.__init__(self, 3)
        self.name = "Prairie"
        self.temp = random.randint(10, 20)  # Température varie entre 20 et 40 degrés
        self.humidity = random.randint(0, 5)  # Humidité allant de 10 à 20%
        self.wold_type = 'flat'
        self.food = 5
        self.image = pygame.image.load("../Graphic/meandow.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
