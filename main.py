#Hi Guys Zappricious Here!
#This is a program that auto-grinds coins

import pyautogui
import time
import random

time.sleep(5)

default_cl = 2

clickx,clicky = 503,887

rand_item = ['shovel', 'rifle', 'fishing', 'lifesaver', 'lucky']


def write(string, cooldown):
    pyautogui.write(string)
    pyautogui.press('enter')
    time.sleep(cooldown)


def basic_cmd():
    write('----------------------THIS IS A PROGRAM RUNNING--------------------', default_cl)
    write('pls use lucky', default_cl)
    write('pls beg', default_cl)
    write('pls dig', default_cl)
    write('pls fish', default_cl)
    write('pls hunt', default_cl)
    write('pls pm', default_cl)
    pyautogui.click(847,882)
    time.sleep(1)

    write('pls search', default_cl)
    pyautogui.click(clickx,clicky)
    time.sleep(1)

    write('pls crime', default_cl)
    pyautogui.click(clickx,clicky)
    time.sleep(1)

    write('pls dep max', default_cl)


    to_buy = random.choice(rand_item)
    write(f'pls buy {to_buy}', 0)

while True:
    basic_cmd()
    time.sleep(15)





