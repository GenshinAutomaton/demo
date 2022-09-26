import pyautogui


def get_Rev():
    width, height = pyautogui.size()
    return width, height


def get_Prob_with_2K():
    width, height = pyautogui.size()
    return width / 2560, height / 1440


def get_correct_Pos(x, y):
    '''
    x 和 y 是在 2k 分辨率下算出的坐标，该函数的作用是把在 2k 分辨率下预先算好的
    各种坐标转换成其它分辨率下的坐标。
    返回值是 int 类型。
    '''
    probx, proby = get_Prob_with_2K()
    return int(x * probx), int(y * proby)