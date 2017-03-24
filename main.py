#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAbstractButton, QToolTip, QPushButton, QLabel)
from PyQt5.QtGui import (QIcon, QFont, QPixmap, QPainter, QPalette, QBrush)

window_title = 'Ocho&Ajou AV Project'
ws_dir = os.path.dirname(os.path.abspath(__file__))
size_scale = 1.8

class QImageButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(QImageButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.param = []
        self.initUI()

    def initUI(self):
        
        
        ## BACKROUND
        bg_img = QPixmap(ws_dir + "/images/bg.png")
        bg_img = bg_img.scaled(bg_img.width(), bg_img.height())
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(bg_img))
        self.setPalette(palette)
        self.setGeometry(100, 100, bg_img.width(), bg_img.height())
        ## TITLE
        self.setWindowTitle(window_title)
        ## ICON
        icon = QIcon(ws_dir + '/images/icon.png')
        self.setWindowIcon(icon)


        ## ROS SECTION
        ##      [BUTTON] INIT ROSCORE
        ros_init_btn_img = QPixmap(ws_dir + '/images/button/ros_init.png')
        ros_init_btn_img = ros_init_btn_img.scaled(ros_init_btn_img.width()/size_scale, ros_init_btn_img.height()/size_scale)
        self.ros_init_btn = QImageButton(ros_init_btn_img, self)
        self.ros_init_btn.setToolTip('ROS Core를 작동시키는 버튼입니다.')
        self.ros_init_btn.resize(self.ros_init_btn.sizeHint())
        self.ros_init_btn.move(20, 55)
        self.ros_init_btn.clicked.connect(lambda : self.exeShellScript('ros.sh', 'INIT ROSCORE'))
        ##      [BUTTON] ROS CONFIG
        ros_config_btn_img = QPixmap(ws_dir + '/images/button/ros_config.png')
        ros_config_btn_img = ros_config_btn_img.scaled(ros_config_btn_img.width()/size_scale, ros_config_btn_img.height()/size_scale)
        self.ros_config_btn = QImageButton(ros_config_btn_img, self)
        self.ros_config_btn.setToolTip('ROS 설정 파일을 실행하는 버튼입니다.')
        self.ros_config_btn.resize(self.ros_config_btn.sizeHint())
        self.ros_config_btn.move(215, 55)
        self.ros_config_btn.clicked.connect(lambda : self.exeShellScript('ros_config.sh', 'INIT ROSCORE'))
        
        ## TURTLEBOT SECTION
        ##      [BUTTON] INIT TURTLEBOT
        start_btn_img = QPixmap(ws_dir + '/images/button/turtlebot_setup.png')
        start_btn_img = start_btn_img.scaled(start_btn_img.width()/size_scale, start_btn_img.height()/size_scale)
        self.start_btn = QImageButton(start_btn_img, self)
        self.start_btn.setToolTip('TurtleBot에 시동을 거는 버튼입니다.')
        self.start_btn.resize(self.start_btn.sizeHint())
        self.start_btn.move(20, 170)
        self.start_btn.clicked.connect(lambda : self.exeShellScript('turtlebot.sh', 'INIT TURTLEBOT'))
        ##      [BUTTON] START TURTLEBOT CONTROLLER
        control_btn_img = QPixmap(ws_dir + '/images/button/turtlebot_control.png')
        control_btn_img = control_btn_img.scaled(control_btn_img.width()/size_scale, control_btn_img.height()/size_scale)
        self.control_btn = QImageButton(control_btn_img, self)
        self.control_btn.setToolTip('TurtleBot 컨트롤 프로그램을 실행하는 버튼입니다.')
        self.control_btn.resize(self.control_btn.sizeHint())
        self.control_btn.move(215, 170)
        self.control_btn.clicked.connect(lambda : self.exeShellScript('control.sh', 'START TURTLEBOT CONTROLLER'))

        ## SENSORS SECTION
        ##      [BUTTON] INIT RGBD CAM
        astra_btn_img = QPixmap(ws_dir + '/images/button/rgbd_cam.png')
        astra_btn_img = astra_btn_img.scaled(astra_btn_img.width()/size_scale, astra_btn_img.height()/size_scale)
        self.astra_btn = QImageButton(astra_btn_img, self)
        self.astra_btn.setToolTip('RGBD Camera를 실행하는 버튼입니다.')
        self.astra_btn.resize(self.astra_btn.sizeHint())
        self.astra_btn.move(20, 283)
        self.astra_btn.clicked.connect(lambda : self.exeShellScript('rgbd_cam.sh', 'INIT RGBD CAM'))
        ##      [BUTTON] INIT LRF SENSOR
        hokuyo_btn_img = QPixmap(ws_dir + '/images/button/lrf.png')
        hokuyo_btn_img = hokuyo_btn_img.scaled(hokuyo_btn_img.width()/size_scale, hokuyo_btn_img.height()/size_scale)
        self.hokuyo_btn = QImageButton(hokuyo_btn_img, self)
        self.hokuyo_btn.setToolTip('LRF Sensor를 실행하는 버튼입니다.')
        self.hokuyo_btn.resize(self.hokuyo_btn.sizeHint())
        self.hokuyo_btn.move(215, 283)
        self.hokuyo_btn.clicked.connect(lambda : self.exeShellScript('lrf.sh', 'INIT LRF SENSOR'))

        ## SLAM ALGORITHMS SCTION
        ##      [BUTTON] START SLAM ALGORITHM A
        algo_a_btn_img = QPixmap(ws_dir + '/images/button/algo_a.png')
        algo_a_btn_img = algo_a_btn_img.scaled(algo_a_btn_img.width()/size_scale, algo_a_btn_img.height()/size_scale)
        self.algo_a_btn = QImageButton(algo_a_btn_img, self)
        self.algo_a_btn.setToolTip('설정된 Fast SLAM을 실행하는 버튼입니다.')
        self.algo_a_btn.resize(self.algo_a_btn.sizeHint())
        self.algo_a_btn.move(20, 398)
        self.algo_a_btn.clicked.connect(lambda : self.exeShellScript('algo_a.sh', 'START SLAM ALGORITHM A'))
        ##      [BUTTON] START SLAM ALGORITHM B
        algo_b_btn_img = QPixmap(ws_dir + '/images/button/algo_b.png')
        algo_b_btn_img = algo_b_btn_img.scaled(algo_b_btn_img.width()/size_scale, algo_b_btn_img.height()/size_scale)
        self.algo_b_btn = QImageButton(algo_b_btn_img, self)
        self.algo_b_btn.setToolTip('설정된 EKF기반 SLAM을 실행하는 버튼입니다.')
        self.algo_b_btn.resize(self.algo_b_btn.sizeHint())
        self.algo_b_btn.move(215, 398)
        self.algo_b_btn.clicked.connect(lambda : self.exeShellScript('algo_b.sh', 'START SLAM ALGORITHM B'))

        ## UTILITIES SECTION
        ##      [BUTTON] INIT RVIZ
        rviz_btn_img = QPixmap(ws_dir + '/images/button/rviz.png')
        rviz_btn_img = rviz_btn_img.scaled(rviz_btn_img.width()/size_scale, rviz_btn_img.height()/size_scale)
        self.rviz_btn = QImageButton(rviz_btn_img, self)
        self.rviz_btn.setToolTip('RViz(data visualization program)를 실행하는 버튼입니다.')
        self.rviz_btn.resize(self.rviz_btn.sizeHint())
        self.rviz_btn.move(20, 512)
        self.rviz_btn.clicked.connect(lambda : self.exeShellScript('rviz.sh', 'INIT RVIZ'))
        ##      [BUTTON] INIT GAZEBO
        gazebo_btn_img = QPixmap(ws_dir + '/images/button/gazebo.png')
        gazebo_btn_img = gazebo_btn_img.scaled(gazebo_btn_img.width()/size_scale, gazebo_btn_img.height()/size_scale)
        self.gazebo_btn = QImageButton(gazebo_btn_img, self)
        self.gazebo_btn.setToolTip('Gazebo(simulation program)을 실행하는 버튼입니다.')
        self.gazebo_btn.resize(self.gazebo_btn.sizeHint())
        self.gazebo_btn.move(215, 512)
        self.gazebo_btn.clicked.connect(lambda : self.exeShellScript('gazebo.sh', 'INIT GAZEBO'))

        ## SHOW MAIN WINDOW
        self.show()
    
    def exeShellScript(self, script_name, message):
        script_dir = ws_dir + '/scripts/'
        script_path = script_dir + script_name
        os.system('gnome-terminal -x ' + script_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    
    sys.exit(app.exec_())
