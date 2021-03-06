from enum import Enum
import math

WIDTH = 600
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class ActionType:
    MOVE = 1
    SHOOT = 2
    NONE = 3

class Input:
    GOUP = 0
    GODOWN = 1
    GOLEFT = 2
    GORIGHT = 3
    SHOOTUP = 4
    SHOOTDOWN = 5
    SHOOTLEFT = 6
    SHOOTRIGHT = 7
    nbInputs = 8

class ObjectName(Enum):
    PLAYER = 1
    BULLET = 2

class Vector2:
    def __init__(self, x, y):
        self.x = float(x);
        self.y = float(y);

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        norm = self.norm()
        if(norm != 0):
            self.x = self.x / norm
            self.y = self.y / norm

        return self

class Action:
    def __init__(self, actionType, direction = None):
        self._type = actionType
        self._direction = direction
