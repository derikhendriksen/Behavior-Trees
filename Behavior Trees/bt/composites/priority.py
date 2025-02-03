from bt_library import Composite, Blackboard, ResultEnum


class Priority(Composite):

    def __init__(self, children: list):
        super().__init__(children)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        for child in self.children:
            result = child.run(blackboard)
            if result == ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard)
            elif result == ResultEnum.RUNNING:
                return self.report_running(blackboard)
        return self.report_failed(blackboard)
