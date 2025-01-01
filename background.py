import pygame

class Background:
    def __init__(self, image_path, speed):
        self.image = pygame.image.load("stockPhotoOfOuterSPace.jpg").convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = speed
        self.x = 0 
    
    def update(self, dt):
        self.x -= self.speed * dt
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x , 0))
        screen.blit(self.image, (self.x + self.width, 0))

