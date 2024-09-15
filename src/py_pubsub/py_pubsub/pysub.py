import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SimpleSub(Node):

    def __init__(self):
        super().__init__('simple_sub_py')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  #just a formal use

    def listener_callback(self, msg):
        self.get_logger().info('Message: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    simple_sub = SimpleSub()

    rclpy.spin(simple_sub)
    simple_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()