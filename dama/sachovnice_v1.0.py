import pygame
from .promenne import *

class Sachovnice:
    def __init__(self):
        self.sachovnice = []
        self.vybrane_pole = None

    def vybrana_pole (self, policko):
        policko.fill(cerna)
        for radek in range(radky):
            for sloupec in range(radek % 2, radky, 2):
                pygame.draw.rect(policko, bila, (radek*velikost_pole, sloupec * velikost_pole, velikost_pole, velikost_pole))

