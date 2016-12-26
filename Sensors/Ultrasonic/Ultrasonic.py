import RPi.GPIO as GPIO
import time


class UltraSonic(object):
    """UltraSonic class define the Ultrasonic distance sensor.
       it requires the Trigger Pin and Echo Pin as an input.

       example: sensor = UltraSonic(17, 18)
    """

    def __init__(self, USTriggerPin, USEchoPin, **book):
        super(UltraSonic, self).__init__(**book)
        if USTriggerPin != 0 and USEchoPin != 0:
            # Set the GPIO modes
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            # Define GPIO pins to use on the Pi
            self.pinTrigger = USTriggerPin
            self.pinEcho = USEchoPin

            # Set pins as output and input
            GPIO.setup(self.pinTrigger, GPIO.OUT)  # Triggerd
            GPIO.setup(self.pinEcho, GPIO.IN)       # Echo

    def MeasureDistance(self):
        """ it returns the distance between
        the robot with the object infront in centimeter
        """
        # Set trigger to False (Low)
        GPIO.output(self.pinTrigger, False)

        # Allow module to settle
        time.sleep(0.1)

        # Send 10us pulse to trigger
        GPIO.output(self.pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)

        # Start the timer
        StartTime = time.time()

        # The start time is reset until the Echo pin is taken high (==1)
        while GPIO.input(self.pinEcho) == 0:
            StartTime = time.time()

        # Stop when the Echo pin is no longer high - the end time
        while GPIO.input(self.pinEcho) == 1:
            StopTime = time.time()
            # If the sensor is too close to an object, the Pi cannot
            # see the echo quickly enough, so it has to detect that
            # problem and say what has happened
            if StopTime - StartTime >= 0.04:
                StopTime = StartTime
                break

        # Calculate pulse length
        ElapsedTime = StopTime - StartTime

        # Distance pulse travelled in that time is
        # time multiplied by the speed of sound (cm/s)
        Distance = ElapsedTime * 34326

        # That was the distance there and back so halve the value
        Distance = Distance / 2
        return Distance

    def CleanGPIOPins(self):
        """ clean up the Ultrasonic Pins"""
        GPIO.cleanup()
