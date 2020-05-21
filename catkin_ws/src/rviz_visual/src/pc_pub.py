#! /usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2 , PointField
from sensor_msgs import point_cloud2
import struct
import numpy as np
from std_msgs.msg import Header , Int16

class Publisher_pointcloud(object):

    def __init__(self):
        rospy.init_node("PC")
        self._pub=rospy.Publisher("PointCloud",PointCloud2,queue_size=1)
        self._sub=rospy.Subscriber("/angles",Int16,self.callback)
        self.angle=Int16()
        self.data=PointCloud2()
        self.once=True
                

    def callback(self,msg):
        self.angle=msg

    def launch(self):

        if self.once:
            self.prev_val=self.angle.data
            self.once=False
            print "once"

        if self.angle.data != self.prev_val:
            self.prev_val=self.angle.data
            num=20
            axis=4
            distance=0.1
            points=[]
            
            mult=0.0025
            for i in range(1,num):
                mult=0.0025
                for j in range(1,40): 
                    x=-i*distance
                    z=i*mult*j ##
                    _list=[x,0,z]
                    points.append(_list)

                mult=0.0025
                for k in range(1,40): 
                    x=i*distance
                    z=i*mult*k ##
                    _list=[x,0,z]
                    points.append(_list)

                mult=0.0025
                for l in range(1,40): 
                    x=-i*distance
                    z=-i*mult*l ##
                    _list=[x,0,z]
                    points.append(_list)

                mult=0.0025
                for m in range(1,40): 
                    x=i*distance
                    z=-i*mult*m ##
                    _list=[x,0,z]
                    points.append(_list)

                mult=0.0025
                for n in range(1,40): 
                    x=i*distance
                    z=0 ##
                    _list=[x,0,z]
                    points.append(_list)


  
               
                    



            fields = [PointField('x', 0, PointField.FLOAT32, 1),
                     PointField('y', 4, PointField.FLOAT32, 1),
                     PointField('z', 8, PointField.FLOAT32, 1),
                     ]

            
            points = np.asarray(points)
            header = Header()
            time=rospy.get_rostime()
            header.stamp.secs=time.secs
            header.frame_id = "M8_quanergy"
            pc2 = point_cloud2.create_cloud(header, fields, points)
            self._pub.publish(pc2)
        
        else:
            pass

    

if __name__=="__main__":
    topic_pub=Publisher_pointcloud()
    rate=rospy.Rate(10)

    ctrl_c=False

    def shutdownhook():
        global ctrl_c
        ctrl_c=True
        rospy.loginfo("Node cancelled")

    rospy.on_shutdown(shutdownhook)

    while not ctrl_c:
        topic_pub.launch()
        rate.sleep()