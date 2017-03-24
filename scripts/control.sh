#!/bin/bash

echo 'START TURTLEBOT CONTROLLER'
source /opt/ocho/scripts/ros_config.bash
roslaunch kobuki_keyop keyop.launch
