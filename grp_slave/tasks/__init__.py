from abc import abstractmethod


class BaseTask:
    @abstractmethod
    def run(self, offsets: tuple[int, int]):
        ...
