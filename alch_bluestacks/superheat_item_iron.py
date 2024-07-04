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

#FOR IRON BAR:
#Iron ore in bank slot (3,1)
#Ring of Forging in bank slot (4,1)
#Begin wearing ring of forging
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

#prompt for number of desired smelts
total_smelts = int(input("enter number smelts desired:"))
smelt_count = 0 #successful smelts

#open bank account
pyautogui.moveTo(580,288) #move mouse to banker
pyautogui.mouseDown() #hold down mouse on banker
time.sleep(1)
pyautogui.mouseUp() #release mouse once menu pops up
pyautogui.moveRel(0,60) #move mouse to bank option
pyautogui.click() #select bank option
time.sleep(0.8) #wait for bank screen to open. maybe change this to image search

while (smelt_count <= total_smelts):
    #NOT NEEDED BUT MIGHT BE USEFUL IN THE FUTURE
    # #check ring of forging status
    # if smelt_count >= 140:
    #     #withdraw ring of forging
    #     pyautogui.click(357,295) #click bank slot (4,1)
    #     time.sleep(0.5)
    #     #exit bank
    #     pyautogui.click(615,215)
    #     time.sleep(1)
    #     #open inventory tab
    #     pyautogui.click(883,261) #inventory tab coords
    #     time.sleep(0.5)
    #     #equip ring of forging
    #     pyautogui.click(inv_21)
    #     time.sleep(0.5)
    #     #open magic tab
    #     pyautogui.click(30,345) #magic tab coords
    #     time.sleep(0.5)
    #     #open bank account
    #     pyautogui.moveTo(580,288) #move mouse to banker
    #     pyautogui.mouseDown() #hold down mouse on banker
    #     time.sleep(1)
    #     pyautogui.mouseUp() #release mouse once menu pops up
    #     pyautogui.moveRel(0,60) #move mouse to bank option
    #     pyautogui.click() #select bank option
    #     time.sleep(0.8) #wait for bank screen to open. maybe change this to image search
        
    #     #reset smelt counter
    #     smelt_count = 0
    #     #end ring forging status

    #withdraw iron ore
    pyautogui.moveTo(308,292) #move mouse to bank slot (1,1)
    pyautogui.mouseDown() #hold down mouse on bank slot
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once withdraw menu pops up
    pyautogui.moveRel(0,152) #select withdraw  all option
    pyautogui.click() #click withdraw all
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

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_34) #select ore in inv(3,4)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_44) #select ore in inv(4,4)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_15) #select ore in inv(1,5)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_25) #select ore in inv(2,5)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_35) #select ore in inv(3,5)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_45) #select ore in inv(4,5)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_16) #select ore in inv(1,6)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_26) #select ore in inv(2,6)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_36) #select ore in inv(3,6)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_46) #select ore in inv(4,6)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_17) #select ore in inv(1,7)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_27) #select ore in inv(2,7)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_37) #select ore in inv(3,7)
    time.sleep(1.2)

    pyautogui.click(180,339) #select superheat item
    time.sleep(0.7)
    pyautogui.click(inv_47) #select ore in inv(4,7)
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

    #deposit iron bars
    pyautogui.moveTo(inv_21) #move mouse to bronze bar
    pyautogui.mouseDown() #hold down mouse on bronze bar
    time.sleep(1)
    pyautogui.mouseUp() #release mouse once menu pops up
    pyautogui.moveRel(0,158) #move to deposit all option
    pyautogui.click() #click deposit all
    time.sleep(0.5)

    #update smelt counter
    smelt_count = smelt_count + 27






