import bt_library as btl
import random


class CleanFloor(btl.Task):

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Floor")

        # Simulate ongoing cleaning process with a chance to fail
        if random.random() < 0.1:
            self.print_message("Cleaning Floor Failed")
            return self.report_failed(blackboard)
        else:
            return self.report_running(blackboard)
