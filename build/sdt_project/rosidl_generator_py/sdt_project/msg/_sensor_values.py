# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sdt_project:msg/SensorValues.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SensorValues(type):
    """Metaclass of message 'SensorValues'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('sdt_project')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'sdt_project.msg.SensorValues')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__sensor_values
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__sensor_values
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__sensor_values
            cls._TYPE_SUPPORT = module.type_support_msg__msg__sensor_values
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__sensor_values

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SensorValues(metaclass=Metaclass_SensorValues):
    """Message class 'SensorValues'."""

    __slots__ = [
        '_sag_motor_sicaklik',
        '_sol_motor_sicaklik',
        '_lift_sicaklik',
        '_sag_motor_akim',
        '_sol_motor_akim',
        '_lift_akim',
        '_asiri_agirlik',
    ]

    _fields_and_field_types = {
        'sag_motor_sicaklik': 'double',
        'sol_motor_sicaklik': 'double',
        'lift_sicaklik': 'double',
        'sag_motor_akim': 'double',
        'sol_motor_akim': 'double',
        'lift_akim': 'double',
        'asiri_agirlik': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.sag_motor_sicaklik = kwargs.get('sag_motor_sicaklik', float())
        self.sol_motor_sicaklik = kwargs.get('sol_motor_sicaklik', float())
        self.lift_sicaklik = kwargs.get('lift_sicaklik', float())
        self.sag_motor_akim = kwargs.get('sag_motor_akim', float())
        self.sol_motor_akim = kwargs.get('sol_motor_akim', float())
        self.lift_akim = kwargs.get('lift_akim', float())
        self.asiri_agirlik = kwargs.get('asiri_agirlik', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.sag_motor_sicaklik != other.sag_motor_sicaklik:
            return False
        if self.sol_motor_sicaklik != other.sol_motor_sicaklik:
            return False
        if self.lift_sicaklik != other.lift_sicaklik:
            return False
        if self.sag_motor_akim != other.sag_motor_akim:
            return False
        if self.sol_motor_akim != other.sol_motor_akim:
            return False
        if self.lift_akim != other.lift_akim:
            return False
        if self.asiri_agirlik != other.asiri_agirlik:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def sag_motor_sicaklik(self):
        """Message field 'sag_motor_sicaklik'."""
        return self._sag_motor_sicaklik

    @sag_motor_sicaklik.setter
    def sag_motor_sicaklik(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sag_motor_sicaklik' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sag_motor_sicaklik' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sag_motor_sicaklik = value

    @builtins.property
    def sol_motor_sicaklik(self):
        """Message field 'sol_motor_sicaklik'."""
        return self._sol_motor_sicaklik

    @sol_motor_sicaklik.setter
    def sol_motor_sicaklik(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sol_motor_sicaklik' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sol_motor_sicaklik' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sol_motor_sicaklik = value

    @builtins.property
    def lift_sicaklik(self):
        """Message field 'lift_sicaklik'."""
        return self._lift_sicaklik

    @lift_sicaklik.setter
    def lift_sicaklik(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lift_sicaklik' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'lift_sicaklik' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._lift_sicaklik = value

    @builtins.property
    def sag_motor_akim(self):
        """Message field 'sag_motor_akim'."""
        return self._sag_motor_akim

    @sag_motor_akim.setter
    def sag_motor_akim(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sag_motor_akim' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sag_motor_akim' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sag_motor_akim = value

    @builtins.property
    def sol_motor_akim(self):
        """Message field 'sol_motor_akim'."""
        return self._sol_motor_akim

    @sol_motor_akim.setter
    def sol_motor_akim(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sol_motor_akim' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sol_motor_akim' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sol_motor_akim = value

    @builtins.property
    def lift_akim(self):
        """Message field 'lift_akim'."""
        return self._lift_akim

    @lift_akim.setter
    def lift_akim(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lift_akim' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'lift_akim' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._lift_akim = value

    @builtins.property
    def asiri_agirlik(self):
        """Message field 'asiri_agirlik'."""
        return self._asiri_agirlik

    @asiri_agirlik.setter
    def asiri_agirlik(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'asiri_agirlik' field must be of type 'bool'"
        self._asiri_agirlik = value
