import cv2
import numpy as np
import win32ui
import win32api
import win32con
import win32gui
import win32print


class GrabScreen:
    def __init__(self):
        # 获取真实的分辨率
        self.hwin = None
        hDC = win32gui.GetDC(0)
        self.realWide = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        self.realHigh = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        # 获取缩放后的分辨率
        scaledWide = win32api.GetSystemMetrics(0)
        # 获取屏幕的缩放比例
        self.scaling = round(self.realWide / scaledWide, 2)

    def get_resolution(self):
        return self.realWide, self.realHigh

    def get_scaling(self):
        return self.scaling

    # "Respawn001", "Apex Legends"
    # "原神", "UnityWndClass"
    def grab_screen(self, winClass, winName):
        # 获取后台窗口的句柄，注意后台窗口不能最小化
        # 窗口的类名可以用 Visual Studio 的 SPY++ 工具获取
        self.hwin = win32gui.FindWindow(winClass, winName)
        if not self.hwin:
            self.hwin = win32gui.GetDesktopWindow()

        left, top, right, bottom = win32gui.GetClientRect(self.hwin)
        width = int((right - left) * self.scaling)
        height = int((bottom - top) * self.scaling)

        # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
        hwinDC = win32gui.GetWindowDC(self.hwin)
        # 创建设备描述表
        srcDC = win32ui.CreateDCFromHandle(hwinDC)
        # 创建内存设备描述表
        memDC = srcDC.CreateCompatibleDC()
        # 创建位图对象准备保存图片
        bmp = win32ui.CreateBitmap()
        # 为 bmp 开辟存储空间
        bmp.CreateCompatibleBitmap(srcDC, width, height)
        # 将截图保存到saveBitMap中
        memDC.SelectObject(bmp)
        # 保存 bmp 到内存设备描述表
        memDC.BitBlt((0, 0), (width, height), srcDC, (left, top), win32con.SRCCOPY)
        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (height, width, 4)

        srcDC.DeleteDC()
        memDC.DeleteDC()
        win32gui.ReleaseDC(self.hwin, hwinDC)
        win32gui.DeleteObject(bmp.GetHandle())
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
