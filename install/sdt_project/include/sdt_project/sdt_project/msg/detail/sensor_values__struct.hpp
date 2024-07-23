// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sdt_project:msg/SensorValues.idl
// generated code does not contain a copyright notice

#ifndef SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_HPP_
#define SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sdt_project__msg__SensorValues __attribute__((deprecated))
#else
# define DEPRECATED__sdt_project__msg__SensorValues __declspec(deprecated)
#endif

namespace sdt_project
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SensorValues_
{
  using Type = SensorValues_<ContainerAllocator>;

  explicit SensorValues_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sag_motor_sicaklik = 0.0;
      this->sol_motor_sicaklik = 0.0;
      this->lift_sicaklik = 0.0;
      this->sag_motor_akim = 0.0;
      this->sol_motor_akim = 0.0;
      this->lift_akim = 0.0;
      this->asiri_agirlik = false;
    }
  }

  explicit SensorValues_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sag_motor_sicaklik = 0.0;
      this->sol_motor_sicaklik = 0.0;
      this->lift_sicaklik = 0.0;
      this->sag_motor_akim = 0.0;
      this->sol_motor_akim = 0.0;
      this->lift_akim = 0.0;
      this->asiri_agirlik = false;
    }
  }

  // field types and members
  using _sag_motor_sicaklik_type =
    double;
  _sag_motor_sicaklik_type sag_motor_sicaklik;
  using _sol_motor_sicaklik_type =
    double;
  _sol_motor_sicaklik_type sol_motor_sicaklik;
  using _lift_sicaklik_type =
    double;
  _lift_sicaklik_type lift_sicaklik;
  using _sag_motor_akim_type =
    double;
  _sag_motor_akim_type sag_motor_akim;
  using _sol_motor_akim_type =
    double;
  _sol_motor_akim_type sol_motor_akim;
  using _lift_akim_type =
    double;
  _lift_akim_type lift_akim;
  using _asiri_agirlik_type =
    bool;
  _asiri_agirlik_type asiri_agirlik;

  // setters for named parameter idiom
  Type & set__sag_motor_sicaklik(
    const double & _arg)
  {
    this->sag_motor_sicaklik = _arg;
    return *this;
  }
  Type & set__sol_motor_sicaklik(
    const double & _arg)
  {
    this->sol_motor_sicaklik = _arg;
    return *this;
  }
  Type & set__lift_sicaklik(
    const double & _arg)
  {
    this->lift_sicaklik = _arg;
    return *this;
  }
  Type & set__sag_motor_akim(
    const double & _arg)
  {
    this->sag_motor_akim = _arg;
    return *this;
  }
  Type & set__sol_motor_akim(
    const double & _arg)
  {
    this->sol_motor_akim = _arg;
    return *this;
  }
  Type & set__lift_akim(
    const double & _arg)
  {
    this->lift_akim = _arg;
    return *this;
  }
  Type & set__asiri_agirlik(
    const bool & _arg)
  {
    this->asiri_agirlik = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sdt_project::msg::SensorValues_<ContainerAllocator> *;
  using ConstRawPtr =
    const sdt_project::msg::SensorValues_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sdt_project::msg::SensorValues_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sdt_project::msg::SensorValues_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sdt_project::msg::SensorValues_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sdt_project::msg::SensorValues_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sdt_project::msg::SensorValues_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sdt_project::msg::SensorValues_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sdt_project::msg::SensorValues_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sdt_project::msg::SensorValues_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sdt_project__msg__SensorValues
    std::shared_ptr<sdt_project::msg::SensorValues_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sdt_project__msg__SensorValues
    std::shared_ptr<sdt_project::msg::SensorValues_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SensorValues_ & other) const
  {
    if (this->sag_motor_sicaklik != other.sag_motor_sicaklik) {
      return false;
    }
    if (this->sol_motor_sicaklik != other.sol_motor_sicaklik) {
      return false;
    }
    if (this->lift_sicaklik != other.lift_sicaklik) {
      return false;
    }
    if (this->sag_motor_akim != other.sag_motor_akim) {
      return false;
    }
    if (this->sol_motor_akim != other.sol_motor_akim) {
      return false;
    }
    if (this->lift_akim != other.lift_akim) {
      return false;
    }
    if (this->asiri_agirlik != other.asiri_agirlik) {
      return false;
    }
    return true;
  }
  bool operator!=(const SensorValues_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SensorValues_

// alias to use template instance with default allocator
using SensorValues =
  sdt_project::msg::SensorValues_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sdt_project

#endif  // SDT_PROJECT__MSG__DETAIL__SENSOR_VALUES__STRUCT_HPP_
