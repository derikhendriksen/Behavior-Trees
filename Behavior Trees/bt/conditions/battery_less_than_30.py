#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import BATTERY_LEVEL


class BatteryLessThan30(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        battery_level = blackboard.get_in_environment(BATTERY_LEVEL, 0)
        self.print_message(f"Current battery level is: {battery_level}")

        if battery_level < 30:
            self.print_message("Battery is less than 30%. Need to charge.")
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
