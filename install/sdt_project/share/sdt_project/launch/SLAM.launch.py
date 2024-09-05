import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    slam_gmapping_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('slam_gmapping'), 
                'launch', 
                'slam_gmapping.launch.py'
            )
        )
    )

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
        sllidar_launch,
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
        slam_gmapping_launch,

    ])
