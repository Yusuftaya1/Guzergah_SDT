#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor kontrolleri burada yapılır 

/mode_status 
/AGV/angle
/AGV/lidar_scan
/AGV/motor_values
/scan
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String ,Bool
from sensor_msgs.msg import LaserScan
from sdt_project.msg import MotorValues
import numpy as np
import time

class TaskManager:
    def __init__(self, motor_controller):
        self.motor_controller = motor_controller
        self.busy = False
    
    def perform_load_action(self, actuator_value):
        self.busy = True
        self.motor_controller.set_motor_values(250.0, 250.0, actuator_value)
        time.sleep(1.4)
        self.motor_controller.set_motor_values(0.0, 0.0, actuator_value)
        action = 'Yük alımı için' if actuator_value == 1000.0 else 'Yük bırakmak için'
        self.motor_controller.get_logger().info(f'{action} duruyor...')
        time.sleep(14)
        self.run_forward()
        self.busy = False

    def perform_turn(self, direction):
        self.busy = True
        self.run_forward()
        time.sleep(2.0)
        if direction == "right":
            self.motor_controller.set_motor_values(180.0, 360.0)
            self.motor_controller.get_logger().info('Sağa dönüş...')

        elif direction == "left":
            self.motor_controller.set_motor_values(360.0, 180.0)
            self.motor_controller.get_logger().info('Sola dönüş...')
            
        time.sleep(5.2)
        self.busy = False

    def run_forward(self):
        self.motor_controller.set_motor_values(250.0, 250.0)
        time.sleep(2)
    
    def engelden_kacma(self):
        self.busy = True
        self.motor_controller.set_motor_values(-300.0, -300.0)
        time.sleep(1.4)
        self.motor_controller.set_motor_values(350.0, 0.0)
        time.sleep(1.4)
        self.motor_controller.set_motor_values(350.0, 350.0)
        time.sleep(7.0)
        self.motor_controller.set_motor_values(0.0, 350.0)
        time.sleep(2.5)
        self.motor_controller.set_motor_values(350.0, 350.0)
        time.sleep(5.3)
        self.motor_controller.set_motor_values(350.0, -150.0)
        time.sleep(1.2)
        self.busy = False
    
    def rotate_around(self, direction, duration=2.0):
        if direction == "clockwise":
            self.motor_controller.set_motor_values(350.0, -350.0)
        elif direction == "counterclockwise":
            self.motor_controller.set_motor_values(-350.0, 350.0)
        time.sleep(duration)
    
    def autonom_charge(self):
        pass

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.wheel_distance = 0.35
        self.wheel_radius = 0.1
        self.coef = 0.02
        self.qr_id = None
        self.engel_detected = False
        self.engel_timer_count = 0
        self.task_manager = TaskManager(self)
        self.angle_sub          = self.create_subscription(Float64, '/AGV/angle', self.angle_callback, 10)
        self.mode_status_sub    = self.create_subscription(String, '/mode_status', self.mode_callback, 10)
        self.lidar_sub          = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.agitlik_sub        = self.create_subscription(Bool,'lift_agirlik',self.agirlik_callback)
        self.motor_values_pub   = self.create_publisher(MotorValues, '/AGV/motor_values', 10)
        self.engel_status_pub   = self.create_publisher(Bool,'engel_tespit',10)
        self.engel_check_timer  = self.create_timer(1.0, self.check_engel_status)
        self.motor_values_msg   = MotorValues()
        self.busy_publisher     = self.create_publisher(Bool,'cizgi_izlemee',10)
    
    def extract_first_part(self, qr_data):
        parts = qr_data.split(';')
        if parts:
            return parts[0]
        return None

    def mode_callback(self, msg):
        self.mode = msg.data
        if self.mode == "Turn Right":
            self.task_manager.perform_turn("right")

        if self.mode == "Turn Left":
            self.task_manager.perform_turn("left")
        
        if self.mode == "clockwise":
            self.task_manager.rotate_around("clockwise", 1.3)

        if self.mode == "counterclockwise":
            self.task_manager.rotate_around("counterclockwise", 1.3)
        
        if self.mode == "Load":
            self.task_manager.perform_load_action(1000.0)
            self.get_logger().info('Yük alındı, devam ediliyor...')

            self.task_manager.run_forward()

        if self.mode == "Unload":
            self.task_manager.perform_load_action(-1000.0)
            self.get_logger().info('Yük bırakıldı, devam ediliyor...')
            self.task_manager.run_forward()
        
        if self.mode == "Finish":
            self.get_logger().info('Finish komutu alındı, sistem durduruluyor...')
            self.set_motor_values(0.0, 0.0)
            rclpy.shutdown()

    def angle_callback(self, msg):
        if self.engel_detected or self.task_manager.busy:
            return
        
        angle = msg.data
        linear = 0.125
        w = angle * (1.0 - self.coef)
        
        if w != 0.0:
            right_speed = 2.5 * linear + (w * (self.wheel_distance / 2.0))
            left_speed = 2.5 * linear - (w * (self.wheel_distance / 2.0))
        else:
            right_speed = linear
            left_speed = linear

        right_speed_normalized = np.clip(right_speed, -1, 1)
        left_speed_normalized = np.clip(left_speed, -1, 1)
        
        self.set_motor_values(
            np.clip(1000 * right_speed_normalized, -1000, 1000),
            np.clip(1000 * left_speed_normalized, -1000, 1000)
            )
        
    def lidar_callback(self, msg):
        ranges = msg.ranges
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        angle_increment = msg.angle_increment
        scanned_angle_min = -2.378
        scanned_angle_max = 2.378
        msg_engel = Bool()

        start_index = int((scanned_angle_min - angle_min) / angle_increment)
        end_index = int((scanned_angle_max - angle_min) / angle_increment)

        start_index = max(0, start_index)
        end_index = min(len(ranges) - 1, end_index)
        scanned_ranges = ranges[:start_index] + ranges[end_index:]
        obstacles = [r for r in scanned_ranges if r < 0.45]

        if obstacles:
            self.engel_detected = True
            msg_engel.data = True
            self.get_logger().info('Engel tespit edildi!')
            self.set_motor_values(0.0, 0.0)
        else:
            self.engel_detected = False
            msg_engel.data = False
            
        #self.engel_status_pub.publish(msg_engel)

    def check_engel_status(self):
        if self.engel_detected:
            if not self.engel_detected:
                self.get_logger().info('Engel ortadan kalktı, devam ediliyor...')
                self.engel_detected = True
            else:
                self.engel_timer_count += 1
                if self.engel_timer_count >= 5:
                    self.get_logger().info('Engel 7 saniye boyunca ortadan kalkmadı, engelden kaçılıyor...')
                    self.busy_publisher.publish(msg=True)
                    self.task_manager.engelden_kacma()
                    self.busy_publisher.publish(msg=False)
                    self.engel_detected = False
        else:
            self.engel_timer_count = 0
            
    def set_motor_values(self, right_speed, left_speed, actuator_value=0.0):
        self.motor_values_msg.sag_teker_hiz = right_speed
        self.motor_values_msg.sol_teker_hiz = left_speed
        self.motor_values_msg.linear_actuator = actuator_value
        self.publish_motor_values()

    def publish_motor_values(self):
        self.get_logger().info(f'Sol teker hız: {self.motor_values_msg.sol_teker_hiz}')
        self.get_logger().info(f'Sağ teker hız: {self.motor_values_msg.sag_teker_hiz}')
        self.get_logger().info(f'Linear aktüatör: {self.motor_values_msg.linear_actuator}')
        self.motor_values_pub.publish(self.motor_values_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
