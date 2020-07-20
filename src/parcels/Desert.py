import random
import pygame

from src.Parcel import Parcel


class Desert (Parcel):
    def __init__(self):
        Parcel.__init__(self, 1)
        self.name = "Désert"
        self.temp = random.randint(20, 40) # Température varie entre 20 et 40 degrés
        self.humidity = random.randint(10, 20) # Humidité allant de 10 à 20%
        self.wold_type = 'flat'
        self.food = 1
        self.image = pygame.image.load("../Graphic/desert.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
