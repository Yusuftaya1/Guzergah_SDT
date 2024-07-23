// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_H_
#define SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MotorValues in the package sdt_project.
typedef struct sdt_project__msg__MotorValues
{
  uint16_t sag_teker_hiz;
  uint16_t sol_teker_hiz;
  bool linear_actuator;
} sdt_project__msg__MotorValues;

// Struct for a sequence of sdt_project__msg__MotorValues.
typedef struct sdt_project__msg__MotorValues__Sequence
{
  sdt_project__msg__MotorValues * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sdt_project__msg__MotorValues__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_H_
