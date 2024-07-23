#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
USER INTERFACE COMMUNİCATİON
SEND SENSOR VALUES TO UI

"SensorValues.msg" read from '/AGV/sensor_values' SEND TO HUB

"""
import rclpy
import socket
from rclpy.node import Node
from sdt_project.msg import SensorValues

class SensorValuesSubscriber(Node):
    def __init__(self):
        self.host = "192.168.1.100"
        self.port = 5000
        self.sock = None
        self.connect()
        super().__init__('sensor_values_subscirber')
        self.SensorValues = self.create_subscription(
            SensorValues,
            '/AGV/sensor_values',
            self.sensor_values_callback,
            10
        )

    def connect(self):
        if self.sock is not None:
            self.disconnect()
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            print(f"Bağlantı kuruldu: {self.host}:{self.port}")
        except socket.error as e:
            raise RuntimeError(f"Bağlantı kurulurken hata oluştu: {e}")
        
    def disconnect(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None
            print(f"Bağlantı kapatıldı: {self.host}:{self.port}")

    def sensor_values_callback(self, msg):
        sending_data = self.sensor_values_to_string(msg)
        self.send_to_hub(sending_data)

    def sensor_values_to_string(self, msg):
        data = (
            f'{msg.sag_motor_sicaklik},{msg.sol_motor_sicaklik},{msg.lift_sicaklik},'
            f'{msg.sag_motor_akim},{msg.sol_motor_akim},{msg.lift_akim},{msg.asiri_agirlik}'
        )
        return data

    def send_to_hub(self,data):
        try:
            self.sock.sendall(data.encode())
            print(f"Yazıldı: {data}")
        except socket.error as e:
            raise RuntimeError(f"Veri gönderilirken hata oluştu: {e}")


if __name__ == "__main__":
    rclpy.init(args=None)
    sensor_values_publisher = SensorValuesSubscriber()
    rclpy.spin(sensor_values_publisher)
    sensor_values_publisher.destroy_node()
    rclpy.shutdown()

