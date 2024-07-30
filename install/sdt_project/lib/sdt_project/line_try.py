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

    def kamera_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
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
        
        min_cx = roi.shape[1]
        max_cx = 0
        for cont in contours:
            mu = cv2.moments(cont, False)
            if mu['m00'] > 100.0:
                r = cv2.boundingRect(cont)
                cx = r[0] + r[2] // 2
                if cx < min_cx:
                    min_cx = cx
                if cx > max_cx:
                    max_cx = cx

        if max_cx == 0 or min_cx == roi.shape[1]:
            self.cizgi_mesaji.data = False
            self.pub_line.publish(self.cizgi_mesaji)
            self.aci_mesaji.data = 0.0
            self.pub_angle.publish(self.aci_mesaji)
            return
        
        center_x = (min_cx + max_cx) / 2
        self.aci_mesaji.data = 1.0 - 2.0 * center_x / roi.shape[1]
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
######################################################################################################################
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
        self.sub_image = self.create_subscription(Image, 'image_raw', self.kamera_callback, 10)
        self.pub_angle = self.create_publisher(Float64, '/AGV/angle', 10)
        self.cizgi_mesaji = Bool()
        self.aci_mesaji = Float64()
        self.bridge = CvBridge()

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

        left_cx = None
        right_cx = None
        roi_center = roi.shape[1] // 2

        for cont in contours:
            mu = cv2.moments(cont, False)
            if mu['m00'] > 100.0:
                r = cv2.boundingRect(cont)
                cx = r[0] + r[2] // 2

                if cx < roi_center:
                    if left_cx is None or cx > left_cx:
                        left_cx = cx
                else:
                    if right_cx is None or cx < right_cx:
                        right_cx = cx

        if left_cx is not None and right_cx is not None:
            center_cx = (left_cx + right_cx) / 2
        elif left_cx is not None:
            center_cx = left_cx
        elif right_cx is not None:
            center_cx = right_cx
        else:
            center_cx = roi_center

        self.aci_mesaji.data = 1.0 - 2.0 * center_cx / roi.shape[1]
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
######################################################################################################################
#!/usr/bin/env python3
"""
A ROS2 node used to control a differential drive robot with a camera,
so it follows the line in a Robotrace style track.
You may change the parameters to your liking.
"""
__author__ = "Gabriel Nascarella Hishida do Nascimento"

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float64

import numpy as np
import cv2
import cv_bridge

# Create a bridge between ROS and OpenCV
bridge = cv_bridge.CvBridge()

# User-defined parameters
MIN_AREA = 500
LINEAR_SPEED = 0.2
TIMER_PERIOD = 0.06
lower_bgr_values = np.array([31,  42,  53])
upper_bgr_values = np.array([255, 255, 255])

def crop_size(height, width):
    return (2 * height // 3 + 10, height, 10, width - 20)

class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')
        self.subscription = self.create_subscription(Image, 'camera/image_raw', self.image_callback, 10)
        self.publisher = self.create_publisher(Float64, '/AGV/angle', 10)
        self.timer = self.create_timer(TIMER_PERIOD, self.timer_callback)
        self.image_input = None
        self.error = 0
        self.should_move = True

    def image_callback(self, msg):
        self.image_input = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def get_contour_data(self, mask, out):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cx_values = []
        for contour in contours:
            M = cv2.moments(contour)
            if M['m00'] > MIN_AREA:
                r = cv2.boundingRect(contour)
                cx = r[0] + r[2] // 2
                cx_values.append(cx)
                cv2.drawContours(out, [contour], -1, (255, 255, 0), 1)
        if cx_values:
            mean_cx = np.mean(cx_values)
        else:
            mean_cx = out.shape[1] / 2
        return mean_cx

    def timer_callback(self):
        if self.image_input is None:
            return

        height, width, _ = self.image_input.shape
        image = self.image_input.copy()

        crop_h_start, crop_h_stop, crop_w_start, crop_w_stop = crop_size(height, width)
        crop = image[crop_h_start:crop_h_stop, crop_w_start:crop_w_stop]
        mask = cv2.inRange(crop, lower_bgr_values, upper_bgr_values)

        output = image
        mean_cx = self.get_contour_data(mask, output[crop_h_start:crop_h_stop, crop_w_start:crop_w_stop])

        self.error = mean_cx - width // 2
        angle = 2.0 * (self.error / width)

        angle_msg = Float64()
        angle_msg.data = angle
        self.publisher.publish(angle_msg)
        self.get_logger().info(f'Publishing: {angle_msg.data}')

        cv2.rectangle(output, (crop_w_start, crop_h_start), (crop_w_stop, crop_h_stop), (0, 0, 255), 2)
        cv2.imshow("output", output)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = LineFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
