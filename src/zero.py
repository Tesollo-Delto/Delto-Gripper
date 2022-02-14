#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState
from std_msgs.msg import Header

# This function is joint_state publisher.
def talker():
	pub = rospy.Publisher('/delto/joint_states', JointState, queue_size=10)
	rospy.init_node('joint_state_publisher')
	
	rate = rospy.Rate(2) # 10hz
	robot_hand_JointState = JointState()
	robot_hand_JointState.header = Header()
	robot_hand_JointState.header.stamp = rospy.Time.now()
	robot_hand_JointState.name = ['finger1_joint1', 'finger1_joint2', 'finger1_joint3', 'finger1_joint4',  
	                  		      'finger2_joint1', 'finger2_joint2', 'finger2_joint3', 'finger2_joint4',  
					  		      'finger3_joint1', 'finger3_joint2', 'finger3_joint3', 'finger3_joint4']

	finger_1_joint1_angle = 0.0
	finger_1_joint2_angle = 0.0
	finger_1_joint3_angle = 0.0
	finger_1_joint4_angle = 0.0
	finger_2_joint1_angle = 0.0
	finger_2_joint2_angle = 0.0
	finger_2_joint3_angle = 0.0
	finger_2_joint4_angle = 0.0
	finger_3_joint1_angle = 0.0
	finger_3_joint2_angle = 0.0
	finger_3_joint3_angle = 0.0
	finger_3_joint4_angle = 0.0

	while not rospy.is_shutdown():
		robot_hand_JointState.header.stamp = rospy.Time.now()
		
		finger_1_joint1_angle = finger_1_joint1_angle + 0.1
		finger_1_joint2_angle = finger_1_joint2_angle + 0.1
		finger_1_joint3_angle = finger_1_joint3_angle + 0.1
		finger_1_joint4_angle = finger_1_joint4_angle + 0.1
		finger_2_joint1_angle = finger_2_joint1_angle + 0.1
		finger_2_joint2_angle = finger_2_joint2_angle + 0.1
		finger_2_joint3_angle = finger_2_joint3_angle + 0.1
		finger_2_joint4_angle = finger_2_joint4_angle + 0.1
		finger_3_joint1_angle = finger_3_joint1_angle + 0.1
		finger_3_joint2_angle = finger_3_joint2_angle + 0.1
		finger_3_joint3_angle = finger_3_joint3_angle + 0.1
		finger_3_joint4_angle = finger_3_joint4_angle + 0.1

		robot_hand_JointState.position = [finger_1_joint1_angle, finger_1_joint2_angle, finger_1_joint3_angle, finger_1_joint4_angle, 
		                                  finger_2_joint1_angle, finger_2_joint2_angle, finger_2_joint3_angle, finger_2_joint4_angle,
		                                  finger_3_joint1_angle, finger_3_joint2_angle, finger_3_joint3_angle, finger_3_joint4_angle]

		pub.publish(robot_hand_JointState)
		print(robot_hand_JointState)
		print("-------------------")

		rate.sleep()


if __name__ == '__main__':
	talker()