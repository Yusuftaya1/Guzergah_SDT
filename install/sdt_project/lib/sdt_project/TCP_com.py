#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
import json
import socket
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String, Bool
from nav_msgs.msg import OccupancyGrid

class TCP_Socket:
    def __init__(self):
        self.target_host = "10.7.91.224"
        self.target_port = 2626
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.settimeout(1.0)
        self.connected = False
        self.received_msg = None

    def connect(self):
        try:
            self.client.connect((self.target_host, self.target_port))
            self.connected = True
        except ConnectionRefusedError:
            print("Bağlantı hatası: Sunucuya bağlanılamadı.")
        except Exception as e:
            print(f"Bağlantı hatası: {e}")

    def data_transfer(self, msg):
        if not self.connected:
            self.connect()
        
        if self.connected:
            self.client.send(msg)
            #response = self.client.recv(4096).decode('utf-8')
            #self.received_msg = response

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
        self.engel_status = self.create_subscription(Bool, 'engel_tespit', self.engel_callback, 10)
        self.map_sub = self.create_subscription(OccupancyGrid, 'map', self.map_callback, 10)
        self.charge_pub = self.create_publisher(String, 'charge_status', 10)
        self.sag_motor_sicaklik = 0.0
        self.sol_motor_sicaklik = 0.0
        self.motor_akim = 0.0
        self.engel_statu = False
        self.map = None
        self.timer = self.create_timer(3.0, self.process_data)

    def engel_callback(self, msg):
        self.engel_statu = msg.data

    def map_callback(self, msg):
        grid_data   = np.array(msg.data, dtype=np.int8)        
        width       = msg.info.width
        height      = msg.info.height
        grid_data   = grid_data.reshape((height, width))
        self.map    = self.get_middle_section(grid_data, 100).astype(int).tolist()

    def get_middle_section(self,matrix, section_size):
        """
        Bu fonksiyon, bir matrisin ortasında verilen boyutta bir bölüm döner.
        
        :param matrix: Girdi matrisi
        :param section_size: Ortadan alınacak bölümün boyutu (tek sayı olmalı)
        :return: Matrisin ortasından alınan bölüm
        """
        rows, cols = matrix.shape
        half_section = section_size // 2
        
        center_row, center_col = rows // 2, cols // 2
        start_row = max(center_row - half_section, 0)
        end_row = min(center_row + half_section + 1, rows)
        start_col = max(center_col - half_section, 0)
        end_col = min(center_col + half_section + 1, cols)
        return matrix[start_row:end_row, start_col:end_col]

    def process_data(self):
        msg_dict = {    
            "sag_motor_sicaklik": self.sag_motor_sicaklik,
            "sol_motor_sicaklik": self.sol_motor_sicaklik,
            "motor_akim": self.motor_akim,
            "engel": self.engel_statu,
            "map": self.map
        }
        
        self.socket.send_data(msg_dict)
        #received_msg = self.socket.get_received_msg()

        #if received_msg == "Charge":
        #    charge_msg = String()
        #    charge_msg.data = "Charge"
        #    self.charge_pub.publish(charge_msg)

def main(args=None):
    rclpy.init(args=args)
    UI_node = UI_sub()
    rclpy.spin(UI_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()