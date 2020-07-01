import pyboy
import imageio
import random
import argparse
from pyboy.utils import WindowEvent


pyboy = pyboy.PyBoy('../gbprojects/tests/GenerationTest/build/rom_gen_test/rom/game.gb')
screen = pyboy.botsupport_manager().screen()

screen_capture_list = []

buttons_press = [
            WindowEvent.PRESS_ARROW_UP, WindowEvent.PRESS_ARROW_DOWN, WindowEvent.PRESS_ARROW_LEFT,
            WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.PRESS_BUTTON_A, WindowEvent.PRESS_BUTTON_B,
            WindowEvent.PRESS_BUTTON_SELECT, WindowEvent.PRESS_BUTTON_START
]
buttons_release = [
            WindowEvent.RELEASE_ARROW_UP, WindowEvent.RELEASE_ARROW_DOWN, WindowEvent.RELEASE_ARROW_LEFT,
            WindowEvent.RELEASE_ARROW_RIGHT, WindowEvent.RELEASE_BUTTON_A, WindowEvent.RELEASE_BUTTON_B,
            WindowEvent.RELEASE_BUTTON_SELECT, WindowEvent.RELEASE_BUTTON_START
]
events = buttons_press + buttons_release

"UDLRABsS"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--buttons', '-b', type=str, help="button input file name")
    parser.add_argument('--game', '-e', type=str, help="rom file name", default='../gbprojects/tests/GenerationTest/build/rom_gen_test/rom/game.gb' )
    parser.add_argument('--video', '-v', type=str, help="output video file name", default="output.mp4")
    args = parser.parse_args()
    button_input_file = open(args.buttons, 'r')


    filename = ""
    for line in button_input_file:
        pyboy.tick()
        print(line)
        for ch_index, ch in enumerate(line.strip()):
            if ch == '-':
                pyboy.send_input(buttons_release[ch_index])
            else:
                pyboy.send_input(buttons_press[ch_index])
                print(buttons_press[ch_index])
        screen_capture_list.append(screen.screen_ndarray())
    imageio.mimwrite(args.video, screen_capture_list, fps=60)
