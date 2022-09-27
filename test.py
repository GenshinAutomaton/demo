import pyautogui as pgi
import time
from packages.chooseInstance import open_guide_book, choose_instance, begin_instance
from packages.attack import *
import torch
from findIns import find_instance
from detect import load_model
import sys, json


def LeiYeBanZhong():
    begin_instance()
    for i in range(0, 10):
        change_with_EQ(4, 0, 2.5, True)
        change_with_QEQ(3, 1, 1, False)
        change_with_QEQ(2, 1, 1.5, False)
        change_with_EQ(1, 1, 1, False)

        for i in range(0, 16):
            A(0.5, False)


def push(dct):
    print(json.dumps(dct))
    sys.stdout.flush()


def pull()
    lines = sys.stdin.readlines()
    data = json.loads(lines)
    return data

# json {key=秘境id：value=次数}
if __name__ == "__main__":
    isTest = True

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    imgsz = 640
    weightPath = r'./param/instance.pt'  # 权重文件
    model = load_model(device, weightPath, imgsz)
    print("Start")
    time.sleep(2)

    if isTest == True:
        # print(pgi.position())
        open_guide_book(3)
        choose_instance(device, model, imgsz, 10)
        # LeiYeBanZhong()
        # find_instance(device, model, imgsz)
        ...
    else:
        data = pull()
        for i in range(1, 20):
            curr = str(i)
            if data[curr] != 0:
                open_guide_book(3)
                for j in range(0, data[curr]): # curr 是当前秘境，发给前端
                    push({curr: "doing"})
                    print("dododo")
                    # choose_instance(device, model, imgsz, i)
                    # LeiYeBanZhong()
                    # 打怪
                    # 领取奖励
                    
                    push({curr: "done"})
                    if j != data[curr]-1:
                        # 继续秘境
                        ...
                    else:
                        # 退出秘境
                        ...
