import cv2
import time
from matplotlib import pyplot as plt
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import *
from python_imagesearch.imagesearch import imagesearch_region_loop
from python_imagesearch.imagesearch import imagesearch_count
from python_imagesearch.imagesearch import region_grabber
import pyautogui



"""
time.sleep(3)
pos = imagesearch("./Yellow1.png", 0.3)
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("Yellow not found")
time.sleep(3)
pos = imagesearch("./Purple1.png", 0.3)
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("Purple not found")
"""


def iskanje1():
    pos = imagesearch("./Blue2011.png", 0.8)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("Ne najde blue")
        pos = imagesearch("./Yellow22.png", 0.8)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
        else:
            print("Ne najde yellow")
            pos = imagesearch("./Purple1.png", 0.8)
            if pos[0] != -1:
                pyautogui.moveTo(pos[0], pos[1])
            else:
                print("Ne najde purple")

def iskanje2():
    pos = imagesearch("./Captcha.png", 0.8)
    if pos[0] != -1:
        pyautogui.moveTo((pos[0] + 30), (pos[1] + 40), 0.2, pyautogui.easeOutQuad)
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey("f")
        time.sleep(2)
        pyautogui.hotkey("F5")
        time.sleep(2)
        pyautogui.hotkey("F5")
        time.sleep(2)
        pyautogui.click(1400, 950)
        time.sleep(1)
        pyautogui.click(1280, 870)
        time.sleep(2)
        pyautogui.hotkey("f")
        time.sleep(1)
        pyautogui.moveTo(1780, 210)
        pyautogui.click()
        print("Recaptcha")
    else:
        print("Ni še štartalo")
        pos = imagesearch("./Playagain.png", 0.8)
        if pos[0] != -1:
            pyautogui.moveTo((pos[0] + 80), (pos[1] + 60))
            pyautogui.click()
            time.sleep(5)
        else:
            print("Ni še štartalo")
            pos = imagesearch("./Play.png", 0.8)
            if pos[0] != -1:
                pyautogui.moveTo((pos[0] + 80), (pos[1] + 60))
                pyautogui.click()
                time.sleep(5)
                print("Zmaga")
            else:
                print("Ni zmagalo")
                pos = imagesearch("./Blue31.png", 0.8)
                if pos[0] != -1:
                    pyautogui.moveTo(pos[0], pos[1])
                    time.sleep(0.1)
                else:
                    print("Ne najde blue31")
                    pos = imagesearch("./Red1.png", 0.8)
                    if pos[0] != -1:
                        pyautogui.moveTo(pos[0], pos[1])
                        time.sleep(0.1)
                    else:
                        print("Ne najde red1")
                        pos = imagesearch("./Green1.png", 0.8)
                        if pos[0] != -1:
                            pyautogui.moveTo(pos[0], pos[1])
                            time.sleep(0.1)
                        else:
                            print("Ne najde green1")
                            pos = imagesearch("./Blue30.png", 0.8)
                            if pos[0] != -1:
                                pyautogui.moveTo(pos[0], pos[1])
                                time.sleep(0.1)
                            else:
                                print("Ne najde green")
                                pos = imagesearch("./Red.png", 0.8)
                                if pos[0] != -1:
                                    pyautogui.moveTo(pos[0], pos[1])
                                    time.sleep(0.2)
                                else:
                                    print("Ne najde blue30")
                                    pos = imagesearch("./Green.png", 0.8)
                                    if pos[0] != -1:
                                        pyautogui.moveTo(pos[0], pos[1])
                                        print("Ne najde red")
                                        time.sleep(0.2)


"""
time.sleep(2)
pos = imagesearch("./Yellow22.png", 0.9)

if pos[0] != -1:

    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(3)

else:
    print("image not found")

time.sleep(3)
pos = imagesearch("./Blue31.png", 0.8)
if pos[0] != -1:
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("Ne najde blue")


time.sleep(2)
pos = imagesearcharea("./Red.png", 500, 330, 1040, 730, 0.8)
if pos[0] != -1:
    pyautogui.moveTo(pos[0], pos[1])"""


