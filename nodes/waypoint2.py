#!/usr/bin/env python3

##############################
## NOTES ##
## The idea for calculating Euclidian distance using distance formula taken from ros tutorials and Anis Koubba tutorials
##############################

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from turtlesim.msg import Pose

import math
import time


def poseCallback(msg_pose): #placeholder. need to define a callback for the subscriber node
    global x2, y2, yaw
    x2 = msg_pose.x
    y2 = msg_pose.y
    #the callback allows for pose of turtle to be saved into global x2 and y2 to be accessible by other functions for later use.

    yaw = msg_pose.theta #callback the angular position of turtle


def mover(publisher_velocity ,distance):

    global x2,y2
    y1 = y2
    x1 = x2

    distance_moved = 0.0 #init variable
    msg_velocity = Twist() #define msg_velocity to be Twist
    msg_velocity.linear.x = abs(2) #set speed of turtle to be 2.0 units
    
    rate = rospy.Rate(10)

    #start moving the turtle
    while True:
        
        #start publishing velocity commands
        publisher_velocity.publish(msg_velocity)

        rate.sleep()

        #need some way to calcualte distance traveled
        distance_moved = math.sqrt(((y2-y1)**2) + ((x2-x1)**2)) #basic distance formula

        print("turtle has moved %d pixels\r\n", distance_moved)
        if (distance_moved >= distance): #check for terminating condition
            print("reached destination\r\n")
            break #this exits the while True loop
    
    #once while loop is exited, the distance desired is achieved so now turtle can stop moving
    msg_velocity.linear.x = 0 #set velocity command to 0
    publisher_velocity.publish(msg_velocity) #publish the 0 velocity command so turtle stops

#use the same structure as linear mover() function to define a spin() function that will change angle of turtle
def spin(publisher_velocity , subscriber_pose, desired_deg): #angle is in degrees for human readability
    
    global yaw #angular data coming from Pose callback function
    desired_rad = math.radians(desired_deg)
    yaw0 = yaw
    
    msg_velocity = Twist() #define msg_velocity to be Twist
    msg_velocity.angular.z = abs(2) #set speed of turtle to be 2.0 units
    
    rate = rospy.Rate(10)

    #start moving the turtle
    while True:
        
        #start publishing velocity commands to rotate turtle
        publisher_velocity.publish(msg_velocity)

        rate.sleep()

        #angle_moved = desired_rad - yaw #check difference b/w desired_rad angle to yaw pose

        print("turtle has turned %d deg\r\n", math.radians(yaw))
        if (yaw >= desired_rad + yaw0): #check for terminating condition
            print("reached destination\r\n")
            break #this exits the while True loop
    
    #once while loop is exited, the angle desired is achieved so now turtle can stop spinning
    msg_velocity.angular.z = 0 #set angular velocity command to 0
    publisher_velocity.publish(msg_velocity) #publish the 0 velocity command so turtle stops


if __name__ == '__main__':
    rospy.init_node('waypoint2')

    #define first topic. This will be main topic for cmd_vel commands
    topic_cmd_vel = '/turtle1/cmd_vel'
    #once turtlesim node is loaded, need to first publish command to move turtle
    publisher_velocity = rospy.Publisher(topic_cmd_vel, Twist, queue_size=10)

    #once turtle has moved, we need the position of the turtle. make a subscriber
    topic_turtle_pose = '/turtle1/pose' #define the topic
    subscriber_pose = rospy.Subscriber(topic_turtle_pose, Pose, poseCallback)
    time.sleep(2)

    #define some kind of 'mover' function that will actually send desired positions to command the turtle to. 
    
    mover(publisher_velocity ,1)
    spin(publisher_velocity, subscriber_pose, 90)
    time.sleep(1)
    mover(publisher_velocity ,1)
    spin(publisher_velocity, subscriber_pose, 90)
    time.sleep(1)
    mover(publisher_velocity ,1)
    spin(publisher_velocity, subscriber_pose, 90)
    time.sleep(1)
    mover(publisher_velocity ,1)
    spin(publisher_velocity, subscriber_pose, 90)
    time.sleep(1)
    

    print('waypoint moving of turtle1 is complete.')

