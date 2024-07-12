#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import random

def publish_empty_trays():
    # Initialize the ROS node
    rospy.init_node('empty_trays_publisher', anonymous=True)

    # Create a publisher for the empty trays topic
    pub = rospy.Publisher('/argHRI/emptyTrays', Int32, queue_size=10)

    # Set the publishing rate (in Hz)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # Generate a random integer between 0 and 4
        empty_trays = random.randint(0, 4)

        # Publish the empty trays value
        pub.publish(empty_trays)

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_empty_trays()
    except rospy.ROSInterruptException:
        pass