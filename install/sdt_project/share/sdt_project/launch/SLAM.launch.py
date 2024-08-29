import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
         Node(
            package='slam_toolbox', 
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False
            }],
            remappings=[
                ('/scan', '/my_scan_topic'), 
                ('/map', '/my_map_topic'),
            ]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='camera',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='pid_library.py',
            name='camera',
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
            name='usb_node',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='TCP_com.py',
            name='usb_node',
            output='screen'
        ),
    ])