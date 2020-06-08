#!/usr/bin/env python3.7
import cv2 as cv
import rospy
from numpy import ndarray
from rostest.msg import image
from image_converter import ImageConverter

source = "/dev/video0"
#source = "test.mp4"


def run():
    rospy.init_node("camera")
    converter = ImageConverter()
    # We only want to process the latest frame, and Publisher's queue is
    # FIFO (?), thus queue_size is set to 1.
    pub = rospy.Publisher("camera_feed", image, queue_size=1)
    cam = cv.VideoCapture(source)
    while cam.grab():
        img = cam.retrieve()[1]
        # Converting the image from numpy ndarray to an image message
        msg = converter.cv2_to_msg(img)
        pub.publish(msg)


if __name__ == "__main__":
    run()
    rospy.spin()
