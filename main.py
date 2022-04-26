import pyautogui
import time

def basic_cmd():
    pyautogui.write('pls use lucky')
    pyautogui.press('enter')
    pyautogui.write('pls beg')
    pyautogui.press('enter')
    pyautogui.write('pls dig')
    pyautogui.press('enter')
    pyautogui.write('pls fish')
    pyautogui.press('enter')
    pyautogui.write('pls hunt')
    pyautogui.press('enter')
    pyautogui.write('pls dep max')
    pyautogui.press('enter')


    time.sleep(45)

while True:
    time.sleep(5)
    basic_cmd()


