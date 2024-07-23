import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sdt_project',
            executable='line_follower.py',
            name='line_follower ',
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
            executable='usb_com.py',
            name='usb_com_node',
            output='screen'
        ),
        
        Node(
            package='sdt_project',
            executable='TCP_Com.py',
            name='UI_com_node',
            output='screen'
        ),
    ])