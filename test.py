import pyautogui
import time
from package.chooseInstance import ChenSha, open_guide_book, choose_instance
from package.attack import *


def LeiYeBanZhong():
    begin_instance()
    for i in range(0, 10):
        change_with_EQ(4, 0, 2.5, True)
        change_with_QEQ(3, 1, 1, False)
        change_with_QEQ(2, 1, 1.5, False)
        change_with_EQ(1, 1, 1, False)

        for i in range(0, 16):
            A(0.5, False)


if __name__ == "__main__":
    # time.sleep(2)
    # print(pyautogui.position())
    open_guide_book(3)
    choose_instance(16)
    ChenSha()
    LeiYeBanZhong()
