from typing import Optional

import pywinctl


def get_window_title(contains: str = "RAGЕ"):
    for title in pywinctl.getAllTitles():
        if contains in title:
            return title
    return None


def find_window(name: str = "RAGE") -> Optional[pywinctl.Window]:
    title = get_window_title(name)
    if title is None:
        return None
    return pywinctl.getWindowsWithTitle(title)[0]
