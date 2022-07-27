import pyautogui
import time


def change_legend(id: str):
    pyautogui.keyDown(id)
    pyautogui.keyUp(id)


def change_with_ultimate(id):
    pyautogui.keyDown('q')
    change_legend(id)
    pyautogui.keyUp('q')


def change_with_allin(id):
    change_legend(id)
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    time.sleep(1)
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')


