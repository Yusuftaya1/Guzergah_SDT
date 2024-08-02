#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bu ROS 2 düğümü, QR kodu ve açı bilgilerine göre motor 
değerlerini ayarlayarak farklı görevleri yerine getirir.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String
from sdt_project.msg import MotorValues
import numpy as np
import time

class TaskManager:
    def __init__(self, motor_controller):
        self.motor_controller = motor_controller
    
    def perform_load_action(self, actuator_value):
        self.motor_controller.set_motor_values(0.0, 0.0, actuator_value)
        action = 'Yük alımı için' if actuator_value == 750.0 else 'Yük bırakmak için'
        self.motor_controller.get_logger().info(f'{action} duruyor...')
        time.sleep(10)
        self.motor_controller.qr_id = None

    def perform_turn(self, direction):
        if direction == "right":
            self.motor_controller.set_motor_values(150.0, 400.0)
            self.motor_controller.get_logger().info('Sağa dönüş...')
        elif direction == "left":
            self.motor_controller.set_motor_values(400.0, 150.0)
            self.motor_controller.get_logger().info('Sola dönüş...')
        time.sleep(2)
        self.motor_controller.qr_id = None

    def run_forward(self):
        self.motor_controller.set_motor_values(400.0, 400.0)
        time.sleep(2)
    
    def engelden_kacma(self):
        self.motor_controller.set_motor_values(0.0, 400.0)
        time.sleep(1.5)
        self.motor_controller.set_motor_values(400.0, 400.0)
        time.sleep(1.5)
        self.motor_controller.set_motor_values(0.0, 400.0)
        time.sleep(1.5)
        self.motor_controller.set_motor_values(400.0, 400.0)
        time.sleep(1.5)

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.wheel_distance = 0.35
        self.wheel_radius = 0.1
        self.coef = 0.02
        self.qr_id = None
        self.task_manager = TaskManager(self)
        self.angle_sub = self.create_subscription(Float64, '/AGV/angle', self.angle_callback, 10)
        self.qr_status_sub = self.create_subscription(String, '/qr_code_data', self.qr_callback, 10)
        self.motor_values_pub = self.create_publisher(MotorValues, '/AGV/motor_values', 10)
        #self.engel_sub = self.create_subscription(String, 'engel_tespit', self.engel_callback, 10)
        self.motor_values_msg = MotorValues()
    
    def qr_callback(self, msg):
        self.qr_id = msg.data
        self.get_logger().info(f'QR ID: {self.qr_id}')

    def angle_callback(self, msg):
        angle = msg.data
        linear = 0.1
        w = angle * (1.0 - self.coef)
        
        if self.qr_id == "1":
            self.task_manager.perform_load_action(750.0)
            self.get_logger().info('Yük alındı , devam ediliyor...')
            self.task_manager.run_forward()

        elif self.qr_id == "2":
            self.task_manager.perform_load_action(250.0)
            self.get_logger().info('Yük bırakıldı , devam ediliyor...')
            self.task_manager.run_forward()

        elif self.qr_id == "3":
            self.task_manager.perform_turn("right")

        elif self.qr_id == "4":
            self.task_manager.perform_turn("left")

        else:
            if w != 0.0:
                right_speed = linear + (w * (self.wheel_distance / 2.0))
                left_speed = linear - (w * (self.wheel_distance / 2.0))
            else:
                right_speed = linear
                left_speed = linear

            right_speed_angular = right_speed / (2 * np.pi * self.wheel_radius)
            left_speed_angular = left_speed / (2 * np.pi * self.wheel_radius)
            
            self.set_motor_values(
                np.clip(2000 * right_speed_angular, -1000, 1000),
                np.clip(2000 * left_speed_angular, -1000, 1000)
            )
    """
    def engel_callback(self, msg):
        self.engel = msg.data
        if self.engel == "1" and not self.engel_detected:
            self.engel_check_timer = self.create_timer(1.0, self.check_engel_status)
            self.engel_timer_count = 0
            self.get_logger().info('Engel tespit edildi, bekleniyor...')
            self.set_motor_values(0.0, 0.0)

    def check_engel_status(self):
        if self.engel_detected:
            if self.engel == "0":
                self.get_logger().info('Engel ortadan kalktı, devam ediliyor...')
                self.task_manager.run_forward()
                self.engel_detected = False
            else:
                self.engel_timer_count += 1
                if self.engel_timer_count >= 7:
                    self.get_logger().info('Engel 7 saniye boyunca ortadan kalkmadı, engelden kaçılıyor...')
                    self.task_manager.engelden_kacma()
                    self.engel_detected = False
    """
    
    def set_motor_values(self, right_speed, left_speed, actuator_value=None):
        self.motor_values_msg.sag_teker_hiz = right_speed
        self.motor_values_msg.sol_teker_hiz = left_speed
        if actuator_value is not None:
            self.motor_values_msg.linear_actuator = actuator_value
        self.publish_motor_values()

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
