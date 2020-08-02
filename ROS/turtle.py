#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897


def forward(vel_msg,velocity_publisher,distance):

    speed = 3
    isForward = 1

    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0


    t0 = rospy.Time.now().to_sec()
    current_distance = 0


    while(current_distance < distance):
            
        velocity_publisher.publish(vel_msg)
            
        t1=rospy.Time.now().to_sec()
            
        current_distance= speed*(t1-t0)
        
    vel_msg.linear.x = 0
        
    velocity_publisher.publish(vel_msg)

    
def rotate(rot_msg,rotation_publisher,clockwise):

    speed = 10
    angle = 90
    

    
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    
    rot_msg.linear.x=0
    rot_msg.linear.y=0
    rot_msg.linear.z=0
    rot_msg.angular.x = 0
    rot_msg.angular.y = 0

    
    if clockwise:
        rot_msg.angular.z = -abs(angular_speed)
    else:
        rot_msg.angular.z = abs(angular_speed)
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        rotation_publisher.publish(rot_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    
    rot_msg.angular.z = 0
    rotation_publisher.publish(rot_msg)


def move():
    
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rotation_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rot_msg = Twist()

    clock1 = 0 #First rotation to left
    dist1 = 5 
    clock2 = 1 #Second rotation to right
    dist2 = 2
    

    while not rospy.is_shutdown():
    	rotate(rot_msg,rotation_publisher,clock1)
    	forward(vel_msg,velocity_publisher,dist1)
    	rotate(rot_msg,rotation_publisher,clock2)
    	forward(vel_msg,velocity_publisher,dist2)
    	rotate(rot_msg,rotation_publisher,clock2)
    	forward(vel_msg,velocity_publisher,dist2)
    	rotate(rot_msg,rotation_publisher,clock2)
    	forward(vel_msg,velocity_publisher,dist2)
    	break


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
