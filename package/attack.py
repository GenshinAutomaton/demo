import pyautogui
import time


def change_legend(id: int):
    map = {1: '1', 2: '2', 3: '3', 4: '4'}
    sid = map[id]
    pyautogui.keyDown(sid)
    pyautogui.keyUp(sid)


def A(ARecovery: float, isLongA: bool):
    if isLongA == True:
        pyautogui.mouseDown('left')
        time.sleep(1.5)
        pyautogui.mouseUp('left')
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


def change_with_Q(id: int, QRecovery: float):
    pyautogui.keyDown('q')
    change_legend(id)
    pyautogui.keyUp('q')
    time.sleep(QRecovery)


def change_with_EQ(id: int, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    EQ(ERecovery, QRecovery, isLongE)


def change_with_QE(id: int, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    QE(ERecovery, QRecovery, isLongE)


def change_with_QEQ(id: int, ERecovery: float, QRecovery: float, isLongE: bool):
    change_legend(id)
    QE(ERecovery, QRecovery, isLongE)
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    time.sleep(QRecovery)
