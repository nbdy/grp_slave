import random
from abc import abstractmethod


class BaseTask:
    @abstractmethod
    def run(self, offsets: tuple[int, int]):
        ...

    @classmethod
    def generate_delay(cls, seconds: float, minimum: float = 0.0, maximum: float = 2.0) -> float:
        return seconds + random.uniform(minimum, maximum)
