from IR.IR import InfraRed
from Ultrasonic.Ultrasonic import UltraSonic
import RPi.GPIO as GPIO


class Sensor(InfraRed, UltraSonic):
    """
       The Sensor class inherits All the Hw sensor class on the robot.
       For examples:
         --> DistanceSensor = Sensor(USTriggerPin=17, USEchoPin=18)
           Declare an object as Ultrasonic sensor.

         --> LineTracker1 = Sensor(PinIR=25)
           Declare an object as Infra Red sensor.
    """

    def __init__(self, PinIR=0, USTriggerPin=0, USEchoPin=0):
        super(Sensor, self).__init__(PinIR=PinIR,
                                     USTriggerPin=USTriggerPin,
                                     USEchoPin=USEchoPin)

        if PinIR == 0 and USTriggerPin == 0 and USEchoPin == 0:
            print "WARNING: No Sensors object declared."

    def CleanGPIOPins(self):
        GPIO.cleanup()
        print "All GPIO pins are Cleaned!"
