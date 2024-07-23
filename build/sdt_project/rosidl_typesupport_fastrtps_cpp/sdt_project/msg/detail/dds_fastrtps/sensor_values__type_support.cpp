// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice
#include "sdt_project/msg/detail/sensor_values__rosidl_typesupport_fastrtps_cpp.hpp"
#include "sdt_project/msg/detail/sensor_values__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace sdt_project
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
cdr_serialize(
  const sdt_project::msg::SensorValues & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: sag_motor_sicaklik
  cdr << ros_message.sag_motor_sicaklik;
  // Member: sol_motor_sicaklik
  cdr << ros_message.sol_motor_sicaklik;
  // Member: lift_sicaklik
  cdr << ros_message.lift_sicaklik;
  // Member: sag_motor_akim
  cdr << ros_message.sag_motor_akim;
  // Member: sol_motor_akim
  cdr << ros_message.sol_motor_akim;
  // Member: lift_akim
  cdr << ros_message.lift_akim;
  // Member: asiri_agirlik
  cdr << (ros_message.asiri_agirlik ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sdt_project::msg::SensorValues & ros_message)
{
  // Member: sag_motor_sicaklik
  cdr >> ros_message.sag_motor_sicaklik;

  // Member: sol_motor_sicaklik
  cdr >> ros_message.sol_motor_sicaklik;

  // Member: lift_sicaklik
  cdr >> ros_message.lift_sicaklik;

  // Member: sag_motor_akim
  cdr >> ros_message.sag_motor_akim;

  // Member: sol_motor_akim
  cdr >> ros_message.sol_motor_akim;

  // Member: lift_akim
  cdr >> ros_message.lift_akim;

  // Member: asiri_agirlik
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.asiri_agirlik = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
get_serialized_size(
  const sdt_project::msg::SensorValues & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: sag_motor_sicaklik
  {
    size_t item_size = sizeof(ros_message.sag_motor_sicaklik);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: sol_motor_sicaklik
  {
    size_t item_size = sizeof(ros_message.sol_motor_sicaklik);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lift_sicaklik
  {
    size_t item_size = sizeof(ros_message.lift_sicaklik);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: sag_motor_akim
  {
    size_t item_size = sizeof(ros_message.sag_motor_akim);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: sol_motor_akim
  {
    size_t item_size = sizeof(ros_message.sol_motor_akim);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lift_akim
  {
    size_t item_size = sizeof(ros_message.lift_akim);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: asiri_agirlik
  {
    size_t item_size = sizeof(ros_message.asiri_agirlik);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sdt_project
max_serialized_size_SensorValues(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: sag_motor_sicaklik
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: sol_motor_sicaklik
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: lift_sicaklik
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: sag_motor_akim
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: sol_motor_akim
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: lift_akim
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: asiri_agirlik
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = sdt_project::msg::SensorValues;
    is_plain =
      (
      offsetof(DataType, asiri_agirlik) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _SensorValues__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const sdt_project::msg::SensorValues *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _SensorValues__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<sdt_project::msg::SensorValues *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _SensorValues__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const sdt_project::msg::SensorValues *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _SensorValues__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_SensorValues(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _SensorValues__callbacks = {
  "sdt_project::msg",
  "SensorValues",
  _SensorValues__cdr_serialize,
  _SensorValues__cdr_deserialize,
  _SensorValues__get_serialized_size,
  _SensorValues__max_serialized_size
};

static rosidl_message_type_support_t _SensorValues__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_SensorValues__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sdt_project

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_sdt_project
const rosidl_message_type_support_t *
get_message_type_support_handle<sdt_project::msg::SensorValues>()
{
  return &sdt_project::msg::typesupport_fastrtps_cpp::_SensorValues__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sdt_project, msg, SensorValues)() {
  return &sdt_project::msg::typesupport_fastrtps_cpp::_SensorValues__handle;
}

#ifdef __cplusplus
}
#endif
