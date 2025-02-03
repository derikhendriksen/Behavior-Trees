import bt_library as btl


class CleanSpot(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Spot")

        return self.report_running(blackboard)

