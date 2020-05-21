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
![image](https://user-images.githubusercontent.com/59718261/82405401-6c53f680-9a29-11ea-82f2-09707bc74733.png)

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

## PointCLoud reduction:
We can create a topic that subscribes to our pointcloud assemble , then we can ignore some points with the variable resample , while the resample is bigget than befores , we will have less points. Lets's see that.
Open another terminal and copy the following command:
```bash
roslaunch functino_laser cloud_reduction.launch
```
Then let's change the topic of the pointcloud on rviz.
#### Resample=10:
![Peek 20-05-2020 19-09](https://user-images.githubusercontent.com/59718261/82509544-cad2b080-9acd-11ea-90c4-db3f18b08d30.gif)
#### Resample=100:
![Peek 20-05-2020 19-10](https://user-images.githubusercontent.com/59718261/82509575-e938ac00-9acd-11ea-9b11-70598d5825a4.gif)
#### Resample=1000:
![Peek 20-05-2020 19-11](https://user-images.githubusercontent.com/59718261/82509579-eccc3300-9acd-11ea-9926-a5fb22e0eb00.gif)

## Notes:
Previously I had a PointCloud2 publisher we a lot of bugs , I couldn't control the points for that I create a list we the values in float32 (value 7).
When you launch a laser_assemble service server you should have a fixed_frame of reference , maybe the base_link.
To change the value of resample you have to enter to the src folder and then open the pointcloud_reduction.py and change the value of the variable of paso_resample.




