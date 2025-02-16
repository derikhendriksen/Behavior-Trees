import bt_library as btl
from ..globals import SPOT_CLEANING


class DoneSpot(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done Spot Cleaning")
        blackboard.set_in_environment(SPOT_CLEANING, False)
        return self.report_succeeded(blackboard)

