#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
import json
import socket
from rclpy.node import Node
from sdt_project.msg import SensorValues 
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid

class TCP_Socket():
    def __init__(self):
        self.target_host = "10.7.91.176"
        self.target_port = 2626
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
                self.client.send(msg)
            except ConnectionError:
                print("Bağlantı hatası: Veri gönderilirken bir hata oluştu.")

    def close(self):
        if self.connected:
            self.client.close()
            self.connected = False

    def send_data(self, send_to_ui):
        msg_json = json.dumps(send_to_ui)
        self.data_transfer(msg_json.encode('utf-8'))
        print(f"Sent sensor data: {send_to_ui}")

class UI_sub(Node):
    def __init__(self):
        super().__init__('UI_com_node')
        self.socket = TCP_Socket()
        self.socket.connect()
        self.subscription = self.create_subscription(SensorValues, '/AGV/sensor_values', self.sensor_callback, 10)
        self.engel_status = self.create_subscription(String, 'engel_tespit', self.engel_callback, 10)
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 10)
        self.sensor_data = None
        self.timer = self.create_timer(1.0, self.merge_and_send)

    def sensor_callback(self, msg):
        self.sag_motor_sicaklik = msg.sag_motor_sicaklik
        self.sol_motor_sicaklik = msg.sol_motor_sicaklik
        self.lift_sicaklik = msg.lift_sicaklik
    
        self.sag_motor_akim = msg.sag_motor_akim
        self.sol_motor_akim = msg.sol_motor_akim
        self.lift_akim = msg.lift_akim

        self.asiri_agirlik = msg.asiri_agirlik

    def engel_callback(self, msg):
        self.engel_statu = msg.data

    def map_callback(self, msg):
        self.map = msg.data

    def merge_and_send(self):
        msg_dict = {
            "sag_motor_sicaklik": self.sag_motor_sicaklik,
            "sol_motor_sicaklik": self.sol_motor_sicaklik,
            "lift_sicaklik":      self.lift_sicaklik,

            "sag_motor_akim":     self.sag_motor_akim,
            "sol_motor_akim":     self.sol_motor_akim,
            "lift_akim":          self.lift_akim,

            "asiri_agirlik":      self.asiri_agirlik,
            "engel":              self.engel_statu,
            "map":                self.map
        }
        
        self.socket.send_data(msg_dict)

def main(args=None):
    rclpy.init(args=args)
    UI_node = UI_sub()
    rclpy.spin(UI_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
