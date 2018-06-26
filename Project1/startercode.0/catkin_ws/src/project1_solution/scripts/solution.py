#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts


def callback(data):
	msg = Int16(data.a + data.b)
	rospy.loginfo(str(data.a) + " and " + str(data.b)+"="+str(msg))
	pub.publish(msg)
	#print str(msg)
   

def listener():
	
	rospy.init_node('listener', anonymous=True)

	global pub
	pub = rospy.Publisher("sum", Int16, queue_size=10)
	rospy.Subscriber("two_ints", TwoInts, callback)
    
	rospy.spin()




if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

