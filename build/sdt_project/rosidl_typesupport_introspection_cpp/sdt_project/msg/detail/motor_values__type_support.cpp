// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sdt_project/msg/detail/motor_values__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sdt_project
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void MotorValues_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sdt_project::msg::MotorValues(_init);
}

void MotorValues_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sdt_project::msg::MotorValues *>(message_memory);
  typed_message->~MotorValues();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember MotorValues_message_member_array[3] = {
  {
    "sag_teker_hiz",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project::msg::MotorValues, sag_teker_hiz),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sol_teker_hiz",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project::msg::MotorValues, sol_teker_hiz),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "linear_actuator",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project::msg::MotorValues, linear_actuator),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers MotorValues_message_members = {
  "sdt_project::msg",  // message namespace
  "MotorValues",  // message name
  3,  // number of fields
  sizeof(sdt_project::msg::MotorValues),
  MotorValues_message_member_array,  // message members
  MotorValues_init_function,  // function to initialize message memory (memory has to be allocated)
  MotorValues_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t MotorValues_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &MotorValues_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace sdt_project


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sdt_project::msg::MotorValues>()
{
  return &::sdt_project::msg::rosidl_typesupport_introspection_cpp::MotorValues_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sdt_project, msg, MotorValues)() {
  return &::sdt_project::msg::rosidl_typesupport_introspection_cpp::MotorValues_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
