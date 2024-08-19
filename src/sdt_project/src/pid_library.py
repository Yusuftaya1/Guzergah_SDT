#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kod denenecek PID Library
"""
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_pid import PID

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.angle_pub = self.create_publisher(Float64, '/AGV/angle', 10)
        self.image_sub = self.create_subscription(Image, 'image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.binary_image = None
        self.pid = PID(6.0, 0.1, 0.15, setpoint=160)
        self.base_speed = 300
        self.max_speed = 1000

    def publish_angle(self, angle):
        msg = Float64()
        msg.data = angle
        self.angle_pub.publish(msg)
        self.get_logger().info(f'Published angle: {angle:.2f}')

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.process_image(frame)
        except CvBridgeError as e:
            self.get_logger().error(f'CvBridge Error: {e}')

    def process_image(self, frame):
        frame = cv2.resize(frame, (320, 240))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        threshold = 60
        _, binary = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV)

        M = cv2.moments(binary)
        if M['m00'] != 0:
            cX = int(M['m10'] / M['m00'])
        else:
            cX = frame.shape[1] // 2

        control_signal = self.pid(cX)
        control_signal_normalized = np.clip(control_signal, -self.max_speed, self.max_speed) / self.max_speed
        edge_threshold = 50
        edges = cv2.Canny(blurred, edge_threshold, edge_threshold * 2)
        edge_moments = cv2.moments(edges)
        
        if edge_moments['m00'] != 0:
            edge_cX = int(edge_moments['m10'] / edge_moments['m00'])
            if abs(edge_cX - cX) > 50:
                control_signal_normalized *= 1.5
                control_signal_normalized = np.clip(control_signal_normalized, -1, 1)

        print(f"PID Kontrol Sinyali (Normalleştirilmiş): {control_signal_normalized:.2f}")

        self.publish_angle(control_signal_normalized)
        self.binary_image = binary

def main():
    rclpy.init()

    motor_controller = MotorController()
    cv2.namedWindow('Filtrelenmiş Görüntü', cv2.WINDOW_NORMAL)
    try:
        while rclpy.ok():
            rclpy.spin_once(motor_controller, timeout_sec=0.1)
            if motor_controller.binary_image is not None:
                cv2.imshow('Filtrelenmiş Görüntü', motor_controller.binary_image)
                motor_controller.binary_image = None  # Görüntüyü bir kez gösterdikten sonra sıfırlayın
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
