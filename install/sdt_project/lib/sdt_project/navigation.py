#!/usr/bin/env python3
"""
QR BİLGİLERİ KULLANILARAK ARACIN DÜZ GİTMESİ YA DA DÖNÜŞ YAPMASI SAĞLANIR

"qr_status" KULLANILARAK ARACIN GİTMESİ GEREKEN YÖN BELİRLENİR VE BUNA GÖRE MOTOR
HIZLARI "/AGV/motor_values_node" a GÖNDERİLİR 

AYRICA "qr_status" KULLANILARAK LİFTİN ÇALIŞMASI DA "/AGV/motor_values_node" ÜZERİNDEN
KONTROL EDİLİR

"/cmd_vel" de KULLANILABİLİR

  ---mode_status --- mode_status node--- 
motor_values NEREDEN ALINACAK ONU BELİRLER

1 == line_follow
2 == turn
3 == escape_block
mode_status node

"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String, Bool

class Navigation:
    def __init__(self):
        super().__init__('Navigation')
        self.qr_status_sub = self.create_subscription(String, '/qr_code_data', self.qr_callback, 10)
        


    def qr_callback(self, msg):
        self.qr_id = msg.data
        self.get_logger().info(f'QR ID: {self.qr_id}')


def main(args=None):
    rclpy.init(args=args)
    node = Navigation()
    rclpy.spin(node)
    rclpy.shutdown()
