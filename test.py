import pyautogui
import time
from package.chooseBoss import ChenSha
from package.attack import change_legend


def LeiYeBanZhong():
    pyautogui.click()
    pyautogui.keyDown('w')
    time.sleep(17.8)
    pyautogui.keyUp('w')
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')

    change_legend('4')

    pyautogui.keyDown('e')
    time.sleep(1.5)
    pyautogui.keyUp('e')

    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    change_legend('3')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    time.sleep(1)

    pyautogui.keyDown('e')
    pyautogui.keyUp('e')

    time.sleep(1)

    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    time.sleep(1)

    change_legend('2')

    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    time.sleep(1)

    pyautogui.keyDown('e')
    pyautogui.keyUp('e')

    time.sleep(1)

    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    time.sleep(1)

    change_legend('1')

    pyautogui.keyDown('e')
    pyautogui.keyUp('e')

    time.sleep(1)

    pyautogui.keyDown('q')
    pyautogui.keyUp('q')

    for i in range(0, 16):
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')

        time.sleep(0.5)


if __name__ == "__main__":
    ChenSha()
    LeiYeBanZhong()
