import pyautogui as pgi
import time
from packages.chooseInstance import open_guide_book, choose_instance, begin_instance
from packages.attack import *
import torch
from findIns import find_instance
from detect import load_model
import json, argparse, redis, atexit


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


def push(username, msg, ex:int):
    name = "MiJing:" + username
    msg = msg.replace("'", '"')
    r.set(name, msg, ex=ex)


'''
receive
{
    \"ins\": {\"1\": \"2\", \"2\": \"3\"},
    \"user\": \"Owenovo\",
    \"pwd\": \"Lmq1226lmq\"
}

--json '{\"ins\": {\"1\": \"2\", \"2\": \"3\"},\"user\": \"Owenovo\",\"pwd\": \"Lmq1226lmq\"}'
python test.py --json '{\"ins\": {\"1\": \"2\", \"2\": \"3\"},\"user\": \"Owenovo\",\"pwd\": \"Lmq1226lmq\"}'
python test.py --json '{\"ins\": {\"1\": \"2\", \"2\": \"3\"},\"user\": \"lmq122677@qq.com\",\"pwd\": \"Lmq1226lmq\"}'
'''

'''
send
{
    \"cur\": \"1\",
    \"fin\": {\"1\": \"2\", \"2\": \"3\"}
}
'''
def clean(username):
    push("finish:" + username, "True", 120)


if __name__ == "__main__":
    isTest = False

    args = getArgs()
    data = args.json
    data = json.loads(data)

    print("linking to redis...")
    username = data['user']
    pwd = data['pwd']
    r = redis.Redis(host='r-bp18tyvha4i273d7x4pd.redis.rds.aliyuncs.com', port=6379, password=pwd)
    atexit.register(clean, username)

    print("loading models...")
    imgsz = 640
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    weightPath = r'./param/instance.pt'  # 权重文件
    model = load_model(device, weightPath, imgsz)
    print("Start")
    time.sleep(2)

    if isTest == True:
        # print(pgi.position())
        # open_guide_book(3)
        # choose_instance(device, model, imgsz, 10)
        # LeiYeBanZhong()
        # find_instance(device, model, imgsz)
        ...
    else:
        msg = {}
        fin = {}
        ins = data["ins"]
        for i in range(0, 19):
            curr = str(i)
            if (curr not in ins.keys()):
                continue
            num = int(ins[curr])
            # open_guide_book(3)
            # choose_instance(device, model, imgsz, i)
            for j in range(0, num): # curr 是当前秘境，发给前端
                msg["cur"] = curr
                push(username, str(msg), 300)
                print("curr: %s, number: %d" % (curr, j))
                # begin_instance()
                # LeiYeBanZhong()
                # 打怪
                # 领取奖励
                
                if curr not in fin.keys():
                    fin[curr] = 1
                else:
                    fin[curr] += 1
                del msg["cur"]
                msg["fin"] = fin

                push(username, str(msg), 300)
                if j != num-1:
                    # 继续秘境
                    ...
                else:
                    # 退出秘境
                    ...
