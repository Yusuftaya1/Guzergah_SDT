// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice
#include "sdt_project/msg/detail/motor_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sdt_project__msg__MotorValues__init(sdt_project__msg__MotorValues * msg)
{
  if (!msg) {
    return false;
  }
  // sag_teker_hiz
  // sol_teker_hiz
  // linear_actuator
  return true;
}

void
sdt_project__msg__MotorValues__fini(sdt_project__msg__MotorValues * msg)
{
  if (!msg) {
    return;
  }
  // sag_teker_hiz
  // sol_teker_hiz
  // linear_actuator
}

bool
sdt_project__msg__MotorValues__are_equal(const sdt_project__msg__MotorValues * lhs, const sdt_project__msg__MotorValues * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sag_teker_hiz
  if (lhs->sag_teker_hiz != rhs->sag_teker_hiz) {
    return false;
  }
  // sol_teker_hiz
  if (lhs->sol_teker_hiz != rhs->sol_teker_hiz) {
    return false;
  }
  // linear_actuator
  if (lhs->linear_actuator != rhs->linear_actuator) {
    return false;
  }
  return true;
}

bool
sdt_project__msg__MotorValues__copy(
  const sdt_project__msg__MotorValues * input,
  sdt_project__msg__MotorValues * output)
{
  if (!input || !output) {
    return false;
  }
  // sag_teker_hiz
  output->sag_teker_hiz = input->sag_teker_hiz;
  // sol_teker_hiz
  output->sol_teker_hiz = input->sol_teker_hiz;
  // linear_actuator
  output->linear_actuator = input->linear_actuator;
  return true;
}

sdt_project__msg__MotorValues *
sdt_project__msg__MotorValues__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__MotorValues * msg = (sdt_project__msg__MotorValues *)allocator.allocate(sizeof(sdt_project__msg__MotorValues), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sdt_project__msg__MotorValues));
  bool success = sdt_project__msg__MotorValues__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sdt_project__msg__MotorValues__destroy(sdt_project__msg__MotorValues * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sdt_project__msg__MotorValues__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sdt_project__msg__MotorValues__Sequence__init(sdt_project__msg__MotorValues__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__MotorValues * data = NULL;

  if (size) {
    data = (sdt_project__msg__MotorValues *)allocator.zero_allocate(size, sizeof(sdt_project__msg__MotorValues), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sdt_project__msg__MotorValues__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sdt_project__msg__MotorValues__fini(&data[i - 1]);
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
sdt_project__msg__MotorValues__Sequence__fini(sdt_project__msg__MotorValues__Sequence * array)
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
      sdt_project__msg__MotorValues__fini(&array->data[i]);
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

sdt_project__msg__MotorValues__Sequence *
sdt_project__msg__MotorValues__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sdt_project__msg__MotorValues__Sequence * array = (sdt_project__msg__MotorValues__Sequence *)allocator.allocate(sizeof(sdt_project__msg__MotorValues__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sdt_project__msg__MotorValues__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sdt_project__msg__MotorValues__Sequence__destroy(sdt_project__msg__MotorValues__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sdt_project__msg__MotorValues__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sdt_project__msg__MotorValues__Sequence__are_equal(const sdt_project__msg__MotorValues__Sequence * lhs, const sdt_project__msg__MotorValues__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sdt_project__msg__MotorValues__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sdt_project__msg__MotorValues__Sequence__copy(
  const sdt_project__msg__MotorValues__Sequence * input,
  sdt_project__msg__MotorValues__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sdt_project__msg__MotorValues);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sdt_project__msg__MotorValues * data =
      (sdt_project__msg__MotorValues *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sdt_project__msg__MotorValues__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sdt_project__msg__MotorValues__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sdt_project__msg__MotorValues__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
