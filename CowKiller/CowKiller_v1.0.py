#CowKiller_v1.0 [created 3/24/2024 8:56AM]
#Use this script to kill cows (melee). Script will be designed for Lumbridge cow pen with the intention of expanding for other areas
#v2.0 will include banking
#For use with bluestacks OSRS client only. Snap client to top left corner of screen.

import pyautogui
import numpy as np
import time
import random
import os

#testing cowhide image recognition
# while 1:
#     cowhide_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\cowhide\cowhide2.png", confidence=0.8)
#     print(type(cowhide_xy))
#     pyautogui.moveTo(cowhide_xy)
#     time.sleep(1)

cow_directory = r'C:\Users\Owner\Desktop\Bot\CowKiller\images\cow'
cow_images = os.listdir(cow_directory)
#print(cow_images)
n = len(cow_images)
cow_images_path = [None]*n

index = 0
while index < len(cow_images):
    cow_images_path[index] = os.path.join(cow_directory,cow_images[index])
    index += 1 


index = 0
#while cow_xy == None:
while 1:
    if index >= n:
        index = 0
    cow_xy = None
    while cow_xy == None:
        if index >= n:
            index = 0
        cow_xy = pyautogui.locateCenterOnScreen(cow_images_path[index], region=(0,40,920,500),confidence=0.55)
        index += 1
    print(type(cow_xy))
    # pyautogui.moveTo(cow_xy)
    # time.sleep(0.1)
    pyautogui.mouseDown(cow_xy)
    time.sleep(0.2)
    clickCow_xy = None
    clickCow_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\clickCow.png", region=(0,40,920,500),confidence=0.6)
    print('click cow', type(clickCow_xy))
    if clickCow_xy != None:
        attackCow_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\attackCow.png", region=(0,40,920,500),confidence=0.7)
        print('attack cow', type(attackCow_xy))
        pyautogui.moveTo(attackCow_xy)
    pyautogui.mouseUp()
    time.sleep(0.25)
    

