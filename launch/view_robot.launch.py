#!/usr/bin/env python3

# Copyright (c) 2024, SENAI CIMATEC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_name = 'open_manipulator_pro_description'

    # Substitution that can access launch configuration variables
    enable_joint_state_publisher_gui = LaunchConfiguration(
        variable_name='enable_joint_state_publisher_gui'
    )

    robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                FindPackageShare(pkg_name),
                '/launch',
                '/robot_description.launch.py'
            ]
        )
    )

    # The argument will be exposed via a command line option for a root launch
    # description, or as action configurations to the include launch
    # description action for the included launch description.
    enable_joint_state_publisher_gui_arg = DeclareLaunchArgument(
        name='enable_joint_state_publisher_gui',
        default_value='false',
        description="True to launch the joint state "
                    "publisher gui, false otherwise",
        choices=['true', 'false']
    )

    rviz_config = os.path.join(
      get_package_share_directory(pkg_name),
      'config',
      'open_manipulator_pro.rviz'
    )

    return LaunchDescription([
        enable_joint_state_publisher_gui_arg,
        robot_description,
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            condition=IfCondition(enable_joint_state_publisher_gui)
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            arguments=['-d', rviz_config]
        )
    ])
