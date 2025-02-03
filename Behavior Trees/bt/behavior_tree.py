from bt_library import Composite, Blackboard, ResultEnum, Timer
from .conditions.battery_less_than_30 import BatteryLessThan30
from .conditions.spot_cleaning import SpotCleaning
from .conditions.general_cleaning import GeneralCleaning
from .conditions.dusty_spot import DustySpot
from .tasks.find_home import FindHome
from .tasks.go_home import GoHome
from .tasks.dock import Dock
from .tasks.clean_spot import CleanSpot
from .tasks.done_general import DoneGeneral
from .tasks.done_spot import DoneSpot
from .tasks.clean_floor import CleanFloor
from .tasks.do_nothing import DoNothing
from .tasks.always_fail import AlwaysFail
from .composites.sequence import Sequence
from .composites.priority import Priority
from .composites.selection import Selection
from .decorators.until_fails import UntilFails


def build_bt():
    print("Initializing...")

    # Battery < 30 Sequence
    battery_sub_30_sequence = Sequence([
        BatteryLessThan30(),
        FindHome(),
        GoHome(),
        Dock(),
    ])

    # Spot Cleaning Sequence
    spot_cleaning_sequence = Sequence([
        SpotCleaning(),
        Timer(20, CleanSpot()),
        DoneSpot(),
    ])

    # Dusty Spot Sequence
    dusty_spot_sequence = Sequence([
        DustySpot(),
        Timer(35, CleanSpot()),
        AlwaysFail(),
    ])

    # General Cleaning Sequence
    general_cleaning_sequence = Sequence([
        GeneralCleaning(),
    ])

    # Nested Priority within General Cleaning Sequence
    nested_priority_in_general_cleaning = Priority([
        dusty_spot_sequence,
        UntilFails(CleanFloor()),
    ])

    # Full General Cleaning Sequence with Nested Priority
    full_general_cleaning_sequence = Sequence([
        general_cleaning_sequence,
        nested_priority_in_general_cleaning,
        DoneGeneral(),
    ])

    # Cleaning Selector (Spot Cleaning and General Cleaning)
    cleaning_selector = Selection([
        spot_cleaning_sequence,
        full_general_cleaning_sequence,
    ])

    # Root Priority Composite
    root_node_priority = Priority([
        battery_sub_30_sequence,
        cleaning_selector,
        DoNothing(),
    ])

    print("\n")
    return root_node_priority


# Assign the root of the tree
tree_root = build_bt()
