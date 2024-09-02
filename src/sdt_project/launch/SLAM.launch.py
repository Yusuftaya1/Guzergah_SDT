import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Include the launch file for SLAM GMapping
    slam_gmapping_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('slam_gmapping'), 
                'launch', 
                'slam_gmapping.launch.py'
            )
        )
    )

    # Include the launch file for SLLidar
    sllidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('sllidar_ros2'),
                'launch',
                'sllidar_s1_launch.py'  # Launch file for SLLidar
            )
        )
    )

    return LaunchDescription([
        # Include SLLidar launch
        sllidar_launch,

        # Static transform from base_link to laser
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_base_to_laser',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser']
        ),
        
        # Static transform from odom to base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_odom_to_base',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
        ),
        slam_gmapping_launch,

        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='camera',
            output='screen'
        ),

        Node(
            package='sdt_project',
            executable='diff_node.py',
            name='diff_drive_node',
            output='screen'
        ),

        Node(
            package='sdt_project',
            executable='usb_com.py',
            name='usb_communication_node',
            output='screen'
        ),
        Node(
            package='sdt_project',
            executable='TCP_com.py',
            name='tcp_communication_node',
            output='screen'
        ),
    ])
