#!/usr/bin/env python3
"""
USB HABERLEŞME SAĞLANMASI;

TEKER HIZLARI "diff_node" içerisinde hesaplanır ve "motor_values_node"a "motor_values.msg"
MESAJI GÖNDERİLİR "motor_values" dan ALINAN VERİLER SERİ PORTA YAZILIR
"""

import rclpy
import serial 
from rclpy.node import Node
from std_msgs.msg import String

class UISub(Node):
    def __init__(self):
        super().__init__('ui_com_node')
        
        # lift_agirlik konusuna yayıncı tanımlanır
        self.charge_pub = self.create_publisher(String, 'lift_agirlik', 10)
        
        # Seri port açılır
        self.ser = serial.Serial('/dev/ttyTHS0', 115200, timeout=1)
        
        # Zamanlayıcı tanımlanır ve her 0.1 saniyede bir read_serial fonksiyonu çağrılır
        self.timer = self.create_timer(0.1, self.read_serial)

    def read_serial(self):
        """Seri porttan veri okuma ve konusuna yayınlama."""
        if self.ser.in_waiting > 0:
            try:
                # Seri porttan gelen veri okunur ve decode edilir
                usb_data = self.ser.readline().decode('utf-8').strip()
                
                # ROS 2 String mesajı olarak yayınlanır
                msg = String()
                msg.data = usb_data
                self.charge_pub.publish(msg)
                
                self.get_logger().info(f'Seri porttan okunan veri yayınlandı: {usb_data}')

            except Exception as e:
                self.get_logger().error(f'Seri port verisi okunurken hata: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    ui_node = UISub()
    rclpy.spin(ui_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
