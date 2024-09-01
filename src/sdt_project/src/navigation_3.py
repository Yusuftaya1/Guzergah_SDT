#!/usr/bin/env python3
"""
DOLU SENARYO 1

QR BİLGİLERİ KULLANILARAK ARACIN DÖNÜŞ YAPMASI SAĞLANIR

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
        self.target_point = "D"
        self.mode_msg = "Start"
    
    def qr_callback(self,msg):
        self.qr_id = msg.data

        if self.target_point == "A":
            if self.qr_id in ["Q43", "Q18"]:
                self.mode_msg = "Turn Left"
            elif self.qr_id == "Q50":
                self.mode_msg = "Load"
                self.target_point = "C"
            else:
                self.mode_msg = "None"

        elif self.target_point == "B":
            if self.qr_id in ["Q31", "Q9"]:
                self.mode_msg = "Turn Right"
            elif self.qr_id == "Q45":
                self.mode_msg = "Unload"
                self.target_point = "A"
            else:
                self.mode_msg = "None"

        elif self.target_point == "C":
            if self.qr_id in ["Q48", "Q5"]:
                self.mode_msg = "Turn Left"
            elif self.qr_id == "Q38":
                self.mode_msg = "Unload"
                self.target_point = "S2"
            else:
                self.mode_msg = "None"

        elif self.target_point == "D":
            if self.qr_id in ["Q42", "Q26"]:
                self.mode_msg = "Turn Right"
            elif self.qr_id == "Q33":
                self.mode_msg = "Load"
                self.target_point = "B"
            else:
                self.mode_msg = "None"

        elif self.target_point == "S2":
            if self.qr_id in ["Q36", "Q23"]:
                self.mode_msg = "Turn Left" 
            elif self.qr_id == "Q7":
                self.mode_msg = "Finish"
            else:
                self.mode_msg = "None"

        if self.mode_msg:
            self.publish_mode_status()
            self.get_logger().info(f'QR ID: {self.qr_id}')
            self.get_logger().info(f'TARGET: {self.target_point}')
            self.get_logger().info(f'MODE: {self.mode_msg}')

    def publish_mode_status(self):
        msg = String()
        msg.data = self.mode_msg
        self.mode_status_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Navigation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
