import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SimplePub(Node):

    def __init__(self):
        super().__init__('simple_pub_py')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1  #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'I am working for %d' % self.i + ' seconds!'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    simple_pub = SimplePub()

    rclpy.spin(simple_pub)
    
    simple_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()