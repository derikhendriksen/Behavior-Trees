import bt_library as btl
from ..globals import HOME_PATH


class GoHome(btl.Task):

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Going Home")

        home_path = blackboard.get_in_environment(HOME_PATH, "")
        if home_path:
            return self.report_succeeded(blackboard)
        else:
            print("Home path not found")
            return self.report_failed(blackboard)
