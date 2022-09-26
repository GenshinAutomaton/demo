import pyautogui as pgi
import time
from packages.chooseInstance import open_guide_book, choose_instance, begin_instance
from packages.attack import *
import torch
from findIns import find_instance
from detect import load_model


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
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    imgsz = 640
    weightPath = r'./param/instance.pt'  # 权重文件
    model = load_model(device, weightPath, imgsz)
    print("Start")
    time.sleep(2)
    # print(pgi.position())
    open_guide_book(3)
    choose_instance(device, model, imgsz, 10)
    # LeiYeBanZhong()
    # find_instance(device, model, imgsz)
