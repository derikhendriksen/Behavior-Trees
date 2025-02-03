import bt_library as btl
from ..globals import GENERAL_CLEANING


class GeneralCleaning(btl.Condition):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Evaluating General Cleaning Condition")

        is_general_cleaning = blackboard.get_in_environment(GENERAL_CLEANING, False)

        if is_general_cleaning:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
