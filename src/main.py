import pygame
from bullet import *
from player import *
from utils import *
import numpy as np

import gym
import gym_soldiers

def getActionKeyboard(input):#input is an array containing all possible inputs
    direction = Vector2(0, 0)
    keystate = pygame.key.get_pressed()
    typeAction = 3

    if input[Input.GOLEFT]:
        typeAction = 1;
        direction.x += -1
    if input[Input.GORIGHT]:
        typeAction = 1;
        direction.x += 1
    if input[Input.GODOWN]:
        typeAction = 1;
        direction.y += 1
    if input[Input.GOUP]:
        typeAction = 1;
        direction.y += -1

    if input[Input.SHOOTUP]:
        typeAction = 2;
        direction = Vector2(0, -1).normalize()
    if input[Input.SHOOTLEFT]:
        typeAction = 2;
        direction = Vector2(-1, 0).normalize()
    if input[Input.SHOOTDOWN]:
        typeAction = 2;
        direction = Vector2(0, 1).normalize()
    if input[Input.SHOOTRIGHT]:
        typeAction = 2;
        direction = Vector2(1, 0).normalize()

    direction.normalize()

    action = Action(typeAction, direction)
    return action

def getInputAI(action):
    input = np.zeros(Input.nbInputs, bool)
    input[action] = True
    return input


def getInputKeyboard():
    input1 = np.zeros(Input.nbInputs, bool)
    input2 = np.zeros(Input.nbInputs, bool)

    keystate = pygame.key.get_pressed()
    input1[Input.GOLEFT] = keystate[pygame.K_LEFT]
    input1[Input.GORIGHT] = keystate[pygame.K_RIGHT]
    input1[Input.GODOWN] = keystate[pygame.K_DOWN]
    input1[Input.GOUP] = keystate[pygame.K_UP]
    input1[Input.SHOOTUP] = keystate[pygame.K_KP8]
    input1[Input.SHOOTLEFT] = keystate[pygame.K_KP4]
    input1[Input.SHOOTDOWN] = keystate[pygame.K_KP5]
    input1[Input.SHOOTRIGHT] = keystate[pygame.K_KP6]

    input2[Input.GOLEFT] = keystate[pygame.K_q]
    input2[Input.GORIGHT] = keystate[pygame.K_d]
    input2[Input.GODOWN] = keystate[pygame.K_z]
    input2[Input.GOUP] = keystate[pygame.K_s]
    input2[Input.SHOOTUP] = keystate[pygame.K_y]
    input2[Input.SHOOTLEFT] = keystate[pygame.K_g]
    input2[Input.SHOOTDOWN] = keystate[pygame.K_h]
    input2[Input.SHOOTRIGHT] = keystate[pygame.K_j]

    return input1, input2

def main():
    env = gym.make('soldiers-v0')
    clock = pygame.time.Clock()
    print(env.action_space)

    running = True

    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)
        act_n = []
        input1, input2 = getInputKeyboard()
        act_n.append(getActionKeyboard(input1))
        input_ai = getInputAI(env.action_space.sample())
        act_n.append(getActionKeyboard(input_ai))
        # print(act_n[0]._type)
        act_n.append(Action(3, None))

        obs_n, reward_n, done_n, _ = env.step(act_n)

        env.render()

main()
