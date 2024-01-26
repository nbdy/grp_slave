from enum import Enum

from grp_slave.tasks.fishing import FishingTask
from grp_slave.tasks.mining import MiningTask
from grp_slave.tasks.oil_rig import OilRig


class Task(str, Enum):
    OIL = "Oil rig"
    MINING = "Mining"
    FISHING = "Fishing"

    def run(self, offsets: tuple[int, int]):
        match self:
            case Task.MINING:
                MiningTask().run(offsets)
            case Task.OIL:
                OilRig().run(offsets)
            case Task.FISHING:
                FishingTask().run(offsets)

    def implemented(self):
        ret = False

        match self:
            case Task.OIL:
                ret = True
            case Task.MINING:
                ret = True
            case Task.FISHING:
                ret = True

        return ret

    def button_state(self):
        if self.implemented():
            return "normal"
        return "disabled"
