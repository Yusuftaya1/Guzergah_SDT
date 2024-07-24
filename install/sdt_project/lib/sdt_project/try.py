#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class CmdVelPublisher(Node):
    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.angle_sub = self.create_subscription(
            Bool,
            'bool_topic',
            self.bool_callback,
            10
        )
        timer_period = 0.5  # saniye
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bool_msg = False
        
    def bool_callback(self,msg):
        self.bool_msg = msg.data
        self.get_logger().info('bool callback:')

    def timer_callback(self):
        msg = Twist()
        if bool(self.bool_msg)  == False:
            msg.linear.x = 0.5
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = 0.1
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg)
        else:
            self.get_logger().info('FALSE BLOCK')

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
