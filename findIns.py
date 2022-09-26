import torch
from utils.general import scale_coords, xyxy2xywh
from mouse_control import lock
from grabscreen import GrabScreen
from detect import manipulate_img, detect, load_model


def find_instance(device, model, imgsz):
    grabimg = GrabScreen()
    originImg = grabimg.grab_screen("原神", "UnityWndClass")
    img = manipulate_img(device, model, originImg, imgsz)
    pred = detect(model, img)

    aims = []
    for det in pred:
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], originImg.shape).round()
            for *xyxy, conf, clss in reversed(det):
                xywh = xyxy2xywh(torch.tensor(xyxy).view(1, 4)).view(-1).tolist()
                aim = (int(clss.tolist()), *xywh)  # label format
                aims.append(aim)

    if len(aims):
        lock(aims[0], 0, 0)
        return True
    else:
        lock(None, 500, 0)
        return False


if __name__ == "__main__":
    imgsz = 640
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    weightPath = r'../train/instance.pt'  # 权重文件
    model = load_model(device, weightPath, imgsz)
    find_instance(device, model, imgsz)
