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
  "msg/SensorValues.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

###############  NODES  ###############
install(PROGRAMS
  src/usb_com.py
  src/TCP_com.py
  src/diff_node.py
  src/tf_brodcast.py
  src/pid_library.py
  src/manuel_kumanda.py
  src/navigation_1.py
  src/qr_detect.py
  src/map.py
  DESTINATION lib/${PROJECT_NAME}
)

###############  LAUNCH  ###############
install(FILES
  launch/mission1.launch.py
  launch/mission2.launch.py
  launch/SLAM.launch.py 
  DESTINATION share/${PROJECT_NAME}/launch
)


ament_package()
