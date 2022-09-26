import torch
import numpy as np
from utils.datasets import letterbox
from models.experimental import attempt_load
from utils.general import non_max_suppression


def load_model(device, weights, imgsz):
    print("loading models...")
    model = attempt_load(weights, map_location=device)
    if device == 'cuda':
        model.half()
    else:
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))
    return model


def manipulate_img(device, model, originImg, imgsz):
    # 重构 detect
    stride = int(model.stride.max())
    img = letterbox(originImg, imgsz, stride=stride)[0]
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half() if device == "cuda" else img.float()
    img /= 255.0
    # 如果是单张图片，那么(C,H,W)升维成(1,C,H,W)
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    return img


def detect(model, img):
    iou_thres = 0.45
    conf_thres = 0.25
    pred = model(img, augment=False)[0]
    pred = non_max_suppression(pred, conf_thres, iou_thres, agnostic=False)
    return pred
