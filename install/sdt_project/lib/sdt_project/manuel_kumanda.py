#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class DifferentialDriveController(Node):
    def __init__(self):
        super().__init__('differential_drive_controller')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.wheel_separation = 0.5
        self.wheel_radius     = 0.1
        self.subscription     = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10)

    def cmd_vel_callback(self, msg):
        linear_velocity  = msg.linear.x
        angular_velocity = msg.angular.z
        linear_actuator  = 0
        right_wheel_velocity = (linear_velocity)+ (angular_velocity * self.wheel_separation / 2)
        left_wheel_velocity  = (linear_velocity)- (angular_velocity * self.wheel_separation / 2)
        self.send_wheel_velocities(right_wheel_velocity, left_wheel_velocity,linear_actuator)

    def send_wheel_velocities(self, right_wheel_velocity, left_wheel_velocity,linear_actuator):
        right_wheel_velocity = max(min(right_wheel_velocity, 600), -600)
        left_wheel_velocity = max(min(left_wheel_velocity, 600), -600)
        linear_actuator = max(min(linear_actuator, 600), -600)

        right_wheel_velocity_str = f'{int(right_wheel_velocity):05}'
        left_wheel_velocity_str = f'{int(left_wheel_velocity):05}'
        llinear_actuator_str = f'{int(linear_actuator):05}'

        command = f'{right_wheel_velocity_str},{left_wheel_velocity_str},{llinear_actuator_str}\n'
        self.get_logger().info(f'Seri porta gönderilen veri:{right_wheel_velocity_str},{left_wheel_velocity_str},{llinear_actuator_str}\n')
        self.serial_port.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    differential_drive_controller = DifferentialDriveController()
    rclpy.spin(differential_drive_controller)
    differential_drive_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()