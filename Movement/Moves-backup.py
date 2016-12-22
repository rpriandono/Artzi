import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library
import thread


class BasicMoves(object):
    """basic robot movement i.e. forward, backward, and stop
        exp: VecMoves = BasicMoves(9, 8, 10, 7)
    """

    def __init__(self, PinMotorAForward, PinMotorBForward, PinMotorABackward, PinMotorBBackward):
        super(BasicMoves, self).__init__()
        self.PinMotorAForward = PinMotorAForward
        self.PinMotorBForward = PinMotorBForward
        self.PinMotorABackward = PinMotorABackward
        self.PinMotorBBackward = PinMotorBBackward
        self.frequency = 100
        self.DCpowerA = 0
        self.DCpowerB = 0

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

    def __getDCpower(self, Motor):
        """ Get the current DC power on motor A or Motor B"""
        if Motor == "A":
            return self.DCpowerA
        elif Motor == "B":
            return self.DCpowerB
        else:
            print "ERROR: __getDCpower should be A or B"
            self.CleanUpPinSignal()
            quit()

    def __accelMotorAFwd(self, Power):
        """ Acceleration motor A forward """
        for self.DCpowerA in range(self.DCpowerA, Power + 1, 5):
            self.MotorAForward.ChangeDutyCycle(self.DCpowerA)
            print self.DCpowerA
            time.sleep(0.1)
        print "Forward Acc, Motor A DC power: ", self.__getDCpower("A"), "%"

    def __accelMotorBFwd(self, Power):
        """ Acceleration motor B forward """
        for self.DCpowerB in range(self.DCpowerB, Power + 1, 5):
            self.MotorBForward.ChangeDutyCycle(self.DCpowerB)
            print self.DCpowerB
            time.sleep(0.1)
        print "Forward Acc, Motor B DC power: ", self.__getDCpower("B"), "%"

    def __decelMotorAFwd(self, Power):
        """ Deceleration motor A forward """
        for self.DCpowerA in range(self.DCpowerA, Power - 1, -5):
            self.MotorAForward.ChangeDutyCycle(self.DCpowerA)
            print self.DCpowerA
            time.sleep(0.1)
        print "Forward Dec, Motor A DC power: ", self.__getDCpower("A"), "%"

    def __decelMotorBFwd(self, Power):
        """ Deceleration motor B forward """
        for self.DCpowerB in range(self.DCpowerB, Power - 1, -5):
            self.MotorBForward.ChangeDutyCycle(self.DCpowerB)
            print self.DCpowerB
            time.sleep(0.1)
        print "Forward Dec, Motor B DC power: ", self.__getDCpower("B"), "%"

    def __accelMotorABwd(self, Power):
        """ Acceleration motor A backward"""
        for self.DCpowerA in range(self.DCpowerA, Power + 1, 5):
            self.MotorABackward.ChangeDutyCycle(self.DCpowerA)
            print self.DCpowerA
            time.sleep(0.1)
        print "Backward Acc, Motor A DC power: ", self.__getDCpower("A"), "%"

    def __accelMotorBBwd(self, Power):
        """ Acceleration motor B backward"""
        for self.DCpowerB in range(self.DCpowerB, Power + 1, 5):
            self.MotorBBackward.ChangeDutyCycle(self.DCpowerB)
            print self.DCpowerB
            time.sleep(0.1)
        print "Backward Acc, Motor B DC power: ", self.__getDCpower("B"), "%"

    def __decelMotorABwd(self, Power):
        """ Deceleration motor A backward"""
        for self.DCpowerA in range(self.DCpowerA, Power - 1, -5):
            self.MotorABackward.ChangeDutyCycle(self.DCpowerA)
            print self.DCpowerA
            time.sleep(0.1)
        print "Backward Dec, Motor A DC power: ", self.__getDCpower("A"), "%"

    def __decelMotorBBwd(self, Power):
        """ Deceleration motor B backward"""
        for self.DCpowerB in range(self.DCpowerB, Power - 1, -5):
            self.MotorBBackward.ChangeDutyCycle(self.DCpowerB)
            print self.DCpowerB
            time.sleep(0.1)
        print "Backward Dec, Motor B DC power: ", self.__getDCpower("B"), "%"

    def forward(self, PowerMotorA, PowerMotorB):
        """ Moves the vehicle forward and defining the DC power percentage 0 to 100 (full Power) on each motor.
            exp: object.forward(50,50) or object.forward(100,100)
        """
        # guard the percentage 1-100 <-- to do
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()
        self.MotorABackward.stop()
        self.MotorBBackward.stop()
        self.MotorAForward.start(self.DCpowerA)
        self.MotorBForward.start(self.DCpowerB)

        if self.DCpowerA <= PowerMotorA and self.DCpowerB <= PowerMotorB:
            thread.start_new_thread(self.__accelMotorAFwd, (PowerMotorA, ))
            thread.start_new_thread(self.__accelMotorBFwd, (PowerMotorB, ))
        elif self.DCpowerA >= PowerMotorA and self.DCpowerB <= PowerMotorB:
            thread.start_new_thread(self.__decelMotorAFwd, (PowerMotorA, ))
            thread.start_new_thread(self.__accelMotorBFwd, (PowerMotorB, ))
        elif self.DCpowerA <= PowerMotorA and self.DCpowerB >= PowerMotorB:
            thread.start_new_thread(self.__accelMotorAFwd, (PowerMotorA, ))
            thread.start_new_thread(self.__decelMotorBFwd, (PowerMotorB, ))
        else:
            thread.start_new_thread(self.__decelMotorAFwd, (PowerMotorA, ))
            thread.start_new_thread(self.__decelMotorBFwd, (PowerMotorB, ))

    def backward(self, PowerMotorA, PowerMotorB):
        """ Moves the vehicle backward and defining the DC power percentage 0 to 100 (full Power).
            exp: object.backward(50) or object.backward(100)
        """
        # guard the percentage 1-100 <-- to do
        if PowerMotorA < 0 or PowerMotorA > 100 or PowerMotorB < 0 or PowerMotorB > 100:
            print "ERROR: Power usage should be between 0 to 100%"
            self.CleanUpPinSignal()
            quit()

        self.MotorAForward.stop()
        self.MotorBForward.stop()
        self.MotorABackward.start(self.DCpowerA)
        self.MotorBBackward.start(self.DCpowerB)

        if self.DCpowerA <= PowerMotorA and self.DCpowerB <= PowerMotorB:
            thread.start_new_thread(self.__accelMotorABwd, (PowerMotorA, ))
            thread.start_new_thread(self.__accelMotorBBwd, (PowerMotorB, ))
        elif self.DCpowerA >= PowerMotorA and self.DCpowerB <= PowerMotorB:
            thread.start_new_thread(self.__decelMotorABwd, (PowerMotorA, ))
            thread.start_new_thread(self.__accelMotorBBwd, (PowerMotorB, ))
        elif self.DCpowerA <= PowerMotorA and self.DCpowerB >= PowerMotorB:
            thread.start_new_thread(self.__accelMotorABwd, (PowerMotorA, ))
            thread.start_new_thread(self.__decelMotorBBwd, (PowerMotorB, ))
        else:
            thread.start_new_thread(self.__decelMotorABwd, (PowerMotorA, ))
            thread.start_new_thread(self.__decelMotorBBwd, (PowerMotorB, ))

    def stop(self):
        """ Vehilce stop or idle.
        """
        self.DCpowerA = 0
        self.DCpowerB = 0
        self.MotorAForward.ChangeDutyCycle(self.DCpowerA)
        self.MotorBForward.ChangeDutyCycle(self.DCpowerB)
        self.MotorABackward.ChangeDutyCycle(self.DCpowerA)
        self.MotorBBackward.ChangeDutyCycle(self.DCpowerB)

    def CleanUpPinSignal(self):
        """ this method stops the wheels rotation and cleans up the GPIO Pins
        ===== RUN THIS METHOD EVERYTIME PROGRAM IS ENDED!!! =====
        """
        GPIO.cleanup()
        print "GPIO cleaned!"
