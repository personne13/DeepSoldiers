import pygame
import random
from utils import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.direction = direction
        print(direction.x)
        self.rect = self.image.get_rect()
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.speed = 10

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.bottom > HEIGHT:
            self.kill()
        if self.rect.top < 0:
            self.kill()
