#!/usr/bin/env python3

import pyautogui
import threading
from random import randint

__author__ = "Michael(Yu) Lin"
__version__ = "0.1.0"
__licence__ = "MIT"

def move_timer(threads_arr):
    while(True):
        random_X = randint(-60, 60)
        random_Y =  randint(-60, 60)
        random_Sec = randint(1, 60)
        
        print("Mouse will move {} pixels horizontally and {} pixels vertically after {} seconds".format(random_X, random_Y, random_Sec)) 
        
        thread = threading.Timer(random_Sec, move_mouse, [random_X, random_Y])
        thread.daemon = True
        thread.start()
        thread.join()

def move_mouse(x, y):
    pyautogui.move(x, y)

def main():
    try:
        print("Starting script...")

        threads_arr = []
        move_timer(threads_arr)
    except(KeyboardInterrupt, SystemExit):
        print("Killing Script")

if __name__ == "__main__":
    main()
