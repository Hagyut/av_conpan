#!/bin/bash

echo 'START SLAM ALGORITHM B'
source /opt/ocho/scripts/ros_config.bash
roslaunch hector_mapping mapping_default.launch
