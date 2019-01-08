from enum import Enum
import math

class ActionType(Enum):
    MOVE = 1
    SHOOT = 2

class Direction(Enum):
    RIGHT = 1
    LEFT = 3
    UP = 2
    DOWN = 3
    NONE = 5

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

class Action:
    def __init__(self, actionType, direction):
        self._type = actionType
        self._direction = direction
