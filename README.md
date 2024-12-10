# **Open Manipulator Pro Description**  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## **Overview**
Repository to group URDF, launch files, rviz configuration, meshes for the OpenManipulatorPro.

### **License**

This project is licensed under the [MIT License](LICENSE).

**Author**: Deivid Gomes\
**Affiliation**: Brazilian Institute of Robotics - BIR\
**Maintainer**: Deivid Gomes, deivid.silva@fbter.org.br

## **Requirements**

The `open_manipulator_pro_description` package has been tested under:

- ROS2 [`Humble Hawksbill`](https://docs.ros.org/en/humble/Releases/Release-Humble-Hawksbill.html) and Ubuntu 22.04 LTS (Jammy Jellyfish).

Ahead its presented the packages and libraries used in the repository:

## **Installation**
1. Clone this repository into your workspace:
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/deividG0/open_manipulator_pro_description.git
    ```
2. Install dependencies:
    ```bash
    cd ~/ros2_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```
3. Build the workspace:
    ```bash
    cd ~/ros2_ws
    colcon build --symlink-install --event-handlers console_direct+
    ```

## **Usage**

To only view the robot on rviz2, run the following command:

```
ros2 launch open_manipulator_pro_description view_robot.launch.py enable_joint_state_publisher_gui:=true
```

> **NOTE:** The argument `enable_joint_state_publisher_gui` is needed to provide the manipulator's tf tree. When using the ros2_control, it is not required because the `joint_state_broadcaster` provides the tree.

### **Configuration**

**[initial_positions.yaml](open_manipulator_pro_description/config/initial_positions.yaml):** Initial joint values for the manipulator.

### **Contributing**

To contribute to this package, you can either [open an issue](https://github.com/deividG0/open_manipulator_pro_description/issues) describing the desired subject or develop the feature yourself and [submit a pull request](https://github.com/deividG0/open_manipulator_pro_description/pulls) to the main branch.

If you choose to develop the feature yourself, please adhere to the [ROS 2 Code style and language] guidelines to improve code readability and maintainability.

