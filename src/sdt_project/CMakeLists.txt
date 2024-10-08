cmake_minimum_required(VERSION 3.8)
project(sdt_project)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)


set(msg_files
  "msg/MotorValues.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

###############  NODES  ###############
install(PROGRAMS
  src/deneme_pid2.py
  src/usb_com.py
  src/TCP_com.py
  src/diff_node.py
  src/line_follow_main.py
  src/manuel_kumanda.py
  src/navigation_1.py
  src/navigation_2.py
  src/navigation_3.py
  src/navigation_4.py
  src/qr_detect.py
  src/tcp_usb.py
  src/pid_line_follower.py
  src/qr_mask.py
  src/usb2_sensor.py
  DESTINATION lib/${PROJECT_NAME}
)

###############  LAUNCH  ###############
install(FILES
  launch/SLAM.launch.py 
  launch/mission1.launch.py
  launch/mission2.launch.py
  launch/mission3.launch.py
  launch/mission4.launch.py
  launch/cartographer.launch.py
  launch/occupancy_grid.launch.py
  DESTINATION share/${PROJECT_NAME}/launch
)


ament_package()
