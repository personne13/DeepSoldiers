# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
import pygame
import random
from utils import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.speed = 3
        self.direction = Vector2(0, 0)#either 0 either normalized.
        self.actionType = ActionType.NONE
        self.lastShoot = 0
        self.score = 0
        self.shootDirection = Vector2(0, 0)
        self.tag = ObjectName.PLAYER
        self.score = 0
        self.name = name

    def changeDirection(self, direction):
        self.direction = direction

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def reset(self):
        self.rect.centerx = 0
        self.rect.centery = 0


    def shoot(self):
        if(self.lastShoot > 100):
            self.lastShoot = 0
            return True;

        return False;

    def update(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)
        self.direction = Vector2(0, 0)
        self.lastShoot += 1

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
