#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import OccupancyGrid

class OccupancyGridListener(Node):

    def __init__(self):
        super().__init__('occupancy_grid_listener')

        self.subscription = self.create_subscription(
            OccupancyGrid,
            'occupancy_grid',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info('Received OccupancyGrid message:')
        self.get_logger().info(f'Header: {msg.header}')
        self.get_logger().info(f'Info: {msg.info}')
        self.get_logger().info(f'Grid Data Length: {len(msg.data)}')
        self.get_logger().info('First 10 data points: ' + ', '.join(map(str, msg.data[:10])))
        self.get_logger().info('---')

def main(args=None):
    rclpy.init(args=args)
    node = OccupancyGridListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
