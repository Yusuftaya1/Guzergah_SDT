#!/usr/bin/env python3
"""
DOLU SENARYO 2
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Navigation(Node):
    def __init__(self):
        super().__init__('Navigation')
        self.qr_status_sub = self.create_subscription(String, '/qr_code_data', self.qr_callback, 10)
        self.mode_status_pub = self.create_publisher(String, '/mode_status', 10)
        self.target_point = "B"
        self.mode_msg = None

    def qr_callback(self, msg):
        qr_data = msg.data
        self.get_logger().info(f'QR ID: {qr_data}')
        self.qr_id = self.extract_first_part(qr_data)  
        
        if self.target_point == "A":
            if self.qr_id in ["Q36", "Q18"]:
                self.mode_msg = "Turn Left"
            elif self.qr_id == "Q50":
                self.mode_msg = "Unload"
                self.target_point = "S1"
            else:
                self.mode_msg = "None"

        elif self.target_point == "B":
            if self.qr_id in ["Q41", "Q9"]:
                self.mode_msg = "Turn Right"
            elif self.qr_id == "Q45":
                self.mode_msg = "Load"
                self.target_point = "D"
            else:
                self.mode_msg = "None"

        elif self.target_point == "C":
            if self.qr_id in ["Q31", "Q4"]:
                self.mode_msg = "Turn Right"
            elif self.qr_id == "Q38":
                self.mode_msg = "Load"
                self.target_point = "A"
            else:
                self.mode_msg = "None"

        elif self.target_point == "D":
            if self.qr_id in ["Q43", "Q26"]:
                self.mode_msg = "Turn Right"
            elif self.qr_id == "Q33":
                self.mode_msg = "Unload"
                self.target_point = "C"
            else:
                self.mode_msg = "None"

        elif self.target_point == "S1":
            if self.qr_id in ["Q48", "Q8"]:
                self.mode_msg = "Turn Left" 
            elif self.qr_id == "Q22":
                self.mode_msg = "Finish"
            else:
                self.mode_msg = "None"

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
