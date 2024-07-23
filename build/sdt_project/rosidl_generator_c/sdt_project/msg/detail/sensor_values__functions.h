// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__FUNCTIONS_H_
#define SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sdt_project/msg/rosidl_generator_c__visibility_control.h"

#include "sdt_project/msg/detail/sensor_values__struct.h"

/// Initialize msg/SensorValues message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sdt_project__msg__SensorValues
 * )) before or use
 * sdt_project__msg__SensorValues__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__init(sdt_project__msg__SensorValues * msg);

/// Finalize msg/SensorValues message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
void
sdt_project__msg__SensorValues__fini(sdt_project__msg__SensorValues * msg);

/// Create msg/SensorValues message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sdt_project__msg__SensorValues__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
sdt_project__msg__SensorValues *
sdt_project__msg__SensorValues__create();

/// Destroy msg/SensorValues message.
/**
 * It calls
 * sdt_project__msg__SensorValues__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
void
sdt_project__msg__SensorValues__destroy(sdt_project__msg__SensorValues * msg);

/// Check for msg/SensorValues message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__are_equal(const sdt_project__msg__SensorValues * lhs, const sdt_project__msg__SensorValues * rhs);

/// Copy a msg/SensorValues message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__copy(
  const sdt_project__msg__SensorValues * input,
  sdt_project__msg__SensorValues * output);

/// Initialize array of msg/SensorValues messages.
/**
 * It allocates the memory for the number of elements and calls
 * sdt_project__msg__SensorValues__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__Sequence__init(sdt_project__msg__SensorValues__Sequence * array, size_t size);

/// Finalize array of msg/SensorValues messages.
/**
 * It calls
 * sdt_project__msg__SensorValues__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
void
sdt_project__msg__SensorValues__Sequence__fini(sdt_project__msg__SensorValues__Sequence * array);

/// Create array of msg/SensorValues messages.
/**
 * It allocates the memory for the array and calls
 * sdt_project__msg__SensorValues__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
sdt_project__msg__SensorValues__Sequence *
sdt_project__msg__SensorValues__Sequence__create(size_t size);

/// Destroy array of msg/SensorValues messages.
/**
 * It calls
 * sdt_project__msg__SensorValues__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
void
sdt_project__msg__SensorValues__Sequence__destroy(sdt_project__msg__SensorValues__Sequence * array);

/// Check for msg/SensorValues message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__Sequence__are_equal(const sdt_project__msg__SensorValues__Sequence * lhs, const sdt_project__msg__SensorValues__Sequence * rhs);

/// Copy an array of msg/SensorValues messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sdt_project
bool
sdt_project__msg__SensorValues__Sequence__copy(
  const sdt_project__msg__SensorValues__Sequence * input,
  sdt_project__msg__SensorValues__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__FUNCTIONS_H_
