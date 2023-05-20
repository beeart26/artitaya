#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "   %s", data.data)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("sum_std_id", Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
