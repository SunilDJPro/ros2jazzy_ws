from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_pubsub',
            executable='py_pub',
            name='publisher'
        ),
        Node(
            package='py_pubsub',
            executable='py_sub',
            name='subscriber'
        )
    ])
