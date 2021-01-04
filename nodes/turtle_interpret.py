#!/usr/bin/env python

import rospy
import math
import time

from geometry_msgs.msg import Twist
from turtle_interpret.srv import VelTranslate



def handler_vel_translate(Twist):
    TurtleVel = Twist()
    return TurtleVel

def vel_translate_server():
    rospy.init_node('vel_translate_server') #rospy.init_node() first argument is just the name you want to python interpreter to call this method when called directly from the command line.
    s = rospy.Service('vel_translate', VelTranslate, handler_vel_translate)
    print("done sending service to client ")
    rospy.spin()


