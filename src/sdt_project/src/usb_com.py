#!/usr/bin/env python3
"""
USB HABERLEŞME SAĞLANMASI;

TEKER HIZLARI "diff_node" içerisinde hesaplanır ve "motor_values_node"a "motor_values.msg"
MESAJI GÖNDERİLİR "motor_values" dan ALINAN VERİLER SERİ PORTA YAZILIR

SERİ PORTTAN ALINAN "SensorValues.msg" MESAJI "Interface_node" a gönderilir
"""

import rclpy
import serial
from rclpy.node import Node
from sdt_project.msg import MotorValues
from sdt_project.msg import SensorValues

class USBComNode(Node):
    def __init__(self):
        super().__init__('usb_com_node')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.sensor_values_publisher = self.create_publisher(SensorValues, '/AGV/sensor_values', 10)
        self.subscription = self.create_subscription(MotorValues,'/AGV/motor_values',self.motor_values_callback,10)    
        self.wheel_separation = 0.5
        self.wheel_radius = 0.1
        self.timer = self.create_timer(0.5, self.read_serialport_and_publish)

    def motor_values_callback(self, msg):
        right_wheel_velocity  = msg.sag_teker_hiz
        left_wheel_velocity   = msg.sol_teker_hiz
        linear_actuator       = msg.linear_actuator
        self.send_wheel_velocities(right_wheel_velocity, left_wheel_velocity, linear_actuator)

    def send_wheel_velocities(self, right_wheel_velocity, left_wheel_velocity, linear_actuator):
        right_wheel_velocity_str = f'{int(right_wheel_velocity):05}'
        left_wheel_velocity_str = f'{int(left_wheel_velocity):05}'
        linear_actuator_str = f'{int(linear_actuator):05}'
        
        command = f'{right_wheel_velocity_str},{left_wheel_velocity_str},{linear_actuator_str}\n'

        if self.serial_port.in_waiting == 0:
            self.get_logger().info(f'Seri porta gönderilen veri: {command}')
            self.serial_port.write(command.encode())

    def read_serialport_and_publish(self):
        if self.serial_port.in_waiting > 0:
            try:
                usb_data = self.serial_port.readline().decode('utf-8').strip()
                self.get_logger().info(f'USB\'den gelen veri: {usb_data}')
                sensor_values_msg = self.usb_data_splitter(usb_data)
                self.sensor_values_publisher.publish(sensor_values_msg)
            except Exception as e:
                self.get_logger().error(f'USB verisi okunurken hata: {str(e)}')
    
    def usb_data_splitter(self, usb_data):
        sensor_values_msg = SensorValues()
        try:
            values = usb_data.split(',')
            sensor_values_msg.sag_motor_sicaklik = float(values[0])
            sensor_values_msg.sol_motor_sicaklik = float(values[1])
            sensor_values_msg.lift_sicaklik = float(values[2])

            sensor_values_msg.sag_motor_akim = float(values[3])
            sensor_values_msg.sol_motor_akim = float(values[4])
            sensor_values_msg.lift_akim = float(values[5])

            sensor_values_msg.asiri_agirlik = bool(values[6])

        except Exception as e:
            self.get_logger().error(f'Veri ayrıştırma hatası: {str(e)}')
        return sensor_values_msg

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
