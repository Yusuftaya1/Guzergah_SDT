#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialReader(Node):
    def __init__(self):
        super().__init__('serial_reader')
        self.publisher_ = self.create_publisher(String, 'engel_tespit', 10)
        self.serial_connection = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
        self.timer = self.create_timer(0.1, self.read_serial_data)

    def read_serial_data(self):
        if self.serial_connection.in_waiting > 0:
            try:
                data = self.serial_connection.readline().decode('utf-8').strip()
                msg = String()
                msg.data = data
                self.publisher_.publish(msg)
                self.get_logger().info(f'Published: {msg.data}')
            except Exception as e:
                self.get_logger().error(f'Serial read error: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = SerialReader()
    rclpy.spin(node)
    node.serial_connection.close()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
