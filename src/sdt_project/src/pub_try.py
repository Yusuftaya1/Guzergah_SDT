#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import time
class BoolPublisher(Node):
    def __init__(self):
        super().__init__('bool_publisher')
        self.publisher_ = self.create_publisher(Bool, 'bool_topic', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bool_value = True

    def timer_callback(self):
        msg = Bool()
        self.bool_value = not self.bool_value 
        msg.data = self.bool_value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        time.sleep(2)

def main(args=None):
    rclpy.init(args=args)
    bool_publisher = BoolPublisher()
    rclpy.spin(bool_publisher)
    bool_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
