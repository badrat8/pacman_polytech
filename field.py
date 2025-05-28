import pyray
from raylib import colors
import settings

def check_collision(x1, y1, width1, height1, x2, y2, width2, height2):
    a = [x1, y1]
    b = [x1 + width1, y1]
    c = [x1, y1 + height1]
    d = [x1 + width1, y1 + height1]
    def check(x, y):
        if (x >= x2) and (x <= x2 + width2) and (y >= y2) and (y <= y2 + height2):
            return True
        else:
            return False
    if check(a[0], a[1]) or check(b[0], b[1]) or check(c[0], c[1]) or check(d[0], d[1]):
        return True
    return False


class Field():
    def __init__(self):
        self.size = 22
        self.arr = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 9, 1, 1, 9, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 9, 1, 1, 9, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 1, 9, 9, 9, 9, 9, 9, 1, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [4, 3, 3, 3, 3, 3, 0, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 0, 3, 3, 3, 3, 3, 5],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1],
                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def show(self):
        for x in range(len(self.arr)):
            for y in range(len(self.arr[x])):
                if self.arr[x][y] == 1:
                    pyray.draw_rectangle(y * self.size, x * self.size, self.size, self.size, colors.DARKBLUE)
                    pyray.draw_rectangle_lines(y * self.size + 2, x * self.size + 2, self.size - 3, self.size - 3, colors.BLACK)
                    pyray.draw_rectangle_lines(y * self.size, x * self.size, self.size, self.size, colors.BLUE)
                elif self.arr[x][y] == 0:
                    pyray.draw_circle(y * self.size + self.size // 2, x * self.size + self.size // 2, 2, colors.WHITE)
                elif self.arr[x][y] == 2:
                    pyray.draw_circle(y * self.size + self.size // 2, x * self.size + self.size // 2, 6, colors.BEIGE)


    def check_coll(self, px, py, obj_type,obj):
        for x in range(len(self.arr)):
            for y in range(len(self.arr[x])):
                if self.arr[x][y] == 4 and obj_type == "pacman":
                    if check_collision(px - obj.radius, py - obj.radius, obj.radius*2, obj.radius*2, y * self.size, x * self.size, self.size, self.size):
                        settings.TELEPORT_0 = True
                if self.arr[x][y] == 5 and obj_type == "pacman":
                    if check_collision(px - obj.radius, py - obj.radius, obj.radius*2, obj.radius*2, y * self.size, x * self.size, self.size, self.size):
                        settings.TELEPORT_1 = True
                if self.arr[x][y] == 1 or (obj_type == "ghost" and (self.arr[x][y] == 4 or self.arr[x][y] == 5)):
                    if check_collision(px - obj.radius, py - obj.radius, obj.radius*2, obj.radius*2, y * self.size, x * self.size, self.size, self.size):
                        return True
                elif self.arr[x][y] == 0 and obj_type == "pacman":
                    if check_collision(px -  obj.radius, py -  obj.radius,  obj.radius*2, obj.radius*2, y * self.size, x * self.size, self.size, self.size):
                        self.arr[x][y] = -1
                elif self.arr[x][y] == 2 and obj_type == "pacman":
                    if check_collision(px - obj.radius, py - obj.radius, obj.radius*2, obj.radius*2, y * self.size, x * self.size, self.size, self.size):
                        self.arr[x][y] = -1
                        settings.ULTA_TIME = 60 * 5.5

        return False

    def count_coins(self):
        s = 0
        for y in range(len(self.arr)):
            s += self.arr[y].count(-1)
        return s
    def count_seed(self):
        s = 0
        for y in range(len(self.arr)):
            s += self.arr[y].count(0)
            s += self.arr[y].count(2)
        return s