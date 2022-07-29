import pyautogui
import time
from package.chooseBoss import ChenSha
from package.attack import *


def LeiYeBanZhong():
    begin_instance()
    for i in range(0, 10):
        change_with_EQ('4', 0, 2.5, True)
        change_with_QEQ('3', 1, 1, False)
        change_with_QEQ('2', 1, 1.5, False)
        change_with_EQ('1', 1, 1, False)

        for i in range(0, 16):
            A(0.5, False)


if __name__ == "__main__":
    ChenSha()
    LeiYeBanZhong()
