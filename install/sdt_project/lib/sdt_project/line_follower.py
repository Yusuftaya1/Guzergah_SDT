#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Şerit Takip Etme ve PID Kontrolü
"""

import math
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float64, Bool
from cv_bridge import CvBridge

class CizgiTakip(Node):
    def __init__(self):   # ros2 düğümünü baslatır
        super().__init__('serit_takip_node')
        print("waiting for navigate_ready")
        #self.sub_mode = self.create_subscription(std_msgs.msg.Int8, '/AGV/main_mode_topic', self.mode_callback, 10)
        self.sub_image = self.create_subscription(Image, 'image_raw', self.kamera_callback, 10)
        self.pub_angle = self.create_publisher(Float64, '/AGV/angle', 10)
        self.cizgi_mesaji = Bool()
        self.aci_mesaji = Float64()
        self.bridge = CvBridge()
        self.bias = 1

    def kamera_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        roi = img[2 * img.shape[0] // 3 + 10:img.shape[0], 10:img.shape[1] - 20]
        mono = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(mono, (9, 9), 2, 2)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        erode = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        erode_img = cv2.erode(thresh, erode, iterations=1)
        dilate_img = cv2.dilate(erode_img, dilate, iterations=1)
        contours, _ = cv2.findContours(dilate_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        min_max_cx = -float('inf') if self.bias > 0 else float('inf')

        for cont in contours:
            mu = cv2.moments(cont, False)
            if mu['m00'] > 100.0:
                r = cv2.boundingRect(cont)
                cx = r[0] + r[2] - 12 if self.bias > 0 else r[0] + 12

                if self.bias > 0 and cx > min_max_cx:
                    min_max_cx = cx
                elif self.bias < 0 and min_max_cx > cx:
                    min_max_cx = cx
            else:
                self.cizgi_mesaji.data = False
                self.get_logger().info("Cizgi mesaji: ", self.cizgi_mesaji)

        if min_max_cx == float('inf') or min_max_cx == -float('inf'):
            min_max_cx = roi.shape[1] / 2

        self.aci_mesaji.data = 1.0 - 2.0 * min_max_cx / roi.shape[1]
        self.pub_angle.publish(self.aci_mesaji)
        self.get_logger().info(f'Publishing: {self.aci_mesaji.data}')
        
        cv2.imshow("Dilate", dilate_img)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    cizgi_takip = CizgiTakip()
    rclpy.spin(cizgi_takip)
    cizgi_takip.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()