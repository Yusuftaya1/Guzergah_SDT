import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='lidar',
            output='screen'
        ),  
        Node(
            package='slam_gmapping',
            executable='slam_gmapping',
            name='mapping',
            output='screen'
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
            name='pid_controller',
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
            name='tcp_node',
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_base_to_laser',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_odom_to_base',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
        ),
    ])
