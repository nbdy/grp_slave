import time
import pyautogui


def hold_key(key: str, timeout: int = 5):
    pyautogui.keyDown(key)
    time.sleep(timeout)
    pyautogui.keyUp(key)
