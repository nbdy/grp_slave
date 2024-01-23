import PIL.ImageGrab as ImageGrab
from PIL.Image import Image


def screenshot(offsets: tuple[int, int], size: tuple[int, int]) -> Image:
    return ImageGrab.grab((
        offsets[0],
        offsets[1],
        size[0],
        size[1]
    ))
