#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Updated code for detecting QR codes and displaying their data.
"""
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class QRCodeDetector(Node):
    def __init__(self):
        super().__init__('qr_code_detector')
        self.image_sub = self.create_subscription(Image, 'image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.qr_detector = cv2.QRCodeDetector()

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.process_image(frame)
        except Exception as e:
            self.get_logger().error(f'CvBridge Error: {e}')

    def process_image(self, frame):
        frame = cv2.resize(frame, (320, 240))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 3)
        
        self.detect_qr_code(binary)
        
        cv2.imshow("Filtrelenmis Goruntu", binary)
        cv2.waitKey(1)

    def detect_qr_code(self, binary_image):
        data, bbox, _ = self.qr_detector.detectAndDecode(binary_image)
        if data:
            d = data
        else:
            d= "Q0"
        self.get_logger().info(f"QR Kod Verisi: {d}")
def main(args=None):
    rclpy.init(args=args)
    qr_code_detector = QRCodeDetector()

    try:
        while rclpy.ok():
            rclpy.spin_once(qr_code_detector)
    except KeyboardInterrupt:
        print("Çıkış yapılıyor...")
    finally:
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
