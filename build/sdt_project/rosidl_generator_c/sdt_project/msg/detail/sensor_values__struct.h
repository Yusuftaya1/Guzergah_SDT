// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_H_
#define SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/SensorValues in the package sdt_project.
typedef struct sdt_project__msg__SensorValues
{
  double sag_motor_sicaklik;
  double sol_motor_sicaklik;
  double motor_akim;
} sdt_project__msg__SensorValues;

// Struct for a sequence of sdt_project__msg__SensorValues.
typedef struct sdt_project__msg__SensorValues__Sequence
{
  sdt_project__msg__SensorValues * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sdt_project__msg__SensorValues__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_H_
