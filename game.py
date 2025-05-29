import time

import pyray
from raylib import colors
import random
import pacman as pc
import field
import ghost
import settings
import settings as set
import game_data

def start_game():
    f = field.Field()
    pyray.init_window(set.WIDTH, set.HEIGHT, "PAC-MAN")

    #pyray.init_audio_device()
    #music = pyray.load_music_stream("Sound.mp3")
    #pyray.play_music_stream(music)

    pyray.init_audio_device()
    death = pyray.load_sound("pacman_death.wav")
    inter = pyray.load_sound("pacman_intermission.wav")
    beggin = pyray.load_sound("pacman_beginning.wav")
    eat = pyray.load_sound("pacman_chomp.wav")

    pyray.set_sound_volume(death, 1)
    pyray.play_sound(beggin)


    pyray.set_target_fps(60)# FPS

    start_ghost_cords = {"x1": 13.5, "x2": 14.5, "x3": 15.5, "x4": 16.5, "y1": 15.5, "y2": 15.5, "y3": 15.5, "y4": 15.5,}
    start_pacman_cords = {"x": 15, "y": 18.5}

    pacman = pc.Pacman(int(start_pacman_cords["x"]*f.size), int(start_pacman_cords["y"]*f.size), f.size//2-1.5)
    a = [ghost.Ghost(int(start_ghost_cords["x1"]*f.size), int(start_ghost_cords["y1"]*f.size), colors.RED),
         ghost.Ghost(int(start_ghost_cords["x2"]*f.size), int(start_ghost_cords["y2"]*f.size), colors.SKYBLUE),
         ghost.Ghost(int(start_ghost_cords["x3"]*f.size), int(start_ghost_cords["y3"]*f.size), colors.MAGENTA),
         ghost.Ghost(int(start_ghost_cords["x4"]*f.size), int(start_ghost_cords["y4"]*f.size), colors.ORANGE),
         ]

    ghosts_coins = 0
    coins = 0

    beggining = True

    while True:
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        f.show()
        pacman.draw()
        pacman.move()
        f.check_coll(pacman.old_x, pacman.old_y, "pacman", pacman)
        if settings.TELEPORT_0:
            pacman.x = int(28.5*f.size)
            pacman.y = int(15.5*f.size)
            pacman.kesh_x = int(28.5*f.size)
            pacman.kesh_y = int(15.5*f.size)
            settings.TELEPORT_0 = False
        elif settings.TELEPORT_1:
            pacman.x = int(1.5*f.size)
            pacman.y = int(15.5*f.size)
            pacman.kesh_x = int(1.5*f.size)
            pacman.kesh_y = int(15.5*f.size)
            settings.TELEPORT_1 = False
        if f.check_coll(pacman.kesh_x, pacman.kesh_y, "pacman",pacman) == False:
            pacman.Gokesh()
            pacman.Go()
        elif f.check_coll(pacman.x, pacman.y, "pacman",pacman) == False:
            pacman.Go()
        else:
            pacman.Goback()

        for _ghost in a: #GHOSTS
            _ghost.move()
            _ghost.show()
            if f.check_coll(_ghost.x, _ghost.y, "ghost", _ghost):
                _ghost.x = _ghost.old_x
                _ghost.y = _ghost.old_y
                _ghost.way = _ghost.ways[random.randint(0, len(_ghost.ways)-1)]

            if field.check_collision(pacman.x, pacman.y, pacman.radius * 2, pacman.radius * 2, _ghost.x, _ghost.y, _ghost.radius * 2, _ghost.radius * 2):
                if settings.ULTA_TIME > 0:
                    if _ghost.lifes > 1:
                        _ghost.reset()
                    else:
                        a.remove(_ghost)
                        ghosts_coins += 100
                else:
                    if pacman.lifes > 1:
                        pacman.reset()
                        for i in a:
                            i.reset()
                        pyray.play_sound(death)
                    else:
                        return [coins + ghosts_coins, -1]

        new_coins = f.count_coins()
        if new_coins - coins > 0:
            pyray.play_sound(eat)
        coins = new_coins

        c = f.count_seed()
        pyray.draw_text("Your score = " + str(coins + ghosts_coins) + "\nLifes = " + str(pacman.lifes), 740, 60, 60, colors.YELLOW)

        if c == 0:
            return [coins + ghosts_coins, 1]

        if settings.ULTA_TIME == 60 * 5.5:
            pyray.play_sound(inter)

        if settings.ULTA_TIME > 0:
            settings.ULTA_TIME -= 1
        pyray.end_drawing()
        if beggining:
            time.sleep(4)
            beggining = False
    pyray.close_window()