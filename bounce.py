import pygame

class Bounce:

    def __init__(self, mainsurface):
        self.mainsurface = mainsurface
        self.image = pygame.Surface((50,50))
        self.image.fill((255, 182, 193))
        self.rect = self.image.get_rect()
        self.x_speed = 3
        self.y_speed = 5

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.left < 0 or self.rect.right > self.mainsurface.get_width():
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.mainsurface.get_height():
            self.y_speed = -self.y_speed