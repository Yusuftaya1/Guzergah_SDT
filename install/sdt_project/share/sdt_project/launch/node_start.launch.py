import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sdt_project',
            executable='line_follower.py',
            name='line_follower',
            output='screen'
        ),

        Node(
            package='sdt_project',
            executable='diff_node.py',
            name='diff_node',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='subtry.py',
            name='usb_node',
            output='screen'
        ),

        
    ])