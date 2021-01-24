#!/usr/bin/env python3

##############################
## NOTES ##
## The idea for calculating Euclidian distance using distance formula taken from ros tutorials and Anis Koubba tutorials
##############################

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

import math

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
    mover(90)

    print('waypoint moving of turtle1 is complete.')

def poseCallback(msg_pose): #placeholder. need to define a callback for the subscriber node
    global x2, y2
    x2 = msg_pose.x
    y2 = msg_pose.y
    #the callback allows for pose of turtle to be saved into global x2 and y2 to be accessible by other functions for later use.


def mover(distance):

    global x2,y2
    y1 = y2
    x1 = x2

    distance_moved = 0.0 #init variable
    msg_velocity = Twist #define msg_velocity to be Twist
    msg_velocity.x = 2.0 #set speed of turtle to be 2.0 units

    #start moving the turtle
    while True:
        
        #start publishing velocity commands
        publisher_velocity.publish(msg_velocity)

        rospy.Rate.sleep()

        #need some way to calcualte distance traveled
        distance_moved = math.sqrt(((y2-y1)**2) + ((x2-x1)**2)) #basic distance formula

        print("turtle has moved %d pixels\r\n", distance_moved)
        if (distance_moved >= distance): #check for terminating condition
            print("reached destination\r\n")
            break #this exits the while True loop
    
    #once while loop is exited, the distance desired is achieved so now turtle can stop moving
    msg_velocity.x = 0 #set velocity command to 0
    publisher_velocity.publish(msg_velocity) #publish the 0 velocity command so turtle stops


