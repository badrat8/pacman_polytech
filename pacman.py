import pyray
from raylib import colors
import settings



class Pacman:
    def __init__(self, x, y, radius, color=colors.YELLOW, outline=False, speed=2):
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.reset_x = x
        self.reset_y = y
        self.kesh_x = x
        self.kesh_y = y
        self.radius = radius
        self.color = color
        self.outline = outline
        self.speed = speed
        self.lifes = 3
        self.tick = 10
        self.angle_rot = 45
        self.newangle_rot = 45
        self.shift = [0, 0]
        self.newshift = [0, 0]
        self.initial = {
            "x": x,
            "y": y,
            "shift": [speed, speed],
        }

    def set_angle_rot(self, new):
        self.angle_rot = new

    def set_newangle_rot(self, new):
        self.newangle_rot = new


    def collides_with_horizontal_border(self):
        return self.y - self.radius <= 0 or self.y + self.radius >= settings.HEIGHT

    def collides_with_vertical_border(self):
        return self.x - self.radius <= 0 or self.x + self.radius >= settings.WIDTH

    def collides_with(self, other_ball):
        return pyray.check_collision(pyray.Vector2(self.rect.x + self.radius, self.rect.y + self.radius),
                                             pyray.Vector2(other_ball.rect.x + other_ball.x,
                                                           other_ball.rect.y + other_ball.radius)
                                             )

    def reset(self):
        self.lifes -= 1
        self.x = self.reset_x
        self.y = self.reset_y
        self.kesh_x = self.reset_x
        self.kesh_y = self.reset_y
        self.shift = [0, 0]

    def UP(self):
            self.set_newangle_rot(135 + 180)
            self.newshift[1] = -self.speed
            self.newshift[0] = 0

    def DOWN(self):
            self.set_newangle_rot(135)
            self.newshift[1] = self.speed
            self.newshift[0] = 0

    def LEFT(self):
            self.set_newangle_rot(225)
            self.newshift[0] = -self.speed
            self.newshift[1] = 0

    def RIGHT(self):
            self.set_newangle_rot(225 + 180)
            self.newshift[0] = self.speed
            self.newshift[1] = 0

    def Go(self):
        self.old_x = self.x
        self.old_y = self.y
        self.kesh_x = self.old_x
        self.kesh_y = self.old_y
    def Gokesh(self):
        self.x = self.kesh_x
        self.y = self.kesh_y
        self.shift[0]=self.newshift[0]
        self.shift[1]=self.newshift[1]
        self.set_angle_rot(self.newangle_rot)

    def Goback(self):
        self.x = self.old_x
        self.y = self.old_y
        self.kesh_x = self.old_x
        self.kesh_y = self.old_y

    def move(self):
        if self.collides_with_horizontal_border():
            self.shift[1] = 0
        if self.collides_with_vertical_border():
            self.shift[0] = 0

        if pyray.is_key_down(pyray.KeyboardKey.KEY_W): #UP
            self.UP()
        if pyray.is_key_down(pyray.KeyboardKey.KEY_S): #DOWN
            self.DOWN()
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A): #LEFT
            self.LEFT()
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D): #RIGHT
            self.RIGHT()

        self.x += self.shift[0]
        self.y += self.shift[1]
        self.kesh_x += self.newshift[0]
        self.kesh_y += self.newshift[1]


    def draw(self):
        pyray.draw_circle(self.old_x, self.old_y, self.radius, self.color)
        if self.tick >= 0:
            pyray.draw_circle_sector(pyray.Vector2(self.old_x, self.old_y), self.radius+1, self.angle_rot, self.angle_rot - 90, 0, colors.BLACK)
            self.tick -= 1
        elif self.tick >= -10:
            self.tick -= 1
        else:
            self.tick = 10
