#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sdt_project.msg import MotorValues

class MotorValuesSubscriber(Node):
    def __init__(self):
        super().__init__('motor_values_subscriber')

        # /AGV/motor_values konusundan MotorValues mesajlarını almak için bir subscriber oluşturma
        self.motor_values_sub = self.create_subscription(
            MotorValues,
            '/AGV/motor_values',
            self.motor_values_callback,
            10
        )

    def motor_values_callback(self, msg):
        # MotorValues mesajından verileri okuma ve işleme
        sag_teker_hiz = msg.sag_teker_hiz
        sol_teker_hiz = msg.sol_teker_hiz
        linear_actuator = msg.linear_actuator

        # Verileri loglama
        self.get_logger().info(f'sag_teker_hiz: {sag_teker_hiz}')
        self.get_logger().info(f'sol_teker_hiz: {sol_teker_hiz}')
        self.get_logger().info(f'linear_actuator: {linear_actuator}')

def main(args=None):
    rclpy.init(args=args)
    node = MotorValuesSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()