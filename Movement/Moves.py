import RPi.GPIO as GPIO  # Import the GPIO Library
import thread


class BasicMoves(object):
    """basic robot movement i.e.
    forward, backward, rotateLeft, rotateRight and stop
        exp: VecMoves = BasicMoves(10, 7, 9, 8)
    """

    def __init__(self, PinMotorAForward, PinMotorBForward, PinMotorABackward, PinMotorBBackward):
        super(BasicMoves, self).__init__()
        self.PinMotorAForward = PinMotorAForward
        self.PinMotorBForward = PinMotorBForward
        self.PinMotorABackward = PinMotorABackward
        self.PinMotorBBackward = PinMotorBBackward
        self.frequency = 100

        # Set the GPIO modes
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Set the GPIO Pin mode
        GPIO.setup(self.PinMotorAForward, GPIO.OUT)
        GPIO.setup(self.PinMotorBForward, GPIO.OUT)
        GPIO.setup(self.PinMotorABackward, GPIO.OUT)
        GPIO.setup(self.PinMotorBBackward, GPIO.OUT)
        self.MotorAForward = GPIO.PWM(self.PinMotorAForward, self.frequency)
        self.MotorBForward = GPIO.PWM(self.PinMotorBForward, self.frequency)
        self.MotorABackward = GPIO.PWM(self.PinMotorABackward, self.frequency)
        self.MotorBBackward = GPIO.PWM(self.PinMotorBBackward, self.frequency)

    def __MotorAFwd(self, Power):
        """ Motor A forward """
        self.MotorAForward.ChangeDutyCycle(Power)
        print "Forward, Motor A DC power: ", Power, "%"

    def __MotorBFwd(self, Power):
        """ Motor B forward """
        self.MotorBForward.ChangeDutyCycle(Power)
        print "Forward, Motor B DC power: ", Power, "%"

    def __MotorABwd(self, Power):
        """ Motor A backward"""
        self.MotorABackward.ChangeDutyCycle(Power)
        print "Backward, Motor A DC power: ", Power, "%"

    def __MotorBBwd(self, Power):
        """ Motor B backward"""
        self.MotorBBackward.ChangeDutyCycle(Power)
        print "Backward, Motor B DC power: ", Power, "%"

    def forward(self, PowerMotorA, PowerMotorB):
        """ Moves the vehicle forward and defining
        the DC power percentage 0 to 100 (full Power) on each motor.
            exp: object.forward(50,50) or object.forward(100,100)
        """
        # guard the percentage 1-100 <-- to do
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()
        self.MotorABackward.stop()
        self.MotorBBackward.stop()
        self.MotorAForward.start(PowerMotorA)
        self.MotorBForward.start(PowerMotorB)
        thread.start_new_thread(self.__MotorAFwd, (PowerMotorA, ))
        thread.start_new_thread(self.__MotorBFwd, (PowerMotorB, ))

    def backward(self, PowerMotorA, PowerMotorB):
        """ Moves the vehicle backward and defining
        the DC power percentage 0 to 100 (full Power).
            exp: object.backward(50) or object.backward(100)
        """
        # guard the percentage 1-100 <-- to do
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()

        self.MotorAForward.stop()
        self.MotorBForward.stop()
        self.MotorABackward.start(PowerMotorA)
        self.MotorBBackward.start(PowerMotorB)
        thread.start_new_thread(self.__MotorABwd, (PowerMotorA, ))
        thread.start_new_thread(self.__MotorBBwd, (PowerMotorB, ))

    def stop(self):
        """ Vehicle stop or idle.
        """
        self.MotorAForward.ChangeDutyCycle(0)
        self.MotorBForward.ChangeDutyCycle(0)
        self.MotorABackward.ChangeDutyCycle(0)
        self.MotorBBackward.ChangeDutyCycle(0)
        print "Stop, Motor A DC power: ", 0, "%"
        print "Stop, Motor B DC power: ", 0, "%"

    def rotateRight(self, PowerMotorA, PowerMotorB):
        """ rotate the robot to the right.
            requires the DC power for both motors as an input
        """
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()

        self.MotorABackward.stop()
        self.MotorBForward.stop()
        self.MotorAForward.start(PowerMotorA)
        self.MotorBBackward.start(PowerMotorB)
        thread.start_new_thread(self.__MotorAFwd, (PowerMotorA, ))
        thread.start_new_thread(self.__MotorBBwd, (PowerMotorB, ))

    def rotateLeft(self, PowerMotorA, PowerMotorB):
        """ rotate the robot to the left.
            requires the DC power for both motors as an input
        """
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()

        self.MotorAForward.stop()
        self.MotorBBackward.stop()
        self.MotorABackward.start(PowerMotorA)
        self.MotorBForward.start(PowerMotorB)
        thread.start_new_thread(self.__MotorABwd, (PowerMotorA, ))
        thread.start_new_thread(self.__MotorBFwd, (PowerMotorB, ))

    def CleanUpPinSignal(self):
        """
        this method stops the wheels rotation and cleans up the GPIO Pins
        ===== RUN THIS METHOD EVERYTIME PROGRAM IS ENDED!!! =====
        """
        GPIO.cleanup()
        print "GPIO cleaned!"
