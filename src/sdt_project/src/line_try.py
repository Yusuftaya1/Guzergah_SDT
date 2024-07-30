#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Şerit Takip Etme ve PID Kontrolü
"""

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float64, Bool
from cv_bridge import CvBridge

class CizgiTakip(Node):
    def __init__(self):   # ros2 düğümünü başlatır
        super().__init__('serit_takip_node')
        print("waiting for navigate_ready")
        self.sub_image = self.create_subscription(Image, 'image_raw', self.kamera_callback, 10)
        self.pub_angle = self.create_publisher(Float64, '/AGV/angle', 10)
        self.pub_line = self.create_publisher(Bool, '/AGV/line', 10)
        self.cizgi_mesaji = Bool()
        self.aci_mesaji = Float64()
        self.bridge = CvBridge() 

        # PID parametreleri
        self.kp = 0.3
        self.ki = 0.0
        self.kd = 0.2
        self.target_angle = 0.0
        self.error = 0.0
        self.prev_error = 0.0
        self.integral = 0.0

    def kamera_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        # Görüntüden ROI seçimi: Ekranın alt üçte biri
        roi = img[2 * img.shape[0] // 3:img.shape[0], 0:img.shape[1]]
        mono = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(mono, (9, 9), 2)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        erode = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        erode_img = cv2.erode(thresh, erode, iterations=1)
        dilate_img = cv2.dilate(erode_img, dilate, iterations=1)
        
        contours, _ = cv2.findContours(dilate_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            self.aci_mesaji.data = 0.0
            self.pub_angle.publish(self.aci_mesaji)
            return
        
        # Şeridin en geniş noktasını bulma
        min_cx = roi.shape[1]
        max_cx = 0
        for cont in contours:
            mu = cv2.moments(cont, False)
            if mu['m00'] > 100.0:
                r = cv2.boundingRect(cont)
                cx = r[0] + r[2] // 2  # Merkezi x koordinatı
                if cx < min_cx:
                    min_cx = cx
                if cx > max_cx:
                    max_cx = cx
        
        # Şeridin ortasını bulma
        if max_cx == 0 or min_cx == roi.shape[1]:
            self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            self.aci_mesaji.data = 0.0
            self.pub_angle.publish(self.aci_mesaji)
            return
        
        center_x = (min_cx + max_cx) / 2
        aci_mesajii = 1.0 - 2.0 * center_x / roi.shape[1]

        # PID kontrolü
        self.error = self.target_angle - aci_mesajii
        self.integral += self.error
        derivative = self.error - self.prev_error
        self.aci_mesaji.data = self.kp * self.error + self.ki * self.integral + self.kd * derivative
        self.prev_error = self.error

        self.cizgi_mesaji.data = True
        self.pub_line.publish(self.cizgi_mesaji)
        self.pub_angle.publish(self.aci_mesaji)

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
################################################################################################################
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
        self.pub_line = self.create_publisher(Bool, '/AGV/line', 10)
        self.cizgi_mesaji = Bool()
        self.aci_mesaji = Float64()
        self.bridge = CvBridge() # opencv ıle ros dugumlerı arasında ıletısım kurmak ıcın
        self.bias = 1

        # PID parametreleri
        self.kp = 0.3              # katsayılar kp ki kd
        self.ki = 0.0               # target angle hedef acısı
        self.kd = 0.2              # kamera callbackden aldığı veriye göre output pub_angle da yayınladı
        self.target_angle = 0.0     # target angele ı hedeflenen acıya göre ayarlanacak
        self.error = 0.0            # en son entegre olunmus hali
        self.prev_error = 0.0
        self.integral = 0.0

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
                self.cizgi_mesaji.data = True
            else:
                self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            #self.get_logger().info(f'Publishing: {self.cizgi_mesaji}')

        if min_max_cx == float('inf') or min_max_cx == -float('inf'):
            min_max_cx = roi.shape[1] / 2

        aci_mesajii = 1.0 - 2.0 * min_max_cx / roi.shape[1]

        # PID kontrolü
        self.error = self.target_angle - aci_mesajii
        self.integral += self.error
        derivative = self.error - self.prev_error
        self.aci_mesaji.data  = self.kp * self.error + self.ki * self.integral + self.kd * derivative

        self.prev_error = self.error

        self.pub_angle.publish(self.aci_mesaji)
        self.get_logger().info(f'Publishing: {self.aci_mesaji.data}')
        #self.pub_angle.publish(current_angle)

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

################################################################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Şerit Takip Etme ve PID Kontrolü
"""

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float64, Bool
from cv_bridge import CvBridge

class CizgiTakip(Node):
    def __init__(self):
        super().__init__('serit_takip_node')
        self.sub_image = self.create_subscription(Image, 'image_raw', self.kamera_callback, 10)
        self.pub_angle = self.create_publisher(Float64, '/AGV/angle', 10)
        self.pub_line = self.create_publisher(Bool, '/AGV/line', 10)
        self.cizgi_mesaji = Bool()
        self.aci_mesaji = Float64()
        self.bridge = CvBridge()  # OpenCV ile ROS düğümleri arasında iletişim kurmak için

        # PID parametreleri
        self.kp = 0.3
        self.ki = 0.0
        self.kd = 0.2
        self.target_angle = 0.0
        self.error = 0.0
        self.prev_error = 0.0
        self.integral = 0.0

    def kamera_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # Görüntüden ROI seçimi: Ekranın alt üçte biri
        roi = img[2 * img.shape[0] // 3:img.shape[0], 0:img.shape[1]]
        mono = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(mono, (9, 9), 2)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        erode = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        erode_img = cv2.erode(thresh, erode, iterations=1)
        dilate_img = cv2.dilate(erode_img, dilate, iterations=1)
        
        contours, _ = cv2.findContours(dilate_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            self.aci_mesaji.data = 0.0
            self.pub_angle.publish(self.aci_mesaji)
            return
        
        # Şeridin merkez x koordinatını bulma
        cx_values = []
        for cont in contours:
            mu = cv2.moments(cont, False)
            if mu['m00'] > 100.0:
                r = cv2.boundingRect(cont)
                cx = r[0] + r[2] // 2
                cx_values.append(cx)
        
        if not cx_values:
            self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            self.aci_mesaji.data = 0.0
            self.pub_angle.publish(self.aci_mesaji)
            return
        
        # Şeridin ortasını bulma
        avg_cx = np.mean(cx_values)
        img_center_x = roi.shape[1] / 2
        aci_mesajii = (avg_cx - img_center_x) / img_center_x

        # PID kontrolü
        self.error = self.target_angle - aci_mesajii
        self.integral += self.error
        derivative = self.error - self.prev_error
        self.aci_mesaji.data = self.kp * self.error + self.ki * self.integral + self.kd * derivative
        self.prev_error = self.error

        self.cizgi_mesaji.data = True
        self.pub_line.publish(self.cizgi_mesaji)
        self.pub_angle.publish(self.aci_mesaji)

        # Görüntüyü göster
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