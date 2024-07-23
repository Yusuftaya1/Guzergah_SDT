// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "sdt_project/msg/detail/motor_values__struct.h"
#include "sdt_project/msg/detail/motor_values__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool sdt_project__msg__motor_values__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[42];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("sdt_project.msg._motor_values.MotorValues", full_classname_dest, 41) == 0);
  }
  sdt_project__msg__MotorValues * ros_message = _ros_message;
  {  // sag_teker_hiz
    PyObject * field = PyObject_GetAttrString(_pymsg, "sag_teker_hiz");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sag_teker_hiz = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // sol_teker_hiz
    PyObject * field = PyObject_GetAttrString(_pymsg, "sol_teker_hiz");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sol_teker_hiz = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // linear_actuator
    PyObject * field = PyObject_GetAttrString(_pymsg, "linear_actuator");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->linear_actuator = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sdt_project__msg__motor_values__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MotorValues */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sdt_project.msg._motor_values");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MotorValues");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sdt_project__msg__MotorValues * ros_message = (sdt_project__msg__MotorValues *)raw_ros_message;
  {  // sag_teker_hiz
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->sag_teker_hiz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sag_teker_hiz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sol_teker_hiz
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->sol_teker_hiz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sol_teker_hiz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // linear_actuator
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->linear_actuator ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "linear_actuator", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
