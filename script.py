#!/usr/bin/env python3

import pyautogui
import threading
from pynput.keyboard import Listener
from random import randint

__author__ = "Michael(Yu) Lin"
__version__ = "0.1.0"
__licence__ = "MIT"

def move_mouse():
    random_X = randint(-60, 60)
    random_Y =  randint(-60, 60)
    random_Sec = randint(1, 60)

    pyautogui.move(random_X, random_Y)
    print("Mouse will move {} pixels horizontally and {} pixels vertically after {} seconds".format(random_X, random_Y, random_Sec)) 
    threading.Timer(random_Sec, move_mouse).start()

def kill_script(key):
    #Kills script on 'ESC' button press
    if key == keyboard.Key.esc:
        print("Killing Script")
        exit()

def main():
    print("Starting script...")

    with Listener(on_press=kill_script) as listener:
        listener.join()
    
    move_mouse()

if __name__ == "__main__":
    main()
