#!/usr/bin/env python
from sensor_msgs.msg import PointCloud2
import rospy
from laser_assembler.srv import AssembleScans2
from std_msgs.msg import Int16

    


def assembler_client():
    rospy.init_node("test_client")
    rospy.wait_for_service("assemble_scans2")
    assemble_scans = rospy.ServiceProxy('assemble_scans2', AssembleScans2)
    pub=rospy.Publisher("/data_cloud",PointCloud2,queue_size=1)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
            print "Got cloud with %u points" % len(resp.cloud.data)
            pub.publish(resp.cloud)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
            
            rate.sleep()

if __name__=="__main__":
    try:
        assembler_client()
    except rospy.ROSInterruptException:
        pass
