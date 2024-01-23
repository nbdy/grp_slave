from grp_slave.tasks import BaseTask
from grp_slave.utils.mouse import hold_mouse


class OilRig(BaseTask):
    def run(self, offsets: tuple[int, int]):
        x = offsets[0] + 300
        for i in range(4):
            hold_mouse((x + (i * 100), 760))
