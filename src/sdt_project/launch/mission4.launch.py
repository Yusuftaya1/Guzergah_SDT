import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    sllidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('sllidar_ros2'),
                'launch',
                'sllidar_s1_launch.py'
            )
        )
    )
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='camera',
            output='screen'
        ),
        sllidar_launch,
        Node(
            package='sdt_project',
            executable='line_follow_main.py',
            name='line',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='diff_node.py',
            name='diff_node',
            output='screen'
        ),
        Node(
            package='zbar_ros',
            executable='barcode_reader',
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
        ),
        Node(
            package='sdt_project',
            executable='usb_com.py',
            name='usb',  # It's better to use a unique name to avoid conflicts
            output='screen'
        ),
    ])
