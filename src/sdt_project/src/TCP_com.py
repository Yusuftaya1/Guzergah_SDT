#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
USER INTERFACE COMMUNİCATİON
SEND SENSOR VALUES TO UI

"SensorValues.msg" read from '/AGV/sensor_values' SEND TO HUB

"""
import rclpy
from rclpy.node import Node
from sdt_project.msg import SensorValues
import socket
import json

class TCP_Socket:
    def __init__(self):
        self.target_host = "192.168.72.214"
        self.target_port = 8910
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        try:
            self.client.connect((self.target_host, self.target_port))
            self.connected = True
        except ConnectionRefusedError:
            print("Bağlantı hatası: Sunucuya bağlanılamadı.")

    def data_transfer(self, msg):
        if not self.connected:
            self.connect()

        if self.connected:
            try:
                self.client.send(msg.encode('utf-8'))  # Encode the message to bytes
                response = self.client.recv(4096)
                print("\nRESPONSE:" + response.decode() + "\n")
            except ConnectionError:
                print("Bağlantı hatası: Veri gönderilirken bir hata oluştu.")

    def close(self):
        if self.connected:
            self.client.close()
            self.connected = False

class UI_subscriber(Node):
    def __init__(self):
        super().__init__('ui_subscriber')
        self.socket = TCP_Socket()
        self.create_subscription(
            SensorValues,
            '/AGV/sensor_values',
            self.sensor_values_callback,
            10
        )

    def sensor_values_callback(self, msg):
        msg_dict = {
            "sag_motor_sicaklik": msg.sag_motor_sicaklik,
            "sol_motor_sicaklik": msg.sol_motor_sicaklik,
            "lift_sicaklik":      msg.lift_sicaklik,
            "sag_motor_akim":     msg.sag_motor_akim,
            "sol_motor_akim":     msg.sol_motor_akim,
            "lift_akim":          msg.lift_akim,
            "asiri_agirlik":      msg.asiri_agirlik
        }
        msg_json = json.dumps(msg_dict)
        self.socket.data_transfer(msg_json.encode())

def main(args=None):
    rclpy.init(args=args)
    node = UI_subscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.socket.close()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
