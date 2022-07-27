import pyautogui
import time


def ChenSha():
    time.sleep(2)
    pyautogui.keyDown('f1')
    pyautogui.keyUp('f1')

    x = 400
    y = 575

    time.sleep(1)

    pyautogui.moveTo(x, y)
    pyautogui.click()

    pyautogui.moveTo(2064, 1050)
    for i in range(1, 100):
        pyautogui.scroll(-1)

    pyautogui.click()
    pyautogui.moveTo(2246, 1348)
    time.sleep(1)
    pyautogui.click()

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
    time.sleep(5)
