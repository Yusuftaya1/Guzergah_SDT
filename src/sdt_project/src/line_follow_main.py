#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kod denendi videoda kullanıldı
"""
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class PID:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def update(self, measurement):
        error = self.setpoint - measurement
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.angle_pub = self.create_publisher(Float64, '/AGV/angle', 10)
        self.image_sub = self.create_subscription(Image, 'image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.binary_image = None
        #self.pid = PID(kp=6.25, ki=0.15, kd=0.2, setpoint=160)
        self.pid = PID(kp=10.5, ki=0.15, kd=0.6, setpoint=160)
        self.base_speed = 350
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
        except Exception as e:
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

        control_signal = self.pid.update(cX)

        if control_signal > 1000:
            control_signal = 1000
        elif control_signal < -1000:
            control_signal = -1000
        
        control_signal = np.clip(control_signal, -self.max_speed, self.max_speed)
        control_signal_normalized = control_signal / self.max_speed

        edge_threshold = 50
        edges = cv2.Canny(blurred, edge_threshold, edge_threshold * 2)
        edge_moments = cv2.moments(edges)
        
        if edge_moments['m00'] != 0:
            edge_cX = int(edge_moments['m10'] / edge_moments['m00'])
            if abs(edge_cX - cX) > 50:
                control_signal_normalized *= 1.5
                control_signal_normalized = np.clip(control_signal_normalized, -1, 1)

        self.get_logger().info(f"PID Kontrol Sinyali: {control_signal:.2f}")
        self.get_logger().info(f"PID Kontrol Sinyali (Normalleştirilmiş): {control_signal_normalized:.2f}")

        self.publish_angle(control_signal_normalized)

        self.binary_image = binary

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
