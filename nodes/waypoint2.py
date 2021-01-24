#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist



if __name__ == '__main__':
    rospy.init_node('waypoint2')

    #define first topic. This will be main topic for cmd_vel commands
    topic_cmd_vel = '/turtle1/cmd_vel'
    #once turtlesim node is loaded, need to first publish command to move turtle
    publisher_velocity = rospy.Publisher(topic_cmd_vel, Twist, queue_size=10)

    #once turtle has moved, we need the position of the turtle. make a subscriber
    topic_turtle_pose = '/turtle1/pose' #define the topic
    subscriber_pose = rospy.Subscriber(topic_turtle_pose, Pose, poseCallback)

    #define some kind of 'mover' function that will actually send desired positions to command the turtle to. 
    mover()

    print('waypoint moving of turtle1 is complete.')
