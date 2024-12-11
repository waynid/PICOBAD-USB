import time
import os
import usb_hid
from keycode_win_fr import Keycode as badUSB
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_fr import KeyboardLayout as KeyboardLayoutFR                                                                         

time.sleep(5)

keyboard = Keyboard(usb_hid.devices)

layout = KeyboardLayoutFR(keyboard)

#  _____    __     ___      ____          _____      _    _ ______ _____  ______ 
# |  __ \ /\\ \   / / |    / __ \   /\   |  __ \    | |  | |  ____|  __ \|  ____|
# | |__) /  \\ \_/ /| |   | |  | | /  \  | |  | |   | |__| | |__  | |__) | |__   
# |  ___/ /\ \\   / | |   | |  | |/ /\ \ | |  | |   |  __  |  __| |  _  /|  __|  
# | |  / ____ \| |  | |___| |__| / ____ \| |__| |   | |  | | |____| | \ \| |____ 
# |_| /_/    \_\_|  |______\____/_/    \_\_____/    |_|  |_|______|_|  \_\______|   

keyboard.send(badUSB.WINDOWS, badUSB.R)

time.sleep(1)

layout.write("cmd")

time.sleep(1)

keyboard.send(badUSB.ENTER)

time.sleep(1)

layout.write("@echo off")
    
keyboard.send(badUSB.ENTER)

layout.write("cls && echo Welcome to PICOBAD-USB ! THIS IS THE BASE CODE.")
    
keyboard.send(badUSB.ENTER)

time.sleep(1)

layout.write("start https://github.com/waynid/PICOBAD-USB")

keyboard.send(badUSB.ENTER)

time.sleep(1)
