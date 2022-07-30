import pyautogui
import time



def open_guide_book(bookLabel: int):
    time.sleep(2)
    pyautogui.keyDown('f1')
    pyautogui.keyUp('f1')

    time.sleep(1)

    x = 400
    y = 575

    # 选择秘境 / 每日任务
    if bookLabel == 3:
        x = 400
        y = 575
        
    pyautogui.moveTo(x, y)
    pyautogui.click()


def choose_instance(insId: int):
    pyautogui.moveTo(2064, 1050)
    if insId <= 4:
        # 不用滚动
        ...

    else:
        roll = 7.7 * （insId - 4） # 待验证
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
