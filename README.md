# Delto-Gripper

## Overview

This is the official release to control Delto-Gripper with ROS Kinetic.

This document summarizes basic information for using Delto-Gripper.

The Delto-gripper has three fingers, and each finger is controlled by four independent joints by torque.


## ROS Packages for Delto-Gripper

Version kinetic + Ubuntu 16.04

If you use a version other than Kinetic, it cannot guarantee performance.

## Run Rviz & Gazebo

  + Gazebo Install
  
    Install ROS-Gazebo package.

    + Gazebo with ROS
      
      Please follow the [Gazebo Tutorials](http://gazebosim.org/tutorials?cat=connect_ros) to configure the simulation environment.   

    + Install Delto-Gripper

      Enter below command in order to download the Gazebo package for Delto-Gripper.

            cd ~/catkin_ws/src
            git clone https://github.com/TESOLLO-GIT/Delto-Gripper
    
    + Install additional Packages
   
      If ROS is installed with ros-kinetic-desktop-full option, additional packages may be required.
    
            sudo apt-get install ros-kinetic-ros-control
            sudo apt-get install ros-kinetic-ros-controllers
            sudo apt-get install ros-kinetic-gzeobo-ros-control
    
  + Build

        cd ~/catkin_ws
        catkin_make

  + Run 

    + Rviz

      To run with Rviz, enter the command below.
  
          roslaunch delto display.launch
        
    + Gazebo

      When using Delto-Gripper in Gazebo simulation, enter the command below.
        
          roslaunch delto gazebo.launch
          
      ![ScreenShot](https://raw.github.com/TESOLLO-GIT/Delto-Gripper/master/img.png)
      
      Click the Play button from Gazebo.
          
      Delto-Gripper's joints are as follows.<br/>
      [ finger1_joint1, finger1_joint2, finger1_joint3, finger1_joint4,<br/>
        finger2_joint1, finger2_joint2, finger2_joint3, finger2_joint4,<br/>
        finger3_joint1, finger3_joint2, finger3_joint3, finger3_joint4]
            
      When adjusting each joint using Terminal, use the command below. Adjust and use the value of 'data'.
      
          rostopic pub -1 /delto/finger1_1_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger1_2_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger1_3_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger1_4_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger2_1_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger2_2_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger2_3_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger2_4_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger3_1_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger3_2_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger3_3_effort/command std_msgs/Float64 "data: 0.0"
          rostopic pub -1 /delto/finger3_4_effort/command std_msgs/Float64 "data: 0.0"
          
      example:
        Apply 2 force to joint 4 of finger 3 and bend it.
        
          rostopic pub -1 /delto/finger3_4_effort/command std_msgs/Float64 "data: 2.0"
        


## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Support

This is a beta release version for the Delto-Gripper platform. There may be bugs and there are many things to improve.

Please direct support requests to support@tesollo.com.


