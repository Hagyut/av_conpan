#!/bin/bash

echo 'INIT GAZEBO'
source /opt/ocho/scripts/ros_config.bash
roslaunch kobuki_gazebo kobuki_empty_world.launch
