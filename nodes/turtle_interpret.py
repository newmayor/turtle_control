

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move(vel_publish, direction):
    cmd_vel = Twist()

    global x,y
    x0 = x
    y0 = y

    #init the cmd vel publisher using existing turtlesim topic cmd_vel and msg Twist
    cmd_vel_pub = rospy.Publisher(cmd_vel, Twist, queue_size=10)

    while True:
        rospy.loginfo("starting motion")

        cmd_vel_pub.publish()



if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #subscriber node
        turtle_vel = "/turtle1/pose" #topic name for subscriber message. turtle1 is just an instantiation of the turtlesim robot and pose is a preexisting msg in the turtlesim package
        position_sub = rospy.Subscriber(turtle_vel, Pose, poseCallback) #Pose is an existing msg file in turtlesim

        #publisher node
        turtle_interpret = "/turtle1/cmd_vel" #topic name for publisher message. turtle1 is just an instantiation of the turtlesim robot and cmd_vel is a preexisting msg in the turtlesim package
        cmd_vel_pub = rospy.Publisher(turtle_interpret, Twist, queue_size=10) #Twist is an existing msg file in turtlesim
    
    except: rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
