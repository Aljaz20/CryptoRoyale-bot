import pyautogui
import time

def zaznavanje():
    time.sleep(3)
    print("Točka 1:", pyautogui.position())
    time.sleep(5)
    print("Točka 2:", pyautogui.position())

zaznavanje()