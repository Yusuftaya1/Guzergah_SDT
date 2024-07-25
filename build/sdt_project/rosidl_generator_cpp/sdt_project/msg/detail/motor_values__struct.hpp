// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sdt_project:msg/MotorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_HPP_
#define SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sdt_project__msg__MotorValues __attribute__((deprecated))
#else
# define DEPRECATED__sdt_project__msg__MotorValues __declspec(deprecated)
#endif

namespace sdt_project
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MotorValues_
{
  using Type = MotorValues_<ContainerAllocator>;

  explicit MotorValues_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sag_teker_hiz = 0.0;
      this->sol_teker_hiz = 0.0;
      this->linear_actuator = 0.0;
    }
  }

  explicit MotorValues_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sag_teker_hiz = 0.0;
      this->sol_teker_hiz = 0.0;
      this->linear_actuator = 0.0;
    }
  }

  // field types and members
  using _sag_teker_hiz_type =
    double;
  _sag_teker_hiz_type sag_teker_hiz;
  using _sol_teker_hiz_type =
    double;
  _sol_teker_hiz_type sol_teker_hiz;
  using _linear_actuator_type =
    double;
  _linear_actuator_type linear_actuator;

  // setters for named parameter idiom
  Type & set__sag_teker_hiz(
    const double & _arg)
  {
    this->sag_teker_hiz = _arg;
    return *this;
  }
  Type & set__sol_teker_hiz(
    const double & _arg)
  {
    this->sol_teker_hiz = _arg;
    return *this;
  }
  Type & set__linear_actuator(
    const double & _arg)
  {
    this->linear_actuator = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sdt_project::msg::MotorValues_<ContainerAllocator> *;
  using ConstRawPtr =
    const sdt_project::msg::MotorValues_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sdt_project::msg::MotorValues_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sdt_project::msg::MotorValues_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sdt_project::msg::MotorValues_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sdt_project::msg::MotorValues_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sdt_project::msg::MotorValues_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sdt_project::msg::MotorValues_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sdt_project::msg::MotorValues_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sdt_project::msg::MotorValues_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sdt_project__msg__MotorValues
    std::shared_ptr<sdt_project::msg::MotorValues_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sdt_project__msg__MotorValues
    std::shared_ptr<sdt_project::msg::MotorValues_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorValues_ & other) const
  {
    if (this->sag_teker_hiz != other.sag_teker_hiz) {
      return false;
    }
    if (this->sol_teker_hiz != other.sol_teker_hiz) {
      return false;
    }
    if (this->linear_actuator != other.linear_actuator) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorValues_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorValues_

// alias to use template instance with default allocator
using MotorValues =
  sdt_project::msg::MotorValues_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sdt_project

#endif  // SDT_PROJECT__MSG__DETAIL__MOTOR_VALUES__STRUCT_HPP_
