#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def callback(data):

    radian2decimal = 32768 / 3.141592
    name = list(data.name)
    position = list(data.position)

    for i in range(0,12):
        position[i] = (int)(position[i] * radian2decimal + 32768)
        position[i] = hex(position[i])

    rospy.loginfo( "\n"+
        name[0] + ": " + position[0] + "\t" +
        name[1] + ": " + position[1] + "\t" +
        name[2] + ": " + position[2] + "\t" +
        name[3] + ": " + position[3] + "\n" +
        name[4] + ": " + position[4] + "\t" +
        name[5] + ": " + position[5] + "\t" +
        name[6] + ": " + position[6] + "\t" +
        name[7] + ": " + position[7] + "\n" +
        name[8] + ": " + position[8] + "\t" +
        name[9] + ": " + position[9] + "\t" +
        name[10] + ": " + position[10] + "\t" +
        name[11] + ": " + position[11]
        )
    


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/delto/joint_states', JointState, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

