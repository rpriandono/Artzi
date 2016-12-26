# Artzi
Vehicle robotics code for automated vehicle

Artzi is a simulation model robot for Automated vehicle.
It contains with several components.

Movement:
A component contains with BasicMoves class that defines the vehicle movement.
the BasicMoves class act as the Hardware Software interface because it basically controll the wheel rotation.

Sensors:
A componenet represents the Hw sensor attached to the robot.
it contains Sensor class that Cooperative inheritance all the sensor class avaliable.
at the moments only two type of sensors are attached i.e. Infra Red and Ultrasonic