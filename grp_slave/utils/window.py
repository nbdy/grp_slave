import re
from typing import Optional

import pywinctl

WINDOW_PATTERN = re.compile(r"RAG. Multi.la.er")


def get_window_title():
    titles = pywinctl.getAllTitles()

    for title in titles:
        if WINDOW_PATTERN.match(title):
            return title

    return None


def find_window() -> Optional[pywinctl.Window]:
    title = get_window_title()
    if title is None:
        return None
    return pywinctl.getWindowsWithTitle(title)[0]
