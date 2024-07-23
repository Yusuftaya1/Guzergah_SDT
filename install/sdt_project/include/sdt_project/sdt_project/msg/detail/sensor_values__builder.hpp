// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__BUILDER_HPP_
#define SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sdt_project/msg/detail/sensor_values__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sdt_project
{

namespace msg
{

namespace builder
{

class Init_SensorValues_asiri_agirlik
{
public:
  explicit Init_SensorValues_asiri_agirlik(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  ::sdt_project::msg::SensorValues asiri_agirlik(::sdt_project::msg::SensorValues::_asiri_agirlik_type arg)
  {
    msg_.asiri_agirlik = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_lift_akim
{
public:
  explicit Init_SensorValues_lift_akim(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  Init_SensorValues_asiri_agirlik lift_akim(::sdt_project::msg::SensorValues::_lift_akim_type arg)
  {
    msg_.lift_akim = std::move(arg);
    return Init_SensorValues_asiri_agirlik(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_sol_motor_akim
{
public:
  explicit Init_SensorValues_sol_motor_akim(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  Init_SensorValues_lift_akim sol_motor_akim(::sdt_project::msg::SensorValues::_sol_motor_akim_type arg)
  {
    msg_.sol_motor_akim = std::move(arg);
    return Init_SensorValues_lift_akim(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_sag_motor_akim
{
public:
  explicit Init_SensorValues_sag_motor_akim(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  Init_SensorValues_sol_motor_akim sag_motor_akim(::sdt_project::msg::SensorValues::_sag_motor_akim_type arg)
  {
    msg_.sag_motor_akim = std::move(arg);
    return Init_SensorValues_sol_motor_akim(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_lift_sicaklik
{
public:
  explicit Init_SensorValues_lift_sicaklik(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  Init_SensorValues_sag_motor_akim lift_sicaklik(::sdt_project::msg::SensorValues::_lift_sicaklik_type arg)
  {
    msg_.lift_sicaklik = std::move(arg);
    return Init_SensorValues_sag_motor_akim(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_sol_motor_sicaklik
{
public:
  explicit Init_SensorValues_sol_motor_sicaklik(::sdt_project::msg::SensorValues & msg)
  : msg_(msg)
  {}
  Init_SensorValues_lift_sicaklik sol_motor_sicaklik(::sdt_project::msg::SensorValues::_sol_motor_sicaklik_type arg)
  {
    msg_.sol_motor_sicaklik = std::move(arg);
    return Init_SensorValues_lift_sicaklik(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

class Init_SensorValues_sag_motor_sicaklik
{
public:
  Init_SensorValues_sag_motor_sicaklik()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorValues_sol_motor_sicaklik sag_motor_sicaklik(::sdt_project::msg::SensorValues::_sag_motor_sicaklik_type arg)
  {
    msg_.sag_motor_sicaklik = std::move(arg);
    return Init_SensorValues_sol_motor_sicaklik(msg_);
  }

private:
  ::sdt_project::msg::SensorValues msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sdt_project::msg::SensorValues>()
{
  return sdt_project::msg::builder::Init_SensorValues_sag_motor_sicaklik();
}

}  // namespace sdt_project

#endif  // SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__BUILDER_HPP_
