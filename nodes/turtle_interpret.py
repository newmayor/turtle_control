#!/usr/bin/env python

import rospy
import math
import time
from turtle_control.msg import TurtleVel
from geometry_msgs.msg import Twist
from turtlesim.msg import Poses

def poseCallback(position_message):
    global x,y, yaw
    x = position_message.x
    y = position_message.y
    yaw = position_message.theta

def move(speed, distance, go_forward):
    global x,y
    x0 = x
    y0 = y

    distance_moved = 0 #this will be updated in the while loop as the turtle moves


    turtle_vel = "/turtle1/cmd_vel" #topic name for TurtleVel messages. turtle1 is just an instantiation of the turtlesim robot and cmd_vel is a preexisting msg in the turtlesim package
    
    #initialize the subscriber and publisher nodes on the same topic "turtle_vel" with same message type "TurtleVel"
    loop_rate = rospy.Rate(10) #publish 10 message per second
    turtle_vel_sub = rospy.Subscriber(turtle_vel, TurtleVel, poseCallback) #poseCallback will publish the change in position

    #publisher node
    turtle_vel_pub = rospy.Publisher(turtle_vel, TurtleVel, queue_size=10) #Twist is an existing msg file in turtlesim

    #set the speed and direction of velocity command "TurtleVel"
    if (go_forward):
        TurtleVel.linear.x = abs(speed)
    else:
        TurtleVel.linear.x = -abs(speed)

        
    while True:
        rospy.loginfo("moving forward")
        
        #prepare to move
        #publish the speed and direction of turtle's motion using the "speed" and "direction" parameters passed into the move() method. Use them in the TurtleVel message
        turtle_vel_pub.publish(TurtleVel)

        loop_rate.sleep()

        #use the distance equation to update the turtle's distance moved
        distance_moved = abs(math.sqrt(((x-x0)**2) + ((y-y0)**2)))

        rospy.loginfo("Turtle moved: ")
        print(distance_moved)

        #check for move stop condition
        if (distance_moved>distance):
            rospy.loginfo("destination reached")
            break

def handler_vel_translate(Twist):
    TurtleVel = Twist()
    return TurtleVel

def vel_translate_server():
    rospy.init_node('vel_translate_server') #rospy.init_node() first argument is just the name you want to python interpreter to call this method when called directly from the command line.
    s = rospy.Service('vel_translate', VelTranslate, handler_vel_translate)
    print("done sending service to client ")
    rospy.spin()


if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        turtle_vel = "/turtle1/cmd_vel" #topic name for TurtleVel messages. turtle1 is just an instantiation of the turtlesim robot and cmd_vel is a preexisting msg in the turtlesim package
        
        #subscriber node
        turtle_vel_sub = rospy.Subscriber(turtle_vel, TurtleVel, poseCallback) #Pose is an existing msg file in turtlesim

        #publisher node
        turtle_vel_pub = rospy.Publisher(turtle_vel, TurtleVel, queue_size=10) #Twist is an existing msg file in turtlesim
        time.sleep(2)

    except: rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
