# CRAZY TURTLE
Demonstration package for ME495.
This README is intentionally vague.
Figuring out how this package works and filling in the details is part of the
exercise. Replace the the blanks marked with `<angle brackets>` with your answer.
Unless otherwise specified, list the command and all arguments that you passed to it.

## Setup Instructions
1. Compile the workspace by executing `catkin_make`
2. Initialize the ROS environment (i.e., set the necessary ROS environment variables) by executing `source devel/setup.bash`
3. Run the launchfile `~/catkin_ws/src/crazy_turtle/launch` by executing `roslaunch`
4. When running you can see a visual depiction of the ROS graph using the `rqt_graph` command.
   The ROS graph, including all topics and node labels, looks like:
   ![see screenshot in git:](https://github.com/newmayor/turtle_control/blob/main/graph_step4.png)

## Runtime Information
The `launchfile` from above should be running when executing these commands.

5. Use the ROS command `rosnode list` to list all the nodes that are running.
   The output of the command looks like
   ```
   /mover
   /roaming_turtle
   /rosout

   ```
6. Use the ROS command `rostopic list` to list the topics
   The output of the command looks like
   ```
   /rosout
   /rosout_agg
   /turtle1/cmd_vel
   /turtle1/color_sensor
   /turtle1/pose

   ```

7. Use the ROS command `rostopic hz /turtle1/cmd_vel` to verify that the frequency of
   the `/turtle1/cmd_vel` topic is `100 Hz`

8. Use the ROS command `rosservice list` to list the services.
   The output of the command looks like
   ```
   /clear
   /kill
   /mover/get_loggers
   /mover/set_logger_level
   /reset
   /roaming_turtle/get_loggers
   /roaming_turtle/set_logger_level
   /rosout/get_loggers
   /rosout/set_logger_level
   /rostopic_34698_1607221414023/get_loggers
   /rostopic_34698_1607221414023/set_logger_level
   /spawn
   /switch
   /turtle1/set_pen
   /turtle1/teleport_absolute
   /turtle1/teleport_relative

   ```
9. Use the ROS command `rosservice info /switch` to view information about the `/switch` service.
   The type of the `/switch` service is `crazy_turtle/Switch` and it is offered by
   the `/mover` node.

10. Use the ROS command `rosparam list` to list the parameters that are loaded
    into the parameter server.
    The output of the command looks like
    ```
    
   /mover/velocity
   /roaming_turtle/background_b
   /roaming_turtle/background_g
   /roaming_turtle/background_r
   /rosdistro
   /roslaunch/uris/host_numair_pc__41443
   /rosversion
   /run_id

    ```

## Package and Dependencies
11. Use the ROS command `` rospack depends1 crazy_turtle `crazy_turtle`
   The output of the command looks like
   ```
   rospy
   message_runtime
   turtlesim
   ```
12. Use the ROS command `rossrv pacakge crazy_turtle` to list the types of services defined by `crazy_turtle`
    The output of the command looks like
    ```
    crazy_turtle/Switch

    ```
## Live Interaction
13. Use the ROS command `rosservice call /switch` to call the `/switch` service.
    The command returns `<return value>` and the turtle <brief description of what the turtle does>.
    (Hint: use `rossrv info` on the type of the `/switch` service to see the parameters.
     To test the behavior, look at the code or try calling with `x = 1`, `y = 1`, once with `linear_velocity = 0` and `angular_velocity = 0` and once with these at different nonzero values.)
14. What is the value of the `/mover/velocity` parameter? <value here>
15. What happens to the turtle's motion if you change `/mover/velocity` to 10 while the turtlesim and mover node are running? <faster | slower | same>
16. Use the ROS command `<command and args>` to kill the `/mover` node.
17. Use the ROS command `<command and args>` to start the `/mover` node. Be sure to
    remap `cmd_vel` to `/turtle1/cmd_vel`.
18. What happened to the turtle's velocity after relaunching `mover`? <faster | slower | same>