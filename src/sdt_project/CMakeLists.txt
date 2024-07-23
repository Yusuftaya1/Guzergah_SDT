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

install(PROGRAMS
  src/usb_com.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  src/manuel_kumanda.py
  DESTINATION lib/${PROJECT_NAME}
)

install(FILES
  launch/node_start.launch.py
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
