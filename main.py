# Hi Guys Zappricious Here!
# This is a program that auto-grinds coins and items!

import pyautogui
import time
import random
import schedule
import keyboard

time.sleep(5)

command_cooldown = 0.2

default_cl = 2
default_speed = 0.1
clickx, clicky = 503, 887



rand_item = ['shovel', 'rifle', 'fishing', 'lifesaver', 'lucky']



def write(string, cooldown=default_cl):
    pyautogui.write(string, interval = default_speed )
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(cooldown)

def use(item, cooldown=default_cl):
    pyautogui.write('/use', interval=default_speed)
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.write(item, interval=default_speed)
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(default_cl)

def run_2(command, input, cooldown=default_cl):
    pyautogui.write(f'/{command}', interval=default_speed)
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.write(input, interval=default_speed)
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(default_cl)

def depmax(cooldown=default_cl):
    pyautogui.write('/deposit', interval=default_speed)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.write('max', interval=default_speed)
    pyautogui.press('enter')
    time.sleep(command_cooldown)
    pyautogui.press('enter')
    time.sleep(default_cl)

def click(x, y, cooldwon=default_cl):
    pyautogui.click(x, y)
    time.sleep(cooldwon)


def stream():
    write('/stream')
    click(772, 841, 1.5)
    click(695, 892, 1.5)
    click(720, 737, 1.5)

def work():
    write('/work')
    write('/use tipjar')

def start():
    use('apple')
    depmax()
    use('pizza')
    time.sleep(3)
    use('lucky')

def basic_cmd():
    write('/beg')
    write('/dig')
    write('/fish')
    write('/hunt')
    write('/postmemes')
    click(847, 882, 1)
    write('/search')
    click(clickx, clicky, 1)
    write('/crime')
    click(clickx, clicky, 1)
    write('/highlow')
    click(clickx, clicky, 1)
    depmax()
    to_buy = random.choice(rand_item)
    # write(f'/buy {to_buy}', 0)

# schedule.every(60).minutes.do(work)
schedule.every(125).minutes.do(use,'pizza')
schedule.every(33).minutes.do(use,'lucky')
# stream()
# schedule.every(10).minutes.do(stream)
start()
running = True
while running:
    basic_cmd()
    schedule.run_pending()
    click(953,649)
    time.sleep(10)






