# Artzi
Vehicle robotics code for automated vehicle

Artzi is a simulation model robot for Automated vehicle.
It contains with several components.

Movement:
A component contains with BasicMoves class that defines the vehicle movement.
the BasicMoves class act as the Hardware Software interface because it basically control the wheel rotation.
the basic movement are forward

Sensors:
A componenet represents the Hw sensor attached to the robot.
it contains Sensor class that uses the Cooperative inheritance all the sensor class avaliable.
at the moments only two type of sensors are attached i.e. Infra Red and Ultrasonic
This component can be expand if you'd like to add another sensor in the future

Algorithms:
a Componenet represents collection of algorithms.
it contains algorithm class that uses the Cooperative inheritance all the Algorithm class avaliable.
Similar like Sensor component, the Algorithms component also can be expand with another algorithms in the future.

Communication:
a components that was design to collect all communication purposes in the future.

Controller:
The components contains the main controller of the Program.
it basicly the component that glues all the components together.
this is where all the components interact with each other.