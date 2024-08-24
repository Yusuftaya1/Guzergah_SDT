#!/usr/bin/env python3
"""
DOLU SENARYO 1

QR BİLGİLERİ KULLANILARAK ARACIN DÜZ GİTMESİ YA DA DÖNÜŞ YAPMASI SAĞLANIR

'/qr_code_data' KULLANILARAK ARACIN GİTMESİ GEREKEN YÖN BELİRLENİR VE BUNA GÖRE 
GEKERLİ KOMUT '/mode_status' a GÖNDERİLİR 

AYRICA "qr_status" KULLANILARAK LİFTİN ÇALIŞMASI DA '/mode_status' ÜZERİNDEN
KONTROL EDİLİR

"/cmd_vel" de KULLANILABİLİR
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Navigation(Node):
    def __init__(self):
        super().__init__('Navigation')
        self.qr_status_sub = self.create_subscription(String, '/qr_code_data', self.qr_callback, 10)
        self.mode_status_pub = self.create_publisher(String, '/mode_status', 10)
        self.target_point = "A"
        self.mode_msg = None

    def qr_callback(self, msg):
        qr_data = msg.data
        self.get_logger().info(f'QR ID: {qr_data}')
        self.qr_id = self.extract_first_part(qr_data)

        if self.qr_id == "Q33":
            self.mode_msg = "Load"
            self.target_point = "B"

        elif self.qr_id == "Q50":
            self.mode_msg = "Load"
            self.target_point = "C"

        elif self.qr_id == "Q38":
            self.mode_msg = "Unload"
            self.target_point = "D"

        elif self.qr_id == "Q45":
            self.mode_msg = "Unload"
            self.target_point = "S1"
        
        if self.target_point == "A":
            if self.qr_id in ["Q11", "Q41"]:
                self.mode_msg = "Turn Right"

        elif self.target_point == "B":
            if self.qr_id in ["Q35", "Q18"]:
                self.mode_msg = "Turn Left"

        elif self.target_point == "C":
            if self.qr_id in ["Q52", "Q24"]:
                self.mode_msg = "Turn Right"

        elif self.target_point == "D":
            if self.qr_id in ["Q40", "Q3"]:
                self.mode_msg = "Turn Left"

        elif self.target_point == "S1":
            if self.qr_id in ["Q47", "Q8"]:
                self.mode_msg = "Turn Left" 
            elif self.qr_id == "Q22":
                self.mode_msg = "Finish"

        if self.mode_msg:
            self.publish_mode_status()

    def extract_first_part(self, qr_data):
        parts = qr_data.split(';')
        if parts:
            return parts[0]
        return None

    def publish_mode_status(self):
        msg = String()
        msg.data = self.mode_msg
        self.mode_status_pub.publish(msg)
        self.get_logger().info(f'Published mode status: {self.mode_msg}')

def main(args=None):
    rclpy.init(args=args)
    node = Navigation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
