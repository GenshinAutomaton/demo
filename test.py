import pyautogui as pgi
import time
from packages.chooseInstance import open_guide_book, choose_instance, begin_instance
from packages.attack import *
import torch
from findIns import find_instance
from detect import load_model
import sys, json
import argparse
import redis


def LeiYeBanZhong():
    begin_instance()
    for i in range(0, 10):
        change_with_EQ(4, 0, 2.5, True)
        change_with_QEQ(3, 1, 1, False)
        change_with_QEQ(2, 1, 1.5, False)
        change_with_EQ(1, 1, 1, False)

        for i in range(0, 16):
            A(0.5, False)


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=str, required=True)
    args = parser.parse_args()
    return args


def push(username, msg):
    name = "MiJing:" + username
    r.set(name, msg, ex=300)


'''
receive
{
    \"ins\": {\"1\": \"2\", \"2\": \"3\"},
    \"user\": \"Owenovo\",
    \"pwd\": \"Lmq1226lmq\"
}
'''

'''
send
{
    \"cur\": \"1\",
    \"fin\": {\"1\": \"2\", \"2\": \"3\"}
}
'''

if __name__ == "__main__":
    isTest = True

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    imgsz = 640
    weightPath = r'./param/instance.pt'  # 权重文件

    args = getArgs()
    data = args.json
    data = json.loads(data)

    print("linking to redis...")
    username = data['user']
    pwd = data['pwd']
    r = redis.Redis(host='r-bp18tyvha4i273d7x4pd.redis.rds.aliyuncs.com', port=6379, password=pwd)  

    print("loading models...")
    model = load_model(device, weightPath, imgsz)
    print("Start")
    time.sleep(2)

    if isTest == True:
        r.set(username, '3', ex=300)

        # print(pgi.position())
        # open_guide_book(3)
        # choose_instance(device, model, imgsz, 10)
        # LeiYeBanZhong()
        # find_instance(device, model, imgsz)
    else:
        msg = {}
        fin = {}
        ins = data['ins']
        for i in range(1, 20):
            curr = str(i)
            if (curr not in ins.keys()):
                continue
            num = int(ins[curr])
            open_guide_book(3)
            choose_instance(device, model, imgsz, i)
            for j in range(0, num): # curr 是当前秘境，发给前端
                msg["cur"] = curr
                push(username, msg)
                print("curr: %s, number: %d" % (curr, j))
                begin_instance()
                # LeiYeBanZhong()
                # 打怪
                # 领取奖励
                
                fin[curr] += 1
                msg["cur"] = 0
                msg["fin"] = fin
                push(username, msg)
                if j != num-1:
                    # 继续秘境
                    ...
                else:
                    # 退出秘境
                    ...
