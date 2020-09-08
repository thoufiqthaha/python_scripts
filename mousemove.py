#! python3

import pyautogui
import time
import random

print("Press Ctrl-C to quit.")
x=0
#a= time.clock()
print (x)   
#print (a)
#b= str (a)
#c= b[3:6]
#d= int (c)
#print (d)
pyautogui.FAILSAFE = False
try:
    while True:
        a= time.clock()
        b= str(a)
        c = b[4:7]
        print (c)
        d = int (c)
        #pyautogui.moveTo(600, 200, duration = 10)
        #pyautogui.moveTo(800, 400, duration = 10)
        pyautogui.moveTo(d, 200)
        time.sleep (4)
        pyautogui.moveTo(d, 400)
        time.sleep (4)
        x=x+20
        print (x)
except KeyboardInterrupt:
    print('\n')