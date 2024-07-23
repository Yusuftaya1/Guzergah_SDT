import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sdt_project',
            executable='usb_com.py',
            name='usb_com_node',
            output='screen'
        ),
        
        Node(
            package='sdt_project',
            executable='UI-com.py',
            name='UI_com_node',
            output='screen'
        ),
    ])