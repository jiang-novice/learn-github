#!/bin/bash
#starting multi nodes
gnome-terminal --tab --title="node1" -- bash -c "cd; source ~/miniconda3/etc/profile.d/conda.sh; conda activate ros2; 
echo 'having activate ros2 env!'; 
echo 'starting node 1'; 
ros2 run turtlesim turtlesim_node; 
"

gnome-terminal --tab --title="node2" -- bash -c "cd; source ~/miniconda3/etc/profile.d/conda.sh; conda activate ros2; 
echo 'having activate ros2 env!'; 
echo 'starting node 2'; 
ros2 run turtlesim turtle_teleop_key; 
"