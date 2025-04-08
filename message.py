import pyautogui as pg
import time
import random

animals = ['monkey', 'donkey', 'dog']

time.sleep(8)

for i in range(100):
    a = random.choice(animals)
    pg.write(f"You are a {a}")
    pg.press('enter')