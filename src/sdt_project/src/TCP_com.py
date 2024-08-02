#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
import json
import socket
from rclpy.node import Node
from sdt_project.msg import SensorValues 
from std_msgs.msg import String

class TCP_Socket():
    def __init__(self):
        self.target_host = "10.7.91.190"
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
                response = self.client.recv(4096)
                print("\nRESPONSE:" + response.decode('utf-8') + "\n")
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
        self.subscription = self.create_subscription(SensorValues, '/AGV/sensor_values', self.sensor_callback, 10)
        self.engel_status = self.create_subscription(String, 'engel_tespit', self.engel_callback, 10)
        self.qr_status =    self.create_subscription(String,'/qr_code_data',self.qr_callback, 10)
        self.sensor_data =  None
        self.engel_statu =  None
        self.qr_statu = None
        self.timer = self.create_timer(1.0, self.merge_and_send)

    def sensor_callback(self, msg):
        self.sensor_data = msg

    def engel_callback(self, msg):
        self.engel_statu = msg

    def qr_callback(self,msg):
        self.qr_statu = msg

    def merge_and_send(self):
        if self.sensor_data and self.engel_statu:
            msg_dict = {
                "sag_motor_sicaklik": self.sensor_data.sag_motor_sicaklik,
                "sol_motor_sicaklik": self.sensor_data.sol_motor_sicaklik,
                "lift_sicaklik":      self.sensor_data.lift_sicaklik,
                "sag_motor_akim":     self.sensor_data.sag_motor_akim,
                "sol_motor_akim":     self.sensor_data.sol_motor_akim,
                "lift_akim":          self.sensor_data.lift_akim,
                "asiri_agirlik":      self.sensor_data.asiri_agirlik,
                "engel":              self.engel_statu.data,
                "map":                None,
                "QR":                 self.qr_statu
            }
            
            self.socket.send_data(msg_dict)

def main(args=None):
    rclpy.init(args=args)
    UI_node = UI_sub()
    rclpy.spin(UI_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
