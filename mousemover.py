#this file is for a program that moves the mouse around automatically
from pynput.mouse import controller
import time

run = True

while run == True:
    mouse.position = (100, 100)
    mouse.position = (200, 200)
    time.sleep(10)
