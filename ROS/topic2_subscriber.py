#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import euler

def callback(data):
    rospy.loginfo(data)

def listener():
    rospy.init_node('topic2listener', anonymous=True)
    l = rospy.Subscriber('topic2',euler, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
