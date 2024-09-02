#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
import json
import socket
from rclpy.node import Node
from sdt_project.msg import SensorValues
from std_msgs.msg import String,Bool
from nav_msgs.msg import OccupancyGrid

class TCP_Socket():
    def __init__(self):
        self.target_host = "10.7.91.176"
        self.target_port = 2626
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(1.0)
        self.connected = False
        self.received_msg = None

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
                try:
                    response = self.client.recv(4096).decode('utf-8')
                    self.received_msg = response
                    print("\nRESPONSE:" + response + "\n")
                except socket.timeout:
                    self.received_msg = None
                
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

    def get_received_msg(self):
        return self.received_msg

class UI_sub(Node):
    def __init__(self):
        super().__init__('UI_com_node')
        self.socket = TCP_Socket()
        self.socket.connect()
        self.subscription = self.create_subscription(SensorValues, '/AGV/sensor_values', self.sensor_callback, 10)
        self.engel_status = self.create_subscription(Bool, 'engel_tespit', self.engel_callback, 10)
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 10)
        self.charge_pub = self.create_publisher(String, 'charge_status', 10)
        self.timer = self.create_timer(1.0, self.merge_and_send)

    def sensor_callback(self, msg):
        self.sag_motor_sicaklik = msg.sag_motor_sicaklik
        self.sol_motor_sicaklik = msg.sol_motor_sicaklik
        self.motor_akim = msg.motor_akim

    def engel_callback(self, msg):
        self.engel_statu = msg.data

    def map_callback(self, msg):
        self.map = msg.data

    def merge_and_send(self):
        msg_dict = {
            "sag_motor_sicaklik": self.sag_motor_sicaklik,
            "sol_motor_sicaklik": self.sol_motor_sicaklik,

            "motor_akim":         self.motor_akim,
            
            "engel":              self.engel_statu,
            "map":                self.map
        }
        
        self.socket.send_data(msg_dict)
        received_msg = self.socket.get_received_msg()

        if received_msg == "Charge":
            charge_msg = String()
            charge_msg.data = "Charge"
            self.charge_pub.publish(charge_msg)

def main(args=None):
    rclpy.init(args=args)
    UI_node = UI_sub()
    rclpy.spin(UI_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
