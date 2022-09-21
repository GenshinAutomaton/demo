import pyautogui as pgi
import time
from .revolution import get_correct_Pos


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



def choose_instance(insId: int):
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
    time.sleep(1)
    pgi.click()
    begin_instance(insId)


def begin_instance(insId: int):
    time.sleep(5)
    pgi.click()
    pgi.keyDown('w')
    time.sleep(17.8)
    pgi.keyUp('w')
    pgi.keyDown('f')
    pgi.keyUp('f')


def ChenSha():
    time.sleep(5)
    pgi.keyDown('w')
    time.sleep(2)
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

    begin_instance()
