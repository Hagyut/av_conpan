#!/bin/bash

echo 'START SLAM ALGORITHM A'
source /opt/ocho/scripts/ros_config.bash
sudo chmod a+rw /dev/ttyACM0
roslaunch kobuki_slam kobuki_slam.launch
