#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class SerialReader(Node):
    def __init__(self):
        super().__init__('serial_reader')
        self.publisher_ = self.create_publisher(Bool, 'engel_tespit', 10)
        self.serial_connection = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
        self.timer = self.create_timer(0.1, self.read_serial_data)

    def read_serial_data(self):
        data = self.serial_connection.readline().decode('utf-8').strip()
        msg = Bool()
        if data == "1":
            self.get_logger().info(f'trueeee')
            msg.data = True
        else:
            self.get_logger().info(f'falseeee')
            msg.data = False
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SerialReader()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
