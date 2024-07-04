import pyautogui
import numpy as np
import time
import random
import os

#testing cowhide image recognition
while 1:
    cowhide_xy = None
    cowhide_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\cowhide\cowhide2.png", confidence=0.8)
    #print(type(cowhide_xy))
    if cowhide_xy != None:
        pyautogui.click(cowhide_xy)
    time.sleep(3)