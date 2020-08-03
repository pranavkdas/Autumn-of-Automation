#!/usr/bin/env python
import rospy
from math import atan2,asin,pi
from beginner_tutorials.msg import quaternion
from beginner_tutorials.msg import euler


def topic2_sender(a):
    pub = rospy.Publisher('topic2', euler, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(a)
        rate.sleep()

def callback(q):
    X = q.x
    Y = q.y
    Z = q.z
    W = q.w

    e = euler()
    e.roll= atan2((2*(W*X+Y*Z)), 1-2*(X*X+Y*Y))
    if (-1<2*(W*X-Y*Z)) and (2*(W*X-Y*Z)<1):
        output.pitch= asin(2*(W*X-Y*Z))
    else:
        e.pitch= pi/2
    e.yaw=atan2(2*(W*Z+X*Y), 1- 2*(Y*Y+Z*Z))
    topic2_sender(e)


def topic1_listen():
    rospy.init_node('my_converter', anonymous=True)
    rospy.Subscriber('topic1',quaternion, callback)
    rospy.spin()


if __name__ == '__main__':
    topic1_listen()
