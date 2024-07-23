#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import websocket
import json
from geometry_msgs.msg import Twist
import threading

class SignalRBridge(Node):
    def __init__(self):
        super().__init__('signalr_bridge')
        self.ws = websocket.WebSocketApp("ws://10.7.91.190:5216/myhub",
                                         on_message=self.on_message,)
        
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)

        # Start WebSocket connection in a separate thread
        self.ws_thread = threading.Thread(target=self.ws.run_forever)
        self.ws_thread.start()

    def on_message(self, ws, message):
        self.get_logger().info(f"Received message from hub: {message}")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received message from ROS topic: linear={msg.linear}, angular={msg.angular}")
        data = {
            'linear': {
                'x': msg.linear.x,
                'y': msg.linear.y,
                'z': msg.linear.z,
            },
            'angular': {
                'x': msg.angular.x,
                'y': msg.angular.y,
                'z': msg.angular.z,
            }
        }
        self.ws.send(json.dumps(data))
        self.get_logger().info(f"Received meaaaaaaaaaaaaaaaaaa")
def main(args=None):
    rclpy.init(args=args)
    node = SignalRBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
