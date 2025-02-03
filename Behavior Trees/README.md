# Behavior Tree Implementation for Roomba Vacuum

## Overview

This project implements a basic reflex agent using a behavior tree. The agent is designed to perform cleaning tasks based on battery level, dust sensor, and predefined conditions for spot and general cleaning. The implementation uses a blackboard to store the state of the environment, with tasks being simulated through print statements to indicate their status.

## Functionality

The behavior tree consists of the following components:

1. **Blackboard**: A shared memory space to store the state of the environment (percepts) and the status of tasks.
2. **Sensor Simulation**: Random values or user input simulate sensor data such as battery level and dust detection.
3. **Behavior Tree Evaluation**: A tree structure that evaluates conditions and executes tasks based on predefined rules using a hierarchical structure of composites, conditions, and tasks.

### Components

1. **Root Node (Priority Composite)**:
   - **Battery < 30 Sequence**: Checks if the battery level is below 30% and if true, executes a sequence to find home, go home, and dock.
   - **Cleaning Selector**: Chooses between spot cleaning and general cleaning.
   - **Do Nothing Task**: Executes if no other tasks are needed.

2. **Battery < 30 Sequence**:
   - **BatteryLessThan30 Condition**: Checks if the battery level is below 30%.
   - **FindHome Task**: Finds the docking station.
   - **GoHome Task**: Moves towards the docking station.
   - **Dock Task**: Docks to recharge.

3. **Cleaning Selector (Selection Composite)**:
   - **Spot Cleaning Sequence**: Executes if the spot cleaning condition is true.
   - **General Cleaning Sequence**: Executes if the general cleaning condition is true.

4. **Spot Cleaning Sequence**:
   - **SpotCleaning Condition**: Checks if the spot cleaning task is active.
   - **CleanSpot Task**: Cleans the spot for 20 seconds.
   - **DoneSpot Task**: Resets the spot cleaning status.

5. **General Cleaning Sequence**:
   - **GeneralCleaning Condition**: Checks if the general cleaning task is active.
   - **Nested Priority Composite**: Contains the dusty spot sequence and the clean floor task.
   - **DoneGeneral Task**: Resets the general cleaning status.

6. **Dusty Spot Sequence**:
   - **DustySpot Condition**: Checks if the dust sensor detects a dirty spot.
   - **CleanSpot Task**: Cleans the spot for 35 seconds.
   - **AlwaysFail Task**: Ensures the sequence always fails to continue cleaning the floor.

7. **Nested Priority Composite**:
   - **Dusty Spot Sequence**: Executes if a dusty spot is detected.
   - **CleanFloor Task**: Runs continuously until it fails.

### Tasks and Conditions

- **BatteryLessThan30 Condition**: Checks if the battery level is below 30%.
- **SpotCleaning Condition**: Checks if the spot cleaning task is active.
- **GeneralCleaning Condition**: Checks if the general cleaning task is active.
- **DustySpot Condition**: Checks if the dust sensor detects a dirty spot.
- **FindHome Task**: Finds the docking station.
- **GoHome Task**: Moves towards the docking station.
- **Dock Task**: Docks to recharge.
- **CleanSpot Task**: Simulates spot cleaning for 20 or 35 seconds.
- **DoneGeneral Task**: Resets the general cleaning status.
- **DoneSpot Task**: Resets the spot cleaning status.
- **CleanFloor Task**: Simulates cleaning the floor continuously.
- **DoNothing Task**: A placeholder task that runs when no other tasks are active.
- **AlwaysFail Task**: Ensures the sequence always fails to allow continued execution.

## Design Choices

### Blackboard

The blackboard is used to store the state of the environment and task statuses. This approach allows for easy sharing of state information between different parts of the behavior tree.

### Sensor Simulation

Sensors are simulated using random values to mimic real-world variability. This ensures that the agent's behavior is tested under different conditions.

### Print Statements

Tasks are implemented using print statements to indicate their status. This simplifies the implementation and focuses on the behavior tree logic without needing to implement full task functionality.

### Behavior Tree Structure

The behavior tree is structured to prioritize low battery conditions, followed by selection between spot cleaning and general cleaning tasks. This hierarchical structure ensures that critical tasks (like charging the battery) are prioritized.

## Running the Program

To run the program, simply execute the Python script. The program will update sensor values, evaluate the behavior tree, and print the status of tasks based on the current state.

python behavior_tree.py
