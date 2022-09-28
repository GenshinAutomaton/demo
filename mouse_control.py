import win32api
import win32con
from grabscreen import GrabScreen


def lock(aim, deltaX, deltaY):
    g = GrabScreen()
    scaling = g.get_scaling()
    if aim is not None:
        mouse_pos_x, mouse_pos_y = win32api.GetCursorPos()
        tag, x_center, y_center, width, height = aim
        mouse_pos_x *= scaling
        mouse_pos_y *= scaling
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x_center - mouse_pos_x + deltaX),
                                                        int(y_center - mouse_pos_y + deltaY))
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, deltaX, deltaY)
