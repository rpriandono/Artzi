import RPi.GPIO as GPIO


class InfraRed(object):
    """ A class for IR sensor.
        It gives a status if the robot above black suface or not.
        it requires a raspberry pi Pin as an input

        example: sensor1 = InfraRed(25)
        """

    def __init__(self, PinIR, **book):
        super(InfraRed, self).__init__(**book)
        if PinIR != 0:
            # Set the GPIO modes
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            # Set variables for the GPIO pins
            self.pinLineFollower = PinIR

            # Set as an input so its value can be read
            GPIO.setup(self.pinLineFollower, GPIO.IN)

    def StatusRead(self):
        """ Return the IR reading status
        when on top of Dark color matter or on top of coloured floor.
        e.g black line, black duck tape, white paper, etc.
        """
        return GPIO.input(self.pinLineFollower)

    def CleanGPIOPins(self):
        """ clean up the IR pin"""
        GPIO.cleanup()
