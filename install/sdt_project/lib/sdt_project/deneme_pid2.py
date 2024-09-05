#!/usr/local/pyenv/shims python3
# # -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float64, String
import cv2
import time
import numpy as np
from ultralytics import YOLO

# PID Kontrolcü sınıfı
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

class ImageProcessingNode(Node):
    def __init__(self):
        super().__init__('image_processing_node')

        # Publisher ve Subscriber'ları tanımla
        self.image_subscription = self.create_subscription(
            Image, 'image_raw', self.image_callback, 10)
        self.angle_pub = self.create_publisher(Float64, '/AGV/angle', 10)
        self.corner_pub = self.create_publisher(String, '/kose_detect', 10)

        # YOLOv8 modelini yükle
        self.model = YOLO('/home/guzergahh/Guzergah_SDT/line_follow/5.onnx')
        self.pid = PID(kp=0.6, ki=0.01, kd=0.4, setpoint=360)
        self.corner_detected_time = None
        self.lost_line_time = None
        self.lost_line_timeout = 1.5  # Çizgi kaybolduğunda bekleme süresi
        self.last_valid_cX = None  # Son geçerli cX değeri

    def image_callback(self, msg):
        # OpenCV formatına dönüştür
        frame = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
        frame_width = frame.shape[1]

        # YOLOv8 modelinden sonuçları al
        results = self.model(frame)
        filtered_results = [result for result in results[0].boxes.data if result[4] > 0.05]

        control_signal = 0  # Kontrol sinyali başlangıç değeri

        if filtered_results:
            cX = self.calculate_center_of_mass(filtered_results)
            if cX is not None:
                self.last_valid_cX = cX  # Son geçerli cX değerini kaydet

                if self.is_corner_detected(filtered_results[0], frame_width):
                    if self.corner_detected_time is None or (time.time() - self.corner_detected_time) > 2:
                        self.corner_detected_time = time.time()
                        if cX < frame_width / 2:  # Sol köşe
                            self.corner_pub.publish(String(data='left_corner'))
                        else:  # Sağ köşe
                            self.corner_pub.publish(String(data='right_corner'))
                else:
                    control_signal = np.clip(self.pid.update(cX), -self.max_speed, self.max_speed)
                    self.angle_pub.publish(Float64(data=control_signal))
                    self.get_logger().info(f"PID Kontrol Sinyali: {control_signal:.2f}")

                self.lost_line_time = None
            else:
                self.get_logger().info("Segment algılanamadı!")
        else:
            if self.lost_line_time is None:
                self.lost_line_time = time.time()

            elapsed_since_lost = time.time() - self.lost_line_time

            if elapsed_since_lost <= self.lost_line_timeout and self.last_valid_cX is not None:
                control_signal = np.clip(self.pid.update(self.last_valid_cX), -self.max_speed, self.max_speed)
                self.angle_pub.publish(Float64(data=control_signal))
                self.get_logger().info(f"Çizgi kayboldu, son bilinen yöne doğru manevra yapılıyor.")
            else:
                if self.last_valid_cX is not None:
                    control_signal = np.clip(self.pid.update(self.last_valid_cX), -self.max_speed * 1.5, self.max_speed * 1.5)
                    self.angle_pub.publish(Float64(data=control_signal))
                    self.get_logger().info("Çizgi uzun süre kayboldu, keskin manevra yapılıyor.")
                else:
                    self.angle_pub.publish(Float64(data=self.base_speed))
                    self.get_logger().info("Çizgi kayboldu, durduruluyor.")

    def is_corner_detected(self, segment, frame_width):
        x1, y1, x2, y2 = map(int, segment[:4])
        width = x2 - x1
        return width > frame_width * 0.7

    def calculate_center_of_mass(self, segments):
        total_weight = 0
        weighted_sum = 0
        for segment in segments:
            x1, _, x2, _ = map(int, segment[:4])
            width = x2 - x1
            cX = (x1 + x2) / 2
            total_weight += width
            weighted_sum += cX * width
        return weighted_sum / total_weight if total_weight > 0 else None

def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
