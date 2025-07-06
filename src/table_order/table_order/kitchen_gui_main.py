import sys

import rclpy
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


# import table_order.test_util
from table_order.kitchen_gui_order import MainPage
from table_order.kitchen_gui_navi import SecondPage

# from kitchen_gui_order import MainPage
# from kitchen_gui_navi import SecondPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        # rclpy.init()

    def init_ui(self):
        self.setWindowTitle("주문 관리 시스템")
        self.setGeometry(100, 100, 800, 600)

        # 스택 위젯 생성
        self.stack_widget = QStackedWidget()
        self.setCentralWidget(self.stack_widget)

        # # 첫 번째 페이지 (기존 메인 페이지)
        self.main_page = MainPage()
        self.stack_widget.addWidget(self.main_page)

        # # 두 번째 페이지
        self.second_page = SecondPage(self)
        self.stack_widget.addWidget(self.second_page)

        # self.robot_image = MyImage("src/table_order/table_order/img/robot.png", self)
        # self.robot_image.setVisible(False)
        # x, y = self.transform(-2.0, -0.5)
        # print(x, y)
        # self.robot_image.move(x, y)  # 초기 위치 설정

        # self.bg = MyImage("src/table_order/table_order/img/bg.png", self)
        # self.bg.setFixedSize(400, 480)  # 이미지 크기 조정
        # self.bg.setVisible(False)
        # self.bg.move(0, 0)  # 초기 위치 설정
        # self.stack_widget.currentChanged.connect(self.setRobotVisibility)

    # def setRobotVisibility(self):
    #     self.bg.setVisible(1 == self.stack_widget.currentIndex())
    #     # self.robot_image.setVisible(1 == self.stack_widget.currentIndex())

    # 변환 공식을 정의
    def transform(self, x, y):
        orig_x = int(y / 1.2 * 160 + 130)
        orig_y = int(210 + x * -90)
        return (orig_x, orig_y)


def main(argv=None):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
