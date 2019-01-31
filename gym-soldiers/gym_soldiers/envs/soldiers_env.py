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

  def getObservation(self):
      sprites = self.all_sprites.sprites()
      bullets = np.zeros(4, int)
      for i in range(2):
        for j in range(len(sprites)):
            obj = sprites[j]
            if (obj.tag == ObjectName.BULLET):
                if (obj.shooter == self.player1 and i == 0):
                  bullets[0] = obj.rect.centerx
                  bullets[1] = obj.rect.centery
                elif(obj.shooter == self.player2 and i == 1):
                  bullets[2] = obj.rect.centerx
                  bullets[3] = obj.rect.centery

      observations = [self.player1.rect.centerx, self.player1.rect.centery, self.player2.rect.centerx, self.player2.rect.centery]
      observations.append(bullets)

      return observations

  def handleCollisions(self, player):
      sprites = self.all_sprites.sprites()
      length = len(sprites)
      toRemove = []
      hasBeenTouched = False
      for j in range(length):
          bullet = sprites[j]
          if (bullet.tag == ObjectName.BULLET): #check if it's a bullet
              if (bullet.shooter != player):
                  if bullet.is_collided_with(player):
                      player.reset()
                      player.score += 1
                      hasBeenTouched = True
                      print(player.name)
                      print(player.score)
                      toRemove.append(bullet)


      for b in toRemove:
          b.kill()

      return hasBeenTouched

  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    self.action_space = spaces.Discrete(Input.nbInputs)
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

    reward = 0

    if(self.handleCollisions(self.player1)):
      reward += 1

    if(self.handleCollisions(self.player2)):
      reward -= 1

    observation = self.getObservation()

    return observation, reward, False, None

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
