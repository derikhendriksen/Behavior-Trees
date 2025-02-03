import bt_library as btl


class DoNothing(btl.Task):
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Doing Nothing")
        return self.report_succeeded(blackboard)
