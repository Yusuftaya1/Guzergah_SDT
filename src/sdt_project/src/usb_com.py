#!/usr/bin/env python3
"""
USB HABERLEŞME SAĞLANMASI;

TEKER HIZLARI "diff_node" içerisinde hesaplanır ve "motor_values_node"a "motor_values.msg"
MESAJI GÖNDERİLİR "motor_values" dan ALINAN VERİLER SERİ PORTA YAZILIR

"""
import rclpy
import serial
from rclpy.node import Node
from sdt_project.msg import MotorValues

class USBComNode(Node):
    def __init__(self):
        super().__init__('usb_com_node')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.subscription = self.create_subscription(MotorValues,'/AGV/motor_values',self.motor_values_callback,10)
        self.wheel_separation = 0.5
        self.wheel_radius = 0.1
        self.timer = self.create_timer(2.0, self.read_serialport_and_publish)

    def motor_values_callback(self, msg):
        right_wheel_velocity  = msg.sag_teker_hiz
        left_wheel_velocity   = msg.sol_teker_hiz
        linear_actuator       = msg.linear_actuator
        self.send_wheel_velocities(right_wheel_velocity, left_wheel_velocity, linear_actuator)
    
    def send_wheel_velocities(self, right_wheel_velocity, left_wheel_velocity, linear_actuator):
        right_wheel_velocity_str = f'{int(right_wheel_velocity):05}'
        left_wheel_velocity_str  = f'{int(left_wheel_velocity):05}'
        linear_actuator_str      = f'{int(linear_actuator):05}'
        
        command = f'{right_wheel_velocity_str},{left_wheel_velocity_str},{linear_actuator_str}\n'

        if self.serial_port.in_waiting == 0:
            self.get_logger().info(f'Seri porta gönderilen veri: {command}')
            self.serial_port.write(command.encode())

    def destroy_node(self):
        self.serial_port.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    USB = USBComNode()
    rclpy.spin(USB)
    USB.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()