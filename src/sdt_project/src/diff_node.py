"""
mode_status YA DA action_status MSG KULLANILARAK MOTOR VALUES DEĞERİ 
QR BİLGİSİNE GÖRE , ÇİZGİYE GÖRE YA DA ESCAPE BLOCK OLARAK GÖNDERİLECEK

"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sdt_project.msg import MotorValues

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.wheel_distance = 0.35
        self.wheel_radius = 0.1
        self.coef = 0.02    
        
        self.angle_sub = self.create_subscription(
            Float64,
            '/AGV/angle',
            self.angle_callback,
            10
        )
        self.motor_values_pub = self.create_publisher(MotorValues, '/AGV/motor_values_node', 10)

    def angle_callback(self, msg):
        angle = msg.data
        linear = 0.1
        w = angle * (1.0 - self.coef)
        if w != 0.0:
            hiz_sol = linear - (w * (self.wheel_distance / 2.0))
            hiz_sag = linear + (w * (self.wheel_distance / 2.0))
        else:
            hiz_sol = linear
            hiz_sag = linear

        hiz_sol_angular = hiz_sol / (2 * 3.14159265 * self.wheel_radius)
        hiz_sag_angular = hiz_sag / (2 * 3.14159265 * self.wheel_radius)

        motor_values_msg = MotorValues()
        motor_values_msg.sag_teker_hiz = hiz_sol_angular
        motor_values_msg.sol_teker_hiz = hiz_sag_angular
        #motor_values_msg.linear_actuator = False

        self.motor_values_pub.publish(motor_values_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
