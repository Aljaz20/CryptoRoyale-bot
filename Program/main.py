import pyautogui
import time
import random
from Prepoznavanje import iskanje1
from stopwatch import Stopwatch
from Prepoznavanje import iskanje2
from Pobiranje import pobiranje



time.sleep(3)
pyautogui.hotkey("f")
time.sleep(1)
pyautogui.moveTo(1780, 210)
pyautogui.click()

stopwatch1 = Stopwatch()

stopwatch1.start()


while True:
    iskanje2()
    if stopwatch1.duration > 1.1:
        pyautogui.click()
        stopwatch1.restart()








