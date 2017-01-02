# Artzi
Artzi is a prototype simulation robot for an Automated vehicle. The software architecture contains several components. The components are segregated based on its functionality.

###Movement: 
A component that defines the vehicle movement. The BasicMoves class acts as the Hardware Software Interface because it controls wheels rotation. The basic movements are forward, backward, rotate left/right, and stop.

###Sensors: 
A component represents the hardware sensor attached to the robot. It contains Sensor class that uses the Cooperative inheritance all the sensor class available. Only two type of sensors that are currently attached i.e. Infra Red and Ultrasonic. This component can be expanded for another sensor in the future (e.g. Camera).

###Algorithms: 
A component that represents a collection of algorithms. It uses the information from the sensor as input. It contains algorithm class that uses the Cooperative inheritance all the Algorithm class available. Similar to Sensor component, the Algorithms component also can be expanded with another algorithm in the future (e.g. Image processing).

###Communication: 
A component that was designed to represent communication purposes (i.e. IEEE wave model, ETSI model). This component still under development

###Controller: 
The component that contains the main controller of the Program. It basically the component that glues all the components together because it is where all the components are interact with each other.

Below is the software class diagram;
![artzi-uml](https://cloud.githubusercontent.com/assets/5297983/21596923/a44f496c-d142-11e6-95fd-296c588c1c99.png)
