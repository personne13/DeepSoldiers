import pygame
import random
from utils import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.direction = direction
        self.rect = self.image.get_rect()
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.speed = 10
        self.shooter = player
        self.tag = ObjectName.BULLET

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

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
