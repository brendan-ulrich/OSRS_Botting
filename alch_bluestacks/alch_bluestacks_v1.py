import pyautogui
import numpy as np
import time
import random

#prompt for number of alchs
num_alchs = int(input("enter number of alchs desired:"))

#define inventory slots and tabs (maybe make this into its own library that i can import)
low_alch_icon = [235,291] #low alch icon (located in magic tab)
inv_11 = [695,274] #(1,1) inventory slot
magic_tab = [30,345] #magic tab coords

#perform alching METHOD 2
alchs = 0 #number of succesful alchs (begins at 0)
while alchs < num_alchs:
    magic_tab_open = None #initilize variable
    magic_tab_open = pyautogui.locateCenterOnScreen('alch_images\magic_tab_open.png', confidence=0.95) #if image is not found this will return None
    #print(type(magic_tab_open))
    if magic_tab_open != None: #if magic tab is open
        pyautogui.click(low_alch_icon) #click low alch icon
        sleep_time = (random.randint(0,100))/1000 #generate a random time between 0 and 0.1 seconds
        time.sleep(sleep_time) #sleep for randomly generated sleep_time (anti-ban feature)
        inv_tab_open = None #initilize variable
        inv_tab_open = pyautogui.locateCenterOnScreen('alch_images\inventory_tab_open.png') #if image is not found this will return None
        if inv_tab_open != None: #if inventory tab is open
            pyautogui.click(inv_11) #click item in (1,1) inventory slot
            alchs = alchs + 1 #add 1 to number of successful alchs
            sleep_time = (random.randint(6,8))/10 #generate a random time between 0.5 and 0.8 seconds
            time.sleep(sleep_time) #sleep for randomly generated sleep_time to allow alch to be performed
    else: #if magic tab is closed
        pyautogui.click(magic_tab) #click magic tab to open it
        sleep_time = (random.randint(0,100))/1000 #generate a random time between 0 and 0.1 seconds
        time.sleep(sleep_time) #sleep for randomly generated sleep_time (anti-ban feature)

# #perform alching METHOD 1
# alchs = 0 #number of succesful alchs
# while alchs < num_alchs:
#     pyautogui.click(low_alch_icon) #click on low alch icon
#     sleep_time = (random.randint(5,8))/10 #generate a random time between 0.5 and 0.8 seconds
#     time.sleep(sleep_time) #sleep for randomly generated sleep_time
#     pyautogui.click(inv_11) #click on (1,1) inventory slot (item to be alched)
#     sleep_time = (random.randint(10,12))/10 #generate a random time between 1 and 1.2 seconds
#     time.sleep(sleep_time) #sleep for randomly generated sleep_time
#     alchs = alchs + 1




