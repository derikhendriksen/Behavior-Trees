from bt_library.blackboard import Blackboard
from bt.behavior_tree import tree_root
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH
import time
import random

# Initialize the blackboard
current_blackboard = Blackboard()

# Take user input for the starting battery level of the Roomba
print("Enter initial battery level (0-100):")
battery_level = int(input())
current_blackboard.set_in_environment(BATTERY_LEVEL, battery_level)

# Ensure other cleaning modes are false by default
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)

if battery_level >= 30:
    print("Enter which mode you would like to begin with: \n"
          "1) Spot Cleaning Mode \n"
          "2) Dusty Spot Cleaning Mode \n"
          "3) General Cleaning Mode")

    current_mode = int(input())

    if current_mode == 1:
        current_blackboard.set_in_environment(SPOT_CLEANING, True)
    elif current_mode == 2:
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
    elif current_mode == 3:
        current_blackboard.set_in_environment(GENERAL_CLEANING, True)
else:
    print("Battery level is low. Charging mode activated.")

current_blackboard.set_in_environment(HOME_PATH, "")

current_iterations = 0
max_iterations = 100

done = False
while not done and current_iterations < max_iterations:
    blackboard_state = {
        "BATTERY_LEVEL": current_blackboard.get_in_environment(BATTERY_LEVEL, None),
        "SPOT_CLEANING": current_blackboard.get_in_environment(SPOT_CLEANING, None),
        "GENERAL_CLEANING": current_blackboard.get_in_environment(GENERAL_CLEANING, None),
        "DUSTY_SPOT_SENSOR": current_blackboard.get_in_environment(DUSTY_SPOT_SENSOR, None),
        "HOME_PATH": current_blackboard.get_in_environment(HOME_PATH, None),
    }

    print("Blackboard:")
    for key, value in blackboard_state.items():
        print(f"{key}: {value}")

    # Update the DUSTY_SPOT_SENSOR value randomly or via user input
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, random.choice([True, False]))

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)

    # Print the result of the tree evaluation
    print("Tree evaluation result:", result)

    battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, battery_level) - 1
    current_blackboard.set_in_environment(BATTERY_LEVEL, battery_level)

    # Ensure General Cleaning continues if it should
    if current_blackboard.get_in_environment(GENERAL_CLEANING, False):
        current_blackboard.set_in_environment(GENERAL_CLEANING, True)

    # Sleep for 1 second to simulate time passing
    time.sleep(1)
    current_iterations += 1
