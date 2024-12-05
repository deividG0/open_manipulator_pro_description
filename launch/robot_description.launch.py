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
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
    # Arguments values
    bool_is_real_launch = False
    is_real_launch = LaunchConfiguration(
        'is_real_launch', default=bool_is_real_launch
        )

    # Arguments
    is_real_launch_arg = DeclareLaunchArgument(
        'is_real_launch',
        default_value=is_real_launch,
        description='If true launch will be done to real robot'
    )

    pkg_name = 'open_manipulator_pro_description'

    xacro_file = os.path.join(
        get_package_share_directory(pkg_name),
        'urdf',
        'open_manipulator_pro.urdf.xacro'
    )

    robot_description = {'robot_description': Command(
        ['xacro ', xacro_file, ' is_real_launch:=', is_real_launch])}

    return LaunchDescription([
        is_real_launch_arg,
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        )
    ])
