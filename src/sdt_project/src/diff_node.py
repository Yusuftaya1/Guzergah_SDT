#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bu ROS 2 düğümü, QR kodu ve açı bilgilerine göre motor değerlerini ayarlayarak
farklı görevleri yerine getirir.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String
from sdt_project.msg import MotorValues
import numpy as np
import time

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.wheel_distance = 0.35
        self.wheel_radius = 0.1
        self.coef = 0.02
        self.qr_id = None 
        self.angle_sub = self.create_subscription(Float64, '/AGV/angle', self.angle_callback, 10)
        self.qr_status_sub = self.create_subscription(String, '/qr_code_data', self.qr_callback, 10)
        self.motor_values_pub = self.create_publisher(MotorValues, '/AGV/motor_values', 10)
        self.motor_values_msg = MotorValues()
        self.stop_duration = 10
        self.forward_duration = 2
        self.turn_duration = 3

    def qr_callback(self, msg):
        self.qr_id = msg.data
        self.get_logger().info(f'QR ID: {self.qr_id}')

    def angle_callback(self, msg):
        angle = msg.data
        linear = 0.1
        w = angle * (1.0 - self.coef)
        
        if self.qr_id == "1":
            self.perform_load_action(750.0)
            self.get_logger().info('Yük alındı, 2 saniye boyunca ilerliyor...')
            self.run_forward()

        elif self.qr_id == "2":
            self.perform_load_action(250.0)
            self.get_logger().info('Yük bırakıldı, 2 saniye boyunca ilerliyor...')
            self.run_forward()

        elif self.qr_id == "3":
            self.perform_turn("right")

        elif self.qr_id == "4":
            self.perform_turn("left")

        else:
            # PID kontrol ve motor hızlarını hesapla
            if w != 0.0:
                right_speed = linear + (w * (self.wheel_distance / 2.0))
                left_speed = linear - (w * (self.wheel_distance / 2.0))
            else:
                right_speed = linear
                left_speed = linear

            right_speed_angular = right_speed / (2 * np.pi * self.wheel_radius)
            left_speed_angular = left_speed / (2 * np.pi * self.wheel_radius)
            
            self.motor_values_msg.sag_teker_hiz = np.clip(2000 * right_speed_angular, -1000, 1000)
            self.motor_values_msg.sol_teker_hiz = np.clip(2000 * left_speed_angular, -1000, 1000)

        self.publish_motor_values()

    def perform_load_action(self, actuator_value):
        self.motor_values_msg.sag_teker_hiz = 0.0
        self.motor_values_msg.sol_teker_hiz = 0.0
        self.motor_values_msg.linear_actuator = actuator_value
        action = 'Yük alımı için' if actuator_value == 750.0 else 'Yük bırakmak için'
        self.get_logger().info(f'{action} duruyor...')
        self.publish_motor_values()
        time.sleep(self.stop_duration)
        self.qr_id = None

    def perform_turn(self, direction):
        if direction == "right":
            self.motor_values_msg.sag_teker_hiz = 150.0
            self.motor_values_msg.sol_teker_hiz = 400.0
            self.get_logger().info('Sağa dönüş...')
        elif direction == "left":
            self.motor_values_msg.sag_teker_hiz = 400.0
            self.motor_values_msg.sol_teker_hiz = 150.0
            self.get_logger().info('Sola dönüş...')
        
        time.sleep(self.turn_duration)
        self.qr_id = None

    def run_forward(self):
        self.motor_values_msg.sag_teker_hiz = 400.0
        self.motor_values_msg.sol_teker_hiz = 400.0
        self.publish_motor_values()
        time.sleep(self.forward_duration)

    def publish_motor_values(self):
        self.get_logger().info(f'Sol teker hız: {self.motor_values_msg.sol_teker_hiz}')
        self.get_logger().info(f'Sağ teker hız: {self.motor_values_msg.sag_teker_hiz}')
        self.get_logger().info(f'Linear aktüatör: {self.motor_values_msg.linear_actuator}')
        self.motor_values_pub.publish(self.motor_values_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
