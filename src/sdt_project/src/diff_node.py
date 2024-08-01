#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
mode_status YA DA action_status MSG KULLANILARAK MOTOR VALUES DEĞERİ 
QR BİLGİSİNE GÖRE , ÇİZGİYE GÖRE YA DA ESCAPE BLOCK OLARAK GÖNDERİLECEK
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String
from sdt_project.msg import MotorValues
import numpy as np

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.wheel_distance = 0.35
        self.wheel_radius = 0.1
        self.coef = 0.02
        self.qr_id = None 
        self.angle_sub = self.create_subscription(Float64,'/AGV/angle',self.angle_callback,10)
        self.qr_status_sub = self.create_subscription( String, '/qr_code_data',self.qr_callback,10)
        self.motor_values_pub = self.create_publisher(MotorValues, '/AGV/motor_values', 10)
        self.motor_values_msg = MotorValues()

    def qr_callback(self, msg):
        self.qr_id = msg.data
        self.get_logger().info(f'QR ID : {self.qr_id}')

    def angle_callback(self, msg):
        self.get_logger().info(f'aaaaaa')
        angle = msg.data
        linear = 0.1
        w = angle * (1.0 - self.coef)
        
        if self.qr_id == "1":
            self.motor_values_msg.sag_teker_hiz = 0.0
            self.motor_values_msg.sol_teker_hiz = 0.0
            self.motor_values_msg.linear_actuator = 750.0

            
        elif self.qr_id == "2":
            self.motor_values_msg.sag_teker_hiz = 0.0
            self.motor_values_msg.sol_teker_hiz = 0.0
            self.motor_values_msg.linear_actuator = 200.0     

        else:
            if w != 0.0:
                hiz_sag = linear + (w * (self.wheel_distance / 2.0))
                hiz_sol = linear - (w * (self.wheel_distance / 2.0))
            else:
                hiz_sag = linear
                hiz_sol = linear

            hiz_sag_angular = hiz_sag / (2 * 3.14159265 * self.wheel_radius)
            hiz_sol_angular = hiz_sol / (2 * 3.14159265 * self.wheel_radius)
            
            self.motor_values_msg.sag_teker_hiz = np.clip(2000 * hiz_sag_angular, -1000, 1000)
            self.motor_values_msg.sol_teker_hiz = np.clip(2000 * hiz_sol_angular, -1000, 1000)

        self.get_logger().info(f'sol_teker_hiz: {self.motor_values_msg.sol_teker_hiz}')
        self.get_logger().info(f'sag_teker_hiz: {self.motor_values_msg.sag_teker_hiz}')
        self.get_logger().info(f'linear_actuator: { self.motor_values_msg.linear_actuator}')

        self.motor_values_pub.publish(self.motor_values_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
