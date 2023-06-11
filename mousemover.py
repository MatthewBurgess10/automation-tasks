#this file is for a program that moves the mouse around automatically
from pynput.mouse import Button, Controller
import time
import random


mouse = Controller()
run = True

mouse.position = 100, 100
while run == True:
    x1 = random.randint(50, 700)
    y1 = random.randint(50, 700)
    mouse.move(x1, y1)
    time.sleep(1)
    x2 = random.randint(50, 700)
    y2 = random.randint(50, 700)
    mouse.move(x2, y2)
    time.sleep(1)
    
#to stop the script click control + c
         

