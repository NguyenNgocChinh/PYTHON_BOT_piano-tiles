'''
require package
1. pip install pyautogui
2. pip install pillow
3. pip install keyboard
4. pip install pypiwin32
'''

'''
first point X: 680 Y: 460
each point distance about 80
RGB: 1,1,1
'''

'''
pyautogui.displayMousePosition()
check point in cursor and color
'''

from time import sleep

import keyboard
import pyautogui
import win32api
import win32con
import win32gui
from pyautogui import *
import threading

STOP = False
positions = []
pos_x_first = 680
pos_y = 495
for x in range(4):
    pos_x = x * 80 + pos_x_first
    positions.append((pos_x, pos_y))
time_sleep_by_thread = 0.06


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def pre_click(x, y):
    print(str(pyautogui.pixel(x, y)[0]) + ',' + str(pyautogui.pixel(x, y)[1]) + ',' + str(pyautogui.pixel(x, y)[2]))
    if pyautogui.pixel(x, y)[0] <= 1:
        click(x, y)
        print(f'click at {x},{y}')
        sleep(0.15)


def watch_stop():
    global STOP
    while not STOP:
        if keyboard.is_pressed('q'):
            print('STOOOOOOOOOPPPPPPPPPPPPPPPP')
            STOP = True
        sleep(0.1)


def main():
    thread_stop = threading.Thread(target=watch_stop)
    thread_stop.start()
    while not STOP:
        for pos in positions:
            if pyautogui.pixel(pos[0], pos[1])[0] < 2:
                click(pos[0], pos[1])
                sleep(0.035)


if __name__ == '__main__':
    main()
    # pyautogui.displayMousePosition()
