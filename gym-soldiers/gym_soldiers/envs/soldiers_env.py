import pygame
from bullet import *
from player import *
from utils import *
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class SoldiersEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def handleActions(self, player):
      if(player.actionType == ActionType.SHOOT):
          if(player.shoot()):
              newBullet = Bullet(Vector2(player.rect.centerx, player.rect.centery), player.shootDirection, player)
              self.all_sprites.add(newBullet)

          player.actionType = ActionType.NONE

  def handleCollisions(self, player):
      #for i in range(len(all_sprites.sprites())):
      #    (all_sprites.sprites()[i].direction)
      sprites = self.all_sprites.sprites()
      length = len(sprites)
      toRemove = []
      for j in range(length):
          bullet = sprites[j]
          if (bullet.tag == ObjectName.BULLET): #check if it's a bullet
              if (bullet.shooter != player):
                  if bullet.is_collided_with(player):
                      player.reset()
                      player.score += 1
                      print(player.name)
                      print(player.score)
                      toRemove.append(bullet)


      for b in toRemove:
          b.kill()

  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DeepSoldiers!")
    self.all_sprites = pygame.sprite.Group()
    self.player1 = Player(Vector2(10, 10), "Franck")
    self.player2 = Player(Vector2(100, 100), "Thomas")

    self.all_sprites.add(self.player1)
    self.all_sprites.add(self.player2)

    return
  def step(self, action_n):#action_n stores actions of both players
    if(action_n[0]._type == 1):
      self.player1.actionType = action_n[0]._type
      self.player1.changeDirection(action_n[0]._direction)

    elif(action_n[0]._type == 2):
      self.player1.actionType = action_n[0]._type
      self.player1.shootDirection = action_n[0]._direction

    if(action_n[1]._type == 1):
      self.player2.actionType = action_n[1]._type
      self.player2.changeDirection(action_n[1]._direction)

    elif(action_n[1]._type == 2):
      self.player2.actionType = action_n[1]._type
      self.player2.shootDirection = action_n[1]._direction

    self.handleActions(self.player1)
    self.handleActions(self.player2)

    self.handleCollisions(self.player1)
    self.handleCollisions(self.player2)

    return None, None, None, None

  def reset(self):
    return

  def render(self, mode='human', close=False):
    self.all_sprites.update()

    # Draw / render
    self.screen.fill(BLACK)
    self.all_sprites.draw(self.screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()
    return
