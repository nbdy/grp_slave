import time

from grp_slave.utils.keyboard import hold_key
from grp_slave.tasks import BaseTask


class MiningTask(BaseTask):
    def run(self, offsets: tuple[int, int]):
        hold_key("e", self.generate_delay(6))
        time.sleep(self.generate_delay(7))
