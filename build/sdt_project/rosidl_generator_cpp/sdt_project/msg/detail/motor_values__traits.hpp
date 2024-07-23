// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__TRAITS_HPP_
#define SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sdt_project/msg/detail/motor_values__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sdt_project
{

namespace msg
{

inline void to_flow_style_yaml(
  const MotorValues & msg,
  std::ostream & out)
{
  out << "{";
  // member: sag_teker_hiz
  {
    out << "sag_teker_hiz: ";
    rosidl_generator_traits::value_to_yaml(msg.sag_teker_hiz, out);
    out << ", ";
  }

  // member: sol_teker_hiz
  {
    out << "sol_teker_hiz: ";
    rosidl_generator_traits::value_to_yaml(msg.sol_teker_hiz, out);
    out << ", ";
  }

  // member: linear_actuator
  {
    out << "linear_actuator: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_actuator, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MotorValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sag_teker_hiz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sag_teker_hiz: ";
    rosidl_generator_traits::value_to_yaml(msg.sag_teker_hiz, out);
    out << "\n";
  }

  // member: sol_teker_hiz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sol_teker_hiz: ";
    rosidl_generator_traits::value_to_yaml(msg.sol_teker_hiz, out);
    out << "\n";
  }

  // member: linear_actuator
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_actuator: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_actuator, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MotorValues & msg, bool use_flow_style = false)
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
  const sdt_project::msg::MotorValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  sdt_project::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sdt_project::msg::to_yaml() instead")]]
inline std::string to_yaml(const sdt_project::msg::MotorValues & msg)
{
  return sdt_project::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sdt_project::msg::MotorValues>()
{
  return "sdt_project::msg::MotorValues";
}

template<>
inline const char * name<sdt_project::msg::MotorValues>()
{
  return "sdt_project/msg/MotorValues";
}

template<>
struct has_fixed_size<sdt_project::msg::MotorValues>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sdt_project::msg::MotorValues>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sdt_project::msg::MotorValues>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__TRAITS_HPP_
