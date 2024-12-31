import pygame
from constants import *

class Score:
    def __init__(self):
        self.score = 0
        self.smallfont = pygame.font.Font(None, 36)

    def scoring(self, gameDisplay):
        text = self.smallfont.render("score: " + str(self.score), True, (255, 0, 0))
        gameDisplay.blit(text, [SCREEN_WIDTH - 100,0])

    def Scored(self, points):
        self.score += points