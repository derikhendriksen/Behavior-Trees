import bt_library as btl
from ..globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Condition):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Evaluating Dusty Spot Condition")

        # Checks if DUSTY_SPOT_SENSOR is True in the blackboard
        is_dusty_spot = blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False)

        # Returns SUCCEEDED if dusty spot is detected, otherwise returns FAILED
        if is_dusty_spot:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
