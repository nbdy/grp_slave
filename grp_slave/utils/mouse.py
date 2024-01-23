import time
import pyautogui


def hold_mouse(coords: tuple, timeout: int = 5):
    pyautogui.mouseDown(coords[0], coords[1])
    time.sleep(timeout)
    pyautogui.mouseUp(coords[0], coords[1])
