import pyautogui
import numpy as np
import time
import random

#BEFORE STARTING CODE:
#Face north, camera raised to highest viewpoint
#Zoom all the way in
#Must be standing on east side of GE next to the northernmost banker
#Begin with ore in bank (not in inventory)
#Begin with magic tab open (for now)

#FOR BRONZE BAR:
#Tin ore in bank slot (1,1)
#Copper ore in bank slot (2,1)
#Nature runes in inventory slot (1,1)
#Staff of fire equipped

#Define inventory slots:
inv_11 = [695,274] #first row
inv_21 = [737,274] #|
inv_31 = [779,274] #|
inv_41 = [821,274] #|
inv_12 = [695,311] #second row
inv_22 = [737,311] #|
inv_32 = [779,311] #|
inv_42 = [821,311] #|
inv_13 = [695,348] #third row
inv_23 = [737,348] #|
inv_33 = [779,348] #|
inv_43 = [821,348] #|
inv_14 = [695,385] #fourth row
inv_24 = [737,385] #|
inv_34 = [779,385] #|
inv_44 = [821,385] #|
inv_15 = [695,422] #fifth row
inv_25 = [737,422] #|
inv_35 = [779,422] #|
inv_45 = [821,422] #|
inv_16 = [695,459] #sixth row
inv_26 = [737,459] #|
inv_36 = [779,459] #|
inv_46 = [821,459] #|
inv_17 = [695,496] #seventh row
inv_27 = [737,496] #|
inv_37 = [779,496] #|
inv_47 = [821,496] #|

#open bank account
pyautogui.moveTo(580,288) #move mouse to banker
pyautogui.mouseDown() #hold down mouse on banker
time.sleep(1)
pyautogui.mouseUp() #release mouse once menu pops up
pyautogui.moveRel(0,60) #move mouse to bank option
pyautogui.click() #select bank option
time.sleep(0.8) #wait for bank screen to open. maybe change this to image search

while True:
    #withdraw tin ore
    pyautogui.moveTo(210,295) #move mouse to bank slot (1,1)
    pyautogui.mouseDown() #hold down mouse on bank slot
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once withdraw menu pops up
    pyautogui.moveRel(0,95) #select withdraw 13 option (this has been pre-set using "withdraw x" option)
    pyautogui.click() #click withdraw 13
    time.sleep(0.5)

    #withdraw copper ore
    pyautogui.moveTo(259,295) #move mouse to bank slot (2,1)
    pyautogui.mouseDown() #hold down mouse on bank slot
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once withdraw menu pops up
    pyautogui.moveRel(0,95) #select withdraw 13 option (this has been pre-set using "withdraw x" option)
    pyautogui.click() #click withdraw 13
    time.sleep(0.5)

    #exit bank
    pyautogui.click(615,215)
    time.sleep(1)

    #smelt ores
    pyautogui.click(180,339)#select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_21) #select ore in inv(2,1) 
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_31) #select ore in inv(3,1)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_41) #select ore in inv(4,1)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_12) #select ore in inv(1,2)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_22) #select ore in inv(2,2)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_32) #select ore in inv(3,2)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_42) #select ore in inv(4,2)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_13) #select ore in inv(1,3)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_23) #select ore in inv(2,3)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_33) #select ore in inv(3,3)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_43) #select ore in inv(4,3)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_14) #select ore in inv(1,4)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_24) #select ore in inv(2,4)
    time.sleep(1.2)
    #all ores have been smelted

    #open bank account
    pyautogui.moveTo(580,288) #move mouse to banker
    pyautogui.mouseDown() #hold down mouse on banker
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once menu pops up
    pyautogui.moveRel(0,60) #move mouse to bank option
    pyautogui.click() #select bank option
    time.sleep(0.8) #wait for bank screen to open. maybe change this to image search

    #deposit bronze bars
    pyautogui.moveTo(inv_21) #move mouse to bronze bar
    pyautogui.mouseDown() #hold down mouse on bronze bar
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once menu pops up
    pyautogui.moveRel(0,158) #move to deposit all option
    pyautogui.click() #click deposit all
    time.sleep(0.5)





