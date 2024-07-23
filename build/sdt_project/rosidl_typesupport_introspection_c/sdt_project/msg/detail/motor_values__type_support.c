// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sdt_project/msg/detail/motor_values__rosidl_typesupport_introspection_c.h"
#include "sdt_project/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sdt_project/msg/detail/motor_values__functions.h"
#include "sdt_project/msg/detail/motor_values__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sdt_project__msg__MotorValues__init(message_memory);
}

void sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_fini_function(void * message_memory)
{
  sdt_project__msg__MotorValues__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_member_array[3] = {
  {
    "sag_teker_hiz",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project__msg__MotorValues, sag_teker_hiz),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sol_teker_hiz",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project__msg__MotorValues, sol_teker_hiz),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "linear_actuator",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sdt_project__msg__MotorValues, linear_actuator),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_members = {
  "sdt_project__msg",  // message namespace
  "MotorValues",  // message name
  3,  // number of fields
  sizeof(sdt_project__msg__MotorValues),
  sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_member_array,  // message members
  sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_init_function,  // function to initialize message memory (memory has to be allocated)
  sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_type_support_handle = {
  0,
  &sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sdt_project
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sdt_project, msg, MotorValues)() {
  if (!sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_type_support_handle.typesupport_identifier) {
    sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sdt_project__msg__MotorValues__rosidl_typesupport_introspection_c__MotorValues_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
