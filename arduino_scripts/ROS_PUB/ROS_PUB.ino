#include <ros.h>
#include <std_msgs/Int16.h>
#include<math.h>

ros::NodeHandle  nh;

std_msgs::Int16 data;
ros::Publisher pub("/angles", &data);   //Publicar datos en topico /angles


unsigned comp=0;  //Variable sin signo
int angle=0;      //Variable angle 

void setup()
{
  nh.initNode();
  nh.advertise(pub);
}

void loop()
{
  angle=angle+comp; 
  if(angle==0){  //Cuando angle llegue a 0 
    comp=+1;     //Entonces comp sera +1 para que vaya aumentando de 1 en 1
    nh.loginfo("Angulo inicial 0");
  }
  if(angle==180){ //Cuando angle llegue a 180
    comp=-1;      //Entonces comp sera -1 para decrementar hasta 0 
    nh.loginfo("Angulo final 180");
  }
  data.data= angle; //Guardar el estado de angle en el mensaje
  pub.publish( &data ); //Publicarlo
  nh.spinOnce();
  delay(200);
}
