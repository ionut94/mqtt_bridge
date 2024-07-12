import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import random

# Initialise the discreete locations
def generate_locations():
    # Create a dictionary of locations
    locations = {}

    # Generate 10 random x,y coordinates and names
    for i in range(10):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        name = f"Location {i+1}"
        locations[name] = (x, y)

    return locations

def scan_callback(odom_msg):
    # Get the current position from the odometry message
    current_position = (odom_msg.pose.pose.position.x, odom_msg.pose.pose.position.y)

    # Calculate the distance between the current position and each location
    distances = {}
    for location_name, location_position in locations.items():
        location_distance = ((current_position[0] - location_position[0]) ** 2 +
                             (current_position[1] - location_position[1]) ** 2) ** 0.5
        distances[location_name] = location_distance

    # Find the closest location
    closest_location = min(distances, key=distances.get)

    # Publish the closest location on /robot_location topic
    location_pub.publish(closest_location)
    
if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('location_publisher')

    # Generate the dictionary of locations
    locations = generate_locations()
    # Print the dictionary of locations
    print(locations)

    # Create a publisher for /robot_location topic
    location_pub = rospy.Publisher('/robot_location', String, queue_size=10)

    # Subscribe to the /odom topic to get continuous location data
    rospy.Subscriber('/odom', Odometry, scan_callback)

    # Spin the node to process callbacks
    rospy.spin()