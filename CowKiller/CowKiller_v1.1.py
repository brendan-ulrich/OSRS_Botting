#CowKiller_v1.1 [created 3/29/2024 7:12AM]
#Change from v1.0:
#   Script will search for "Attack Cow" image or text in a region of interest that is created around the mouse cursor instead of searching
#   the entire screen. The region of interest will be constantly updated as the mouse cursor moves.

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

#--- COW IMAGES ---# [these are the images of cows that the script will search for and try to click on]
#Create list of cow images paths
cow_directory = r'C:\Users\Owner\Desktop\Bot\CowKiller\images\cow'
cow_images = os.listdir(cow_directory)
#print(cow_images)
n_cow = len(cow_images)
cow_images_path = [None]*n_cow

#join image file names to the end of the directory path
index = 0
while index < len(cow_images):
    cow_images_path[index] = os.path.join(cow_directory,cow_images[index])
    index += 1 
#--- END COW IMAGES ---#
    
#--- CLICK COW IMAGES ---# [these are images of the option menu that pops up when a cow is clicked on]   
#Create list of image file paths and create directory variable
clickCow_directory = r'C:\Users\Owner\Desktop\Bot\CowKiller\images\clickCowImages'
clickCow_images = os.listdir(clickCow_directory)
#print(cow_images)
n_clickCow = len(clickCow_images) #number of images in directory folder
clickCow_images_path = [None]*n_clickCow #initialize list of image paths

#join image file names to directory path
index_clickCow = 0
while index_clickCow < len(clickCow_images):
    clickCow_images_path[index_clickCow] = os.path.join(clickCow_directory,clickCow_images[index_clickCow])
    index_clickCow += 1
#--- END CLICK COW IMAGES ---#

#reset index variables    
index = 0
index_clickCow = 0

#while cow_xy == None:
while 1: #main loop
    if index >= n_cow:
        index = 0
    cow_xy = None
    while cow_xy == None:
        if index >= n_cow:
            index = 0
        cow_xy = pyautogui.locateCenterOnScreen(cow_images_path[index], region=(0,40,920,500),confidence=0.55)
        index += 1
    #print(type(cow_xy))
    # pyautogui.moveTo(cow_xy)
    # time.sleep(0.1)
    pyautogui.mouseDown(cow_xy)
    time.sleep(0.5)
    pyautogui.mouseUp()

    #verify that cow has been clicked on
    clickCow_xy = None
    for i in range(5): 
    #while clickCow_xy == None:
        # Get the current position of the mouse cursor
        x, y = pyautogui.position()
        # Print the coordinates of the mouse cursor
        #print(f"Mouse Position: x={x}, y={y}", end='\r')

        # Draw bounding box around mouse cursor
        #   x +/- 200 pixels
        #   y +/- 200 pixels
        
        # Upper left coordinate
        x0 = x - 200
        y0 = y - 200
        # Account for negative values:
        if x0 < 0:
            x0 = 0
        if y0 < 0:
            y0 = 0

        # Lower right coordinate
        x1 = x + 200
        y1 = y + 200
        # Account for negative values:
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0

        # Create box
        cursor_box = [(x0, y0), (x1, y1)]
        #print(cursor_box, end='\r')
        width = x1 - x0
        height = y1 - y0

        #--- SEARCHES FOR BOTH COWS AND CALVES ---#
        if index_clickCow >= n_clickCow:
            index_clickCow = 0
        #while clickCow_xy == None: #original method (continuously searching)
        while index_clickCow < n_clickCow: #new method (searches once for cow, and once for calf and then moves the fuck on) 
            #if index_clickCow >= n_clickCow:
            #    index_clickCow = 0
            clickCow_xy = pyautogui.locateCenterOnScreen(clickCow_images_path[index_clickCow], region=(x0,y0,width,height),confidence=0.6)
            index_clickCow += 1
        #--- END SEARCHES FOR BOTH COWS AND CALVES ---#    

        #UNCOMMENT LINE BELOW FOR ORIGINAL METHOD           
        #clickCow_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\clickCow.png", region=(x0,y0,width,height),confidence=0.6)
        #print('click cow', type(clickCow_xy))

        #Attack cow if we have confirmed it is indeed a cow we clicked on
        if clickCow_xy != None:  
            # Search for image within bounding box 
            attackCow_xy = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\attackCow2.png", region=(x0,y0,width,height),confidence=0.7)
            #print('attack cow', type(attackCow_xy))
            pyautogui.mouseDown(attackCow_xy) #press and hold on attackCow icon    
            pyautogui.mouseUp() #pause and then release mouse to click on cow
            time.sleep(3)
            break
    #end for loop to verify we have clicked on the cow
    
    #Confirm we have successfully attacked the cow
    confirmAttackCow = None
    confirmAttackCow = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\confirmAttackCow.png", region=(102,75,64,20),confidence=0.8)
    print('confirmAttackCow type is: ', type(confirmAttackCow))
    if confirmAttackCow != None:
        waitToKillCow = None
        while waitToKillCow == None:
            waitToKillCow = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\cowHealthRed.png", region=(40,70,185,300),confidence=0.9)
            print('cow is alive', end='\r')        
        print('cow is dead')
    #END Confirm we have successfully attacked the cow
    
    #Confirm we have successfully attacked the cow calf
    confirmAttackCowCalf = None
    confirmAttackCowCalf = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\confirmAttackCowCalf.png", region=(102,75,64,20),confidence=0.8)
    print('confirmAttackCowCalf type is: ', type(confirmAttackCowCalf))
    if confirmAttackCowCalf != None:
        waitToKillCowCalf = None
        while waitToKillCowCalf == None:
            waitToKillCowCalf = pyautogui.locateCenterOnScreen(r"C:\Users\Owner\Desktop\Bot\CowKiller\images\cowCalfHealthRed.png", region=(40,70,185,300),confidence=0.9)
            print('cow calf is alive', end='\r')        
        print('cow calf is dead')       
    #END Confirm we have successfully attacked the cow calf
#end main while loop
            
            
    

