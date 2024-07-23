// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "sdt_project/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "sdt_project/msg/detail/motor_values__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace sdt_project
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
cdr_serialize(
  const sdt_project::msg::MotorValues & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sdt_project::msg::MotorValues & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
get_serialized_size(
  const sdt_project::msg::MotorValues & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
max_serialized_size_MotorValues(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sdt_project

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sdt_project, msg, MotorValues)();

#ifdef __cplusplus
}
#endif

#endif  // SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
