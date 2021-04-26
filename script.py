#!/usr/bin/env python3

import pyautogui
import threading
from random import randint
screenWidth, screenHeight = pyautogui.size() #Pixel width and height of primary monitor
pyautogui.FAILSAFE = False #Turns failsafe to move mouse offscreen off

__author__ = "Michael(Yu) Lin"
__version__ = "0.1.0"
__licence__ = "MIT"

def move_timer():
    while(True):
        random_X = randint(-200, 200)
        random_Y =  randint(-200, 200)
        random_Sec = randint(1, 60)
        
        print("Mouse will move {} pixels horizontally and {} pixels vertically after {} seconds".format(random_X, random_Y, random_Sec)) 
        #Thread timer 
        thread = threading.Timer(random_Sec, move_mouse, [random_X, random_Y])
        thread.daemon = True
        thread.start()
        thread.join()

def move_mouse(x, y):
    currentMouseX, currentMouseY = pyautogui.position()
    
    #Moves mouse; Goes in opposite direction if near screen borders
    pyautogui.move(x * -1 if x + currentMouseX > screenWidth or x + currentMouseX < screenWidth else x, 
        y * -1 if y + currentMouseY > screenHeight or y + currentMouseY < screenHeight else y)
    
    #Hits F12 key
    pyautogui.hotkey('F12')

def main():
    try:
        print("Starting script...")

        move_timer()
    except(KeyboardInterrupt, SystemExit):
        print("Killing Script")

if __name__ == "__main__":
    main()
