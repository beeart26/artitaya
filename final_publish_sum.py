#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def talker():
    pub = rospy.Publisher('sum_std_id', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        art_str = 32  
        rospy.loginfo(art_str)
        pub.publish(art_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
