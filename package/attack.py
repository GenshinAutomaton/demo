import pyautogui
import time

'''
id 一定要是 字符，而不是数字
'''

def change_legend(id: str):
    pyautogui.keyDown(id)
    pyautogui.keyUp(id)


def A(ARecovery: float, isLongA: bool):
    if isLongA == True:
        pyautogui.mouseDown('right')
        time.sleep(1.5)
        pyautogui.mouseUp('right')
    else:
        pyautogui.click()
        time.sleep(ARecovery)


def long_E():
    pyautogui.keyDown('e')
    time.sleep(1.5)
    pyautogui.keyUp('e')


def QE(ERecovery: float, QRecovery: float, isLongE: bool):
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    time.sleep(QRecovery)

    if isLongE == True:
        long_E()
    else:
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')
    time.sleep(ERecovery)


def EQ(ERecovery: float, QRecovery: float, isLongE: bool):
    if isLongE == True:
        long_E()
    else:
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')

    time.sleep(ERecovery)
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    time.sleep(QRecovery)


def change_with_Q(id: str, QRecovery: float):
    pyautogui.keyDown('q')
    change_legend(id)
    pyautogui.keyUp('q')
    time.sleep(QRecovery)


def change_with_EQ(id: str, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    EQ(ERecovery, QRecovery, isLongE)


def change_with_QE(id: str, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    QE(ERecovery, QRecovery, isLongE)


def change_with_QEQ(id: str, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    QE(ERecovery, QRecovery, isLongE)
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    time.sleep(QRecovery)
