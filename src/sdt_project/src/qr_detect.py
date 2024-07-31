#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2

class QRCodeDetector(Node):
    def __init__(self):
        super().__init__('qr_code_detector')
        self.qr_pub = self.create_publisher(String, '/qr_code_data', 10)
        self.create_subscription(Image, '/image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.detector = cv2.QRCodeDetector()

    def image_callback(self, msg):
        try:
            # ROS mesajını OpenCV formatına çevir
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        except Exception as e:
            self.get_logger().error(f"Image conversion error: {e}")
            return

        # QR kodunu tespit et ve decode et
        data, bbox, _ = self.detector.detectAndDecode(cv_image)
        qr_msg = String()

        if data:
            self.get_logger().info(f"QR kod okundu: {data}")
            qr_msg.data = data
        else:
            qr_msg.data = "0"
            self.get_logger().info(f"QR kod yok: {qr_msg.data}")

        self.qr_pub.publish(qr_msg)

        # Görüntüyü göstermek için (isteğe bağlı)
        #cv2.imshow("QRCodeScanner", cv_image)
        #cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    qr_code_detector = QRCodeDetector()
    try:
        rclpy.spin(qr_code_detector)
    except KeyboardInterrupt:
        pass
    finally:
        qr_code_detector.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
