import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='camera',
            output='screen'
        ),
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='lidar',
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
            executable='qr_detect.py',
            name='qr_detectt',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='TCP_com.py',
            name='usb_node',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='navigation4.py',
            name='usb_node',
            output='screen'
        )
        
    ])