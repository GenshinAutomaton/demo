import pyautogui
import time



def open_guide_book():
    time.sleep(2)
    pyautogui.keyDown('f1')
    pyautogui.keyUp('f1')

    time.sleep(1)

    # 选择秘境 / 每日任务
    x = 400
    y = 575
    pyautogui.moveTo(x, y)
    pyautogui.click()


def choose_instance():
    pyautogui.moveTo(2064, 1050)
    for i in range(1, 100):
        pyautogui.scroll(-1)

    pyautogui.click()
    pyautogui.moveTo(2246, 1348)
    time.sleep(1)
    pyautogui.click()


def begin_instance():
    time.sleep(5)
    pyautogui.click()
    pyautogui.keyDown('w')
    time.sleep(17.8)
    pyautogui.keyUp('w')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')


def ChenSha():
    open_guide_book()
    choose_instance()

    time.sleep(5)
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')

    time.sleep(6)
    pyautogui.moveTo(600, 660)
    pyautogui.click()

    pyautogui.moveTo(2246, 1348)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

    begin_instance()
