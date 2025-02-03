from bt_library import Blackboard, ResultEnum
from ..globals import HOME_PATH, BATTERY_LEVEL
import bt_library as btl


class Dock(btl.Task):

    def run(self, blackboard: Blackboard) -> ResultEnum:
        self.print_message("Docking at home.")
        blackboard.set_in_environment(BATTERY_LEVEL, 100)

        return self.report_succeeded(blackboard)
