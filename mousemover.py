#this file is for a program that moves the mouse around automatically
import pyautogui
import sys
import keyboard

run = True

while run == True:
    pyautogui.move(200, 200)
    pyautogui.move(None, 300)
    if keyboard.is_pressed('Esc'):
        sys.exit(0)
        
