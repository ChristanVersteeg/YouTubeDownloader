import win32gui as gui
import win32con as con

hwnd = gui.GetForegroundWindow()

def window(constant):
    gui.SetWindowPos(hwnd, constant, 0, 0, 0, 0, con.SWP_NOMOVE | con.SWP_NOSIZE)

if (gui.GetWindowLong(hwnd, con.GWL_EXSTYLE) & con.WS_EX_TOPMOST) == con.WS_EX_TOPMOST:
    window(con.HWND_NOTOPMOST)
else:
    window(con.HWND_TOPMOST)