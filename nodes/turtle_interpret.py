#!/usr/bin/env python

import rospy
import math
import time

from geometry_msgs.msg import Twist
#from turtle_interpret.srv import VelTranslate


if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        turtle_vel = "/turtle1/cmd_vel" #topic name for TurtleVel messages. turtle1 is just an instantiation of the turtlesim robot and cmd_vel is a preexisting msg in the turtlesim package
        
        #subscriber node
        turtle_vel_sub = rospy.Subscriber(turtle_vel, TurtleVel, poseCallback) #Pose is an existing msg file in turtlesim

        #publisher node
        turtle_vel_pub = rospy.Publisher(turtle_vel, TurtleVel, queue_size=10) #Twist is an existing msg file in turtlesim
        time.sleep(2)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")

def handler_vel_translate(Twist):
    TurtleVel = Twist()
    return TurtleVel

def vel_translate_server():
    rospy.init_node('vel_translate_server') #rospy.init_node() first argument is just the name you want to python interpreter to call this method when called directly from the command line.
    s = rospy.Service('vel_translate', VelTranslate, handler_vel_translate)
    print("done sending service to client ")
    rospy.spin()


