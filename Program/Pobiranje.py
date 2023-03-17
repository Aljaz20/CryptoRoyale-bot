import pyautogui
import time

time.sleep(3)


def pobiranje():
    pyautogui.click(330, 310)
    time.sleep(3)
    a = 0
    while a<2:
        pyautogui.click(570, 480)
        time.sleep(2)
        a=a+1
    pyautogui.click(1690, 80)
    time.sleep(1)


