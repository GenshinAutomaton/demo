import pyautogui


def get_Rev():
    width, height = pyautogui.size()
    return width, height


def get_Prob_with_2K():
    width, height = get_Rev()
    return width / 2560, height / 1440
