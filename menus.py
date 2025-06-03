import pyray
from raylib import colors
import game
import game_data
import settings

width = settings.WIDTH
height = settings.HEIGHT
pyray.init_window(width,height,"PAC-MAN")
def main_menu():
    file=open('Leaders.txt','r')
    lead=file.readlines()
    #pyray.init_audio_device()
    #music = pyray.load_music_stream("Sound.mp3")
    #pyray.play_music_stream(music)
    l1=0
    l2=0
    l3=0
    for i in range(len(lead)):
        lead[i]=int(lead[i])
    for i in range(len(lead)):
        if lead[i]>l1:
            l1=lead[i]
        elif lead[i]>l2:
            l2=lead[i]
        elif lead[i]>l3:
            l3=lead[i]

    settings.LEADERS.append(l1)
    settings.LEADERS.append(l2)
    settings.LEADERS.append(l3)

    while not pyray.window_should_close():
        pyray.begin_drawing()
        #pyray.update_music_stream(music)
        pyray.clear_background(colors.BLACK)
        pyray.draw_text("PAC-MAN",int(width/6),int(height/8),int(width/7), colors.YELLOW)
        pyray.draw_text("Leaders :",int(width/2+170),int(height/2-120),80, colors.WHITE)
        pyray.draw_line(int(width/2+50),int(height/2-30),int(width-50),int(height/2-30),colors.YELLOW)
        pyray.draw_text("1st", int(width / 2 + 150), int(height / 2), 80, colors.YELLOW)
        pyray.draw_text("2nd", int(width / 2 + 150), int(height / 2 + 120), 80, colors.YELLOW)
        pyray.draw_text("3rd", int(width / 2 + 150), int(height / 2 + 240), 80, colors.YELLOW)
        pyray.draw_text(str(l1), int(width / 2 + 350), int(height / 2), 80, colors.YELLOW)
        pyray.draw_text(str(l2), int(width / 2 + 350), int(height / 2 + 120), 80, colors.YELLOW)
        pyray.draw_text(str(l3), int(width / 2 + 350), int(height / 2 + 240), 80, colors.YELLOW)
        pyray.draw_rectangle_lines_ex(pyray.Rectangle(0, 0, width, height), height / 27, colors.BLUE)
        pyray.draw_text("Start game", int(width/4-190), int(height/2+50), 80, colors.BLACK)
        pyray.draw_text("Quit game", int(width / 4 - 170), int(height / 2 + 250), 80, colors.BLACK)
        pyray.end_drawing()
        file.close()
        if pyray.gui_button(pyray.Rectangle(40, height/2, width/2, height/5), ''):
            pyray.close_window()
            result = game.start_game()
            print("")
            settings.LEADERS.append(str(result[0]))
            game_data.write_in_file()
            return result
        if pyray.gui_button(pyray.Rectangle(40, height/4*3, width/2, height/5), ''):
            pyray.close_window()
            exit(0)
    exit(0)

def game_over():
    #pyray.init_audio_device()
    #music = pyray.load_music_stream("Sound.mp3")
    #pyray.play_music_stream(music)
    while not pyray.window_should_close():
        #pyray.update_music_stream(music)
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        pyray.draw_text("GAME OVER", int(width/5),int(height/8),int(width/10),colors.RED)
        pyray.draw_text("Main menu", int(width / 2 - 180), int(height / 2 + 50), 80, colors.BLACK)
        pyray.draw_text("Quit game", int(width / 2 - 180), int(height / 2 + 250), 80, colors.BLACK)
        pyray.draw_rectangle_lines_ex(pyray.Rectangle(0, 0, width, height), height / 27, colors.RED)
        pyray.end_drawing()
        if pyray.gui_button(pyray.Rectangle(width/4, height/2, width/2, height/5), ''):
            main_menu()
        if pyray.gui_button(pyray.Rectangle(width/4, height/4*3, width/2, height/5), ''):
            pyray.close_window()
            exit(0)
def victory():
    #pyray.init_audio_device()
    #music = pyray.load_music_stream("Sound.mp3")
    #pyray.play_music_stream(music)
    while not pyray.window_should_close():
        #pyray.update_music_stream(music)
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        pyray.draw_text("  VICTORY ", int(width/ 5),int(height/8),int(width/10),colors.GREEN)
        pyray.draw_text("Main menu", int(width / 2 - 180), int(height / 2 + 50), 80, colors.BLACK)
        pyray.draw_text("Quit game", int(width / 2 - 180), int(height / 2 + 250), 80, colors.BLACK)
        pyray.draw_rectangle_lines_ex(pyray.Rectangle(0, 0, width, height), height / 27, colors.GREEN)
        pyray.end_drawing()
        if pyray.gui_button(pyray.Rectangle(width/4, height/2, width/2, height/5), ''):
            main_menu()
        if pyray.gui_button(pyray.Rectangle(width/4, height/4*3, width/2, height/5), ''):
            pyray.close_window()
            exit(0)