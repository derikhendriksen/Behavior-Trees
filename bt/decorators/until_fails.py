import bt_library as btl
from bt_library.common import ResultEnum
from bt_library.tree_node import TreeNode


class UntilFails(btl.Decorator):
    def __init__(self, child: TreeNode):
        super().__init__(child)

    def run(self, blackboard: btl.Blackboard) -> ResultEnum:
        self.print_message("Running UntilFails")

        result = self.child.run(blackboard)

        if result == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
