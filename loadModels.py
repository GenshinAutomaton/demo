import torch
import torch.nn as nn
from .utils.downloads import attempt_download


class Ensemble(nn.ModuleList):
    # Ensemble of models
    def __init__(self):
        super().__init__()

    def forward(self, x, augment=False, profile=False, visualize=False):
        y = []
        for module in self:
            y.append(module(x, augment, profile, visualize)[0])
        # y = torch.stack(y).max(0)[0]  # max ensemble
        # y = torch.stack(y).mean(0)  # mean ensemble
        y = torch.cat(y, 1)  # nms ensemble
        return y, None  # inference, train output


def attempt_load(weights, device=None, fuse=True):
    # from models.yolo import Detect, Model
    model = Ensemble()
    ckpt = torch.load(attempt_download(weights), map_location=device)  # load
    if fuse:
        model.append(ckpt['ema' if ckpt.get('ema') else 'model'].float().fuse().eval())  # FP32 model
    else:
        model.append(ckpt['ema' if ckpt.get('ema') else 'model'].float().eval())  # without layer fuse


def load_module(device, weightPath, imgsz):
    model = attempt_load(weightPath, device=device)
    if device == 'cuda':
        model.half()
    else:
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))
    return model