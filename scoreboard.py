import pygame
from constants import *

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
    
    def Scored(self, points):
        self.value += points

    def display(self, screen):
        text = self.font.render(f"Score: {self.value}", True, (200, 0, 0))
        screen.blit(text, (10, 10))