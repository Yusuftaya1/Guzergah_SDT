// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice
#include "sdt_project/msg/detail/sensor_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sdt_project__msg__SensorValues__init(sdt_project__msg__SensorValues * msg)
{
  if (!msg) {
    return false;
  }
  // sag_motor_sicaklik
  // sol_motor_sicaklik
  // motor_akim
  return true;
}

void
sdt_project__msg__SensorValues__fini(sdt_project__msg__SensorValues * msg)
{
  if (!msg) {
    return;
  }
  // sag_motor_sicaklik
  // sol_motor_sicaklik
  // motor_akim
}

bool
sdt_project__msg__SensorValues__are_equal(const sdt_project__msg__SensorValues * lhs, const sdt_project__msg__SensorValues * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sag_motor_sicaklik
  if (lhs->sag_motor_sicaklik != rhs->sag_motor_sicaklik) {
    return false;
  }
  // sol_motor_sicaklik
  if (lhs->sol_motor_sicaklik != rhs->sol_motor_sicaklik) {
    return false;
  }
  // motor_akim
  if (lhs->motor_akim != rhs->motor_akim) {
    return false;
  }
  return true;
}

bool
sdt_project__msg__SensorValues__copy(
  const sdt_project__msg__SensorValues * input,
  sdt_project__msg__SensorValues * output)
{
  if (!input || !output) {
    return false;
  }
  // sag_motor_sicaklik
  output->sag_motor_sicaklik = input->sag_motor_sicaklik;
  // sol_motor_sicaklik
  output->sol_motor_sicaklik = input->sol_motor_sicaklik;
  // motor_akim
  output->motor_akim = input->motor_akim;
  return true;
}

sdt_project__msg__SensorValues *
sdt_project__msg__SensorValues__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__SensorValues * msg = (sdt_project__msg__SensorValues *)allocator.allocate(sizeof(sdt_project__msg__SensorValues), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sdt_project__msg__SensorValues));
  bool success = sdt_project__msg__SensorValues__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sdt_project__msg__SensorValues__destroy(sdt_project__msg__SensorValues * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sdt_project__msg__SensorValues__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sdt_project__msg__SensorValues__Sequence__init(sdt_project__msg__SensorValues__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__SensorValues * data = NULL;

  if (size) {
    data = (sdt_project__msg__SensorValues *)allocator.zero_allocate(size, sizeof(sdt_project__msg__SensorValues), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sdt_project__msg__SensorValues__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sdt_project__msg__SensorValues__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sdt_project__msg__SensorValues__Sequence__fini(sdt_project__msg__SensorValues__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sdt_project__msg__SensorValues__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sdt_project__msg__SensorValues__Sequence *
sdt_project__msg__SensorValues__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__SensorValues__Sequence * array = (sdt_project__msg__SensorValues__Sequence *)allocator.allocate(sizeof(sdt_project__msg__SensorValues__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sdt_project__msg__SensorValues__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sdt_project__msg__SensorValues__Sequence__destroy(sdt_project__msg__SensorValues__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sdt_project__msg__SensorValues__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sdt_project__msg__SensorValues__Sequence__are_equal(const sdt_project__msg__SensorValues__Sequence * lhs, const sdt_project__msg__SensorValues__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sdt_project__msg__SensorValues__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sdt_project__msg__SensorValues__Sequence__copy(
  const sdt_project__msg__SensorValues__Sequence * input,
  sdt_project__msg__SensorValues__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sdt_project__msg__SensorValues);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sdt_project__msg__SensorValues * data =
      (sdt_project__msg__SensorValues *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sdt_project__msg__SensorValues__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sdt_project__msg__SensorValues__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sdt_project__msg__SensorValues__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
