// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__BUILDER_HPP_
#define SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sdt_project/msg/detail/motor_values__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sdt_project
{

namespace msg
{

namespace builder
{

class Init_MotorValues_linear_actuator
{
public:
  explicit Init_MotorValues_linear_actuator(::sdt_project::msg::MotorValues & msg)
  : msg_(msg)
  {}
  ::sdt_project::msg::MotorValues linear_actuator(::sdt_project::msg::MotorValues::_linear_actuator_type arg)
  {
    msg_.linear_actuator = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sdt_project::msg::MotorValues msg_;
};

class Init_MotorValues_sol_teker_hiz
{
public:
  explicit Init_MotorValues_sol_teker_hiz(::sdt_project::msg::MotorValues & msg)
  : msg_(msg)
  {}
  Init_MotorValues_linear_actuator sol_teker_hiz(::sdt_project::msg::MotorValues::_sol_teker_hiz_type arg)
  {
    msg_.sol_teker_hiz = std::move(arg);
    return Init_MotorValues_linear_actuator(msg_);
  }

private:
  ::sdt_project::msg::MotorValues msg_;
};

class Init_MotorValues_sag_teker_hiz
{
public:
  Init_MotorValues_sag_teker_hiz()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorValues_sol_teker_hiz sag_teker_hiz(::sdt_project::msg::MotorValues::_sag_teker_hiz_type arg)
  {
    msg_.sag_teker_hiz = std::move(arg);
    return Init_MotorValues_sol_teker_hiz(msg_);
  }

private:
  ::sdt_project::msg::MotorValues msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sdt_project::msg::MotorValues>()
{
  return sdt_project::msg::builder::Init_MotorValues_sag_teker_hiz();
}

}  // namespace sdt_project

#endif  // SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__BUILDER_HPP_
