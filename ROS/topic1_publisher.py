#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import quaternion

def talker():
    pub = rospy.Publisher('topic1', quaternion, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        q = quaternion()
        q.x=1
        q.y=2
        q.z=3
        q.w=4
        rospy.loginfo(q)
        pub.publish(q)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass