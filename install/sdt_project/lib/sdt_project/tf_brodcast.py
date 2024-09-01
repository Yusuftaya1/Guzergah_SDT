#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import yaml

class TFPublisher(Node):

    def __init__(self):
        super().__init__('tf_publisher')
        self.transform_broadcasters = {}
        with open('/home/yusuf/Guzergah_SDT/src/sdt_project/yamls/tf.yaml', 'r') as file:
            self.frames = yaml.safe_load(file)['frames']
        for frame in self.frames:
            parent_frame = frame['parent']
            child_frame = frame['name']

            if parent_frame not in self.transform_broadcasters:
                self.transform_broadcasters[parent_frame] = TransformBroadcaster(self)
        
        self.timer = self.create_timer(0.1, self.publish_tf)

    def publish_tf(self):
        for frame in self.frames:
            t = TransformStamped()
            t.header.stamp = self.get_clock().now().to_msg()
            t.header.frame_id = frame['parent']
            t.child_frame_id = frame['name']

            t.transform.translation.x = frame['transform']['translation']['x']
            t.transform.translation.y = frame['transform']['translation']['y']
            t.transform.translation.z = frame['transform']['translation']['z']

            t.transform.rotation.x = frame['transform']['rotation']['x']
            t.transform.rotation.y = frame['transform']['rotation']['y']
            t.transform.rotation.z = frame['transform']['rotation']['z']
            t.transform.rotation.w = frame['transform']['rotation']['w']

            # Transform'u yayınla
            self.transform_broadcasters[frame['parent']].sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = TFPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
