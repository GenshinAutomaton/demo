import pyautogui as pgi
import time
from .revolution import get_correct_Pos

import sys
sys.path.append("..")

from findIns import find_instance


def open_guide_book(bookLabel: int):
    time.sleep(2)
    pgi.keyDown('f1')
    pgi.keyUp('f1')

    time.sleep(1)

    x = 400
    y = 575

    # 选择秘境 / 每日任务
    if bookLabel == 3:
        x, y = get_correct_Pos(400, 575)
        pgi.moveTo(x, y)
        pgi.click()

        x, y = get_correct_Pos(681, 392)
        pgi.moveTo(x, y)
        pgi.click()



def choose_instance(device, model, imgsz, insId: int):
    if insId <= 4:
        # 不用滚动
        x = 2064
        y = 450
        y = y + (insId - 1) * 190
        x, y = get_correct_Pos(x, y)
        pgi.moveTo(x, y)
    else:
        x, y = get_correct_Pos(2064, 1050)
        pgi.moveTo(x, y)
        roll = 8 * (insId - 4)
        for i in range(1, int(roll)):
            pgi.scroll(-1)

    pgi.click()
    x, y = get_correct_Pos(2246, 1348)
    pgi.moveTo(x, y)
    time.sleep(2)
    pgi.click()
    time.sleep(10)

    x, y = pgi.position()
    flag = 0
    for i in range(1, 1000):
        if flag == 3:
            break
        if find_instance(device, model, imgsz) == True:
            flag += 1
        else:
            flag = 0
        time.sleep(0.5)

    pgi.keyDown('w')
    time.sleep(5)
    pgi.keyUp('w')
    pgi.keyDown('f')
    pgi.keyUp('f')

    time.sleep(6)
    x, y = get_correct_Pos(600, 660)
    pgi.moveTo(x, y)
    pgi.click()

    x, y = get_correct_Pos(2246, 1348)
    pgi.moveTo(x, y)
    pgi.click()
    time.sleep(1)
    pgi.click()


def begin_instance(insId: int):
    time.sleep(10)
    pgi.click()

    pgi.keyDown('w')
    if insId in [2, 3, 8, 9, 12, 13, 16]:
        time.sleep(17.6)
    elif insId in [1, 4, 5, 7, 11]:
        time.sleep(10)
    elif insId in [10, 14, 15]:
        time.sleep(14.8)
    elif insId == 17:
        time.sleep(16.5)
    elif insId == 6:
        time.sleep(8.5)
    elif insId == 19:
        time.sleep(17)
    pgi.keyUp('w')
    # pgi.keyDown('f')
    # pgi.keyUp('f')
