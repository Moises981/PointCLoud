#include <ros/ros.h>                  //Libreria ros
#include <sensor_msgs/JointState.h>   //Usar message JointState
#include <std_msgs/Int16.h>           //Usar message Int32 

float radian; //Variable de intercambio entre el subscriber y publisher
void callback(const std_msgs::Int16::ConstPtr &msg){    //Llamada al subscriber
    radian=(msg->data*0.0175)-1.58;                     //Convertir el valor del angulo ofrecido por el subscriber
}

int main(int argc , char** argv){
    ros::init(argc,argv,"converter");                   
    ros::NodeHandle nh;                                
    ros::Subscriber sub=nh.subscribe("/angles",1000,callback);       
    ros::Publisher pub=nh.advertise<sensor_msgs::JointState>("joint_states",1000);
    sensor_msgs::JointState msg;
    msg.position.push_back(0);   //Agregar un elemento a la lista position
    msg.name.push_back("sub_to_eje"); //Agregar texto a la lista name
    
    while(ros::ok()){
        ros::Time begin=ros::Time::now(); //Guardar tiempo de ros en begin
        msg.header.stamp.sec=begin.sec+2; //Guardar tiempo de ros en secs , es +2 para dar duracion al movimiento
        msg.position[0]=radian;  //Guardar el valor de radian 
        pub.publish(msg);        //Publicar los valores anteriores
        ros::spinOnce();      
    }
    return 0;
}
