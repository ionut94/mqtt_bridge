#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# Create a class to subscribe to the goal location received from mqtt broaker
class GoalSubscriber:
    def __init__(self):
        self.previous_goal = None
        rospy.init_node('goal_subscriber', anonymous=True)
        rospy.Subscriber('/argHRI/robot_goal_location', String, self.goal_callback)

    # Define the callback function to process the goal location 
    # only if it is different from the previous goal
    def goal_callback(self, data):
        if data.data != self.previous_goal:
            # Send the goal here
            self.previous_goal = data.data
            rospy.loginfo("New goal received: %s" % data.data)

if __name__ == '__main__':
    try:
        goal_subscriber = GoalSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass