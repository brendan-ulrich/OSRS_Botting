import pyautogui
import numpy as np
import time
import random


splashes = 0 #initialize splashes variabe

while True:
    splashes = splashes + 1
    splash_randomizer = random.randint(0,60) #antiban randomization feature
    if (splashes + splash_randomizer) > 200:
        pyautogui.click(881,266)
        splashes = 0

    level_up_indicator = pyautogui.locateCenterOnScreen('alch_images/tap_here_to_continue.png', confidence=0.9) #if image is not found this will return None
    #print(type(magic_tab_open))
    if level_up_indicator != None: #if player has leveled up
        pyautogui.click(level_up_indicator) #click continue
        pyautogui.moveRel(500,0) #move mouse out of the way so image is not blocked
        level_up_indicator = None #reset value
        time.sleep(1)
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('space')
    