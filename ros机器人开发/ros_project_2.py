import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("python_node")
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0
        self.get_logger().info("节点已启动")

    def timer_callback(self):
        self.count += 1
        self.get_logger().info(f"运行中: {self.count}")

def main():
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()