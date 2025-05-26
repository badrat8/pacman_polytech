import datetime
import random
import pyray
from raylib import colors

import settings


class Ghost():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.reset_x = x
        self.reset_y = y
        self.color = color
        self.radius = 9
        self.speed = 6
        self.lifes = 3
        self.ways = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.way = self.ways[random.randint(0, len(self.ways)-1)]

    def reset(self):
        self.lifes -= 1
        self.x = self.reset_x
        self.y = self.reset_y


    def move(self):
        self.old_x = self.x
        self.old_y = self.y
        self.x += self.way[0]
        self.y += self.way[1]
        if random.randint(0, 100) == 0:
            self.way = self.ways[random.randint(0, len(self.ways)-1)]

    def show(self):
        if settings.ULTA_TIME == 0:
            pyray.draw_circle(self.x, self.y, self.radius, self.color)
            pyray.draw_rectangle(self.x - self.radius, self.y, self.radius * 2, self.radius, self.color)
            pyray.draw_circle(self.x - 5, self.y - 2, 3, colors.WHITE)
            pyray.draw_circle(self.x + 5, self.y - 2, 3, colors.WHITE)
            pyray.draw_circle(self.x - 5 + (self.way[0] * 2), self.y - 2 + (self.way[1] * 2), 2, colors.DARKBLUE)
            pyray.draw_circle(self.x + 5 + (self.way[0] * 2), self.y - 2 + (self.way[1] * 2), 2, colors.DARKBLUE)
        else:
            pyray.draw_circle(self.x, self.y, self.radius, colors.DARKBLUE)
            pyray.draw_rectangle(self.x - self.radius, self.y, self.radius * 2, self.radius, colors.DARKBLUE)
            pyray.draw_circle(self.x - 5, self.y - 2, 2, colors.WHITE)
            pyray.draw_circle(self.x + 5, self.y - 2, 2, colors.WHITE)