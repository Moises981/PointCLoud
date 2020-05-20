# PointCLoud
## Installation's steps:
First it's important to compile the packages.
```bash
catkin_make
```
```bash
source devel/setup.bash
```
Now we have to upload the skectch of arduino named ROS_PUB.

Once uploaded the sketch , we have to launch the main.launch located in the rviz_visual package
Copy this command in your terminal:

```bash
roslaunch rviz_visual main.launch
```
After that we'll see the RVIZ interface and the pointcloud.

![v](https://user-images.githubusercontent.com/59718261/82404194-437e3200-9a26-11ea-81c3-c2d63f6abe14.gif)

Then we can accumulate the pointcloud while the servo is rotating , we will send 180 messages by each degree.
To use the laser_assemble we have to put this in the terminal , but don' forget to put the following command everytime you use a new terminal.
```bash
source devel/setup.bash
```
Then we call to the service assemble_scans2 with the following command:
```bash
roslaunch function_laser get_cloud.launch
```
After that we have to change the topic of the pointcloud for "/cloud_data".
![vs](https://user-images.githubusercontent.com/59718261/82404375-c1dad400-9a26-11ea-9130-cf5b894460ac.gif)
Now we can see the points that we generate when the servo of the robot was rotating.

## Notes:
Previously I had a PointCloud2 publisher we a lot of bugs , I couldn't control the points for that I create a list we the values in float32 (value 7).
When you launch a laser_assemble service server you should have a fixed_frame of reference , maybe the base_link.




