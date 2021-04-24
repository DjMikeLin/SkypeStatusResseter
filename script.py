#!/usr/bin/env python3

import sys
import pyautogui
import threading
import time
from random import randint

__author__ = "Michael(Yu) Lin"
__version__ = "0.1.0"
__licence__ = "MIT"

def move_mouse(threads_arr):
    random_X = randint(-60, 60)
    random_Y =  randint(-60, 60)
    random_Sec = randint(1, 60)

    pyautogui.move(random_X, random_Y)
    print("Mouse will move {} pixels horizontally and {} pixels vertically after {} seconds".format(random_X, random_Y, random_Sec)) 
    thread = threading.Timer(random_Sec, move_mouse(threads_arr))
    threads_arr.append(thread)
    #thread.daemon = True
    thread.start()

def main():
    try:
        print("Starting script...")

        threads_arr = []
        move_mouse(threads_arr)
    except (KeyboardInterrupt, SystemExit):
        for thr in threads_arr:
            thr.join()

        "Killing Script"

if __name__ == "__main__":
    main()
