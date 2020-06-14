#!/usr/bin/env python3.7

## Prints messages that are being published to observation topics
#  @package scripts

from konenako.msg import observation, qr_observation, observation_list, qr_observation_list
from std_msgs.msg import String

import rospy


## Subscribes to topics and leaves node to spin
def run():
    print("Printer running")

    rospy.init_node("printer")
    rospy.Subscriber("object_detector/observations", observation_list, print)
    rospy.Subscriber("qr_detector/observations", qr_observation_list, print)

    rospy.spin()


if __name__ == "__main__":
    run()
