#!/bin/bash

echo 'INIT TURTLEBOT'
source /opt/ocho/scripts/ros_config.bash
rosrun kobuki_ftdi create_udev_rules
roslaunch kobuki_node minimal.launch --screen
