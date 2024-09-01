// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__TRAITS_HPP_
#define SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sdt_project/msg/detail/sensor_values__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sdt_project
{

namespace msg
{

inline void to_flow_style_yaml(
  const SensorValues & msg,
  std::ostream & out)
{
  out << "{";
  // member: sag_motor_sicaklik
  {
    out << "sag_motor_sicaklik: ";
    rosidl_generator_traits::value_to_yaml(msg.sag_motor_sicaklik, out);
    out << ", ";
  }

  // member: sol_motor_sicaklik
  {
    out << "sol_motor_sicaklik: ";
    rosidl_generator_traits::value_to_yaml(msg.sol_motor_sicaklik, out);
    out << ", ";
  }

  // member: motor_akim
  {
    out << "motor_akim: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_akim, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SensorValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sag_motor_sicaklik
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sag_motor_sicaklik: ";
    rosidl_generator_traits::value_to_yaml(msg.sag_motor_sicaklik, out);
    out << "\n";
  }

  // member: sol_motor_sicaklik
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sol_motor_sicaklik: ";
    rosidl_generator_traits::value_to_yaml(msg.sol_motor_sicaklik, out);
    out << "\n";
  }

  // member: motor_akim
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor_akim: ";
    rosidl_generator_traits::value_to_yaml(msg.motor_akim, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SensorValues & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace sdt_project

namespace rosidl_generator_traits
{

[[deprecated("use sdt_project::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sdt_project::msg::SensorValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  sdt_project::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sdt_project::msg::to_yaml() instead")]]
inline std::string to_yaml(const sdt_project::msg::SensorValues & msg)
{
  return sdt_project::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sdt_project::msg::SensorValues>()
{
  return "sdt_project::msg::SensorValues";
}

template<>
inline const char * name<sdt_project::msg::SensorValues>()
{
  return "sdt_project/msg/SensorValues";
}

template<>
struct has_fixed_size<sdt_project::msg::SensorValues>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sdt_project::msg::SensorValues>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sdt_project::msg::SensorValues>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__TRAITS_HPP_
