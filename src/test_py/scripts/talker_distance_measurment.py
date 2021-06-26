#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    #publish to chatter topic
    pub = rospy.Publisher('chatter',String,queue_size=10)
    #infrom code's name
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(10) #10Hz

    while not rospy.is_shutdown(): # ctrl+c interrupt
        send_str = 'aisl_first_ros_test%s' % rospy.get_time()
        rospy.loginfo(send_str)
        #print on monitor, lecord in logfile

        pub.publish(send_str)   #publish to topic
        rate.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

