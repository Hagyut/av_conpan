#!/bin/bash

echo 'INIT LRF SENSOR'
source /opt/ocho/scripts/ros_config.bash
cd /dev && ls -l ttyACM*
sudo chmod a+rw /dev/ttyACM0
rosrun urg_node urg_node
