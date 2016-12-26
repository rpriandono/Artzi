from Movement.Moves import BasicMoves
from Sensors.Sensors import Sensor
import time
import threading
import RPi.GPIO as GPIO


class Controller(threading.Thread):
    """Controller class is the robot main controller.
    It run max 4 pararel processes (due to the Rasp Pi quad core)
    """

    def __init__(self, Name, Mutex=[]):
        super(Controller, self).__init__()
        # Ultrasonic Sensor
        self.Ultrasonic = Sensor(USTriggerPin=17, USEchoPin=18)

        # IR Sensor - Right wheel
        self.IRright = Sensor(PinIR=23)

        # IR Sensor - left wheel
        self.IRleft = Sensor(PinIR=25)

        # DC Motor movement
        self.vecMoves = BasicMoves(10, 7, 9, 8)

        # Threading
        self.ThreadName = Name
        self.run_event = threading.Event()
        self.run_event.set()
        self.Mutex = Mutex

    def run(self):
        print "Starting " + self.ThreadName
        if self.ThreadName == "process1":
            self.__thread1(self.Mutex)
        elif self.ThreadName == "process2":
            self.__thread2(self.Mutex)
        elif self.ThreadName == "process3":
            self.__thread3(self.Mutex)
        elif self.ThreadName == "process4":
            self.__thread4(self.Mutex)
        else:
            print "ERROR: Unknown thread ID proccess fail to start."
        print "Exit " + self.ThreadName

    def __thread1(self, Mutex):
        while self.run_event.is_set():
            Mutex[0] = self.IRright.StatusRead()
            Mutex[1] = self.IRleft.StatusRead()
            time.sleep(0.01)

    def __thread2(self, Mutex):
        while self.run_event.is_set():
            Mutex[2] = self.Ultrasonic.MeasureDistance()
            time.sleep(0.5)

    def __thread3(self, Mutex):
        while self.run_event.is_set():
            print Mutex[0], ",", Mutex[1], ",", Mutex[2]

            if Mutex[2] <= 15.0 and Mutex[2] > 0.0:
                print "STOP!"
                self.vecMoves.stop()
            elif Mutex[0] == 1 and Mutex[1] == 1:
                print "forward"
                self.vecMoves.forward(40, 40)
            elif Mutex[0] == 0 and Mutex[1] == 1:
                print "slight right - add loop or recursive"
                self.vecMoves.forward(100, 0)
            elif Mutex[0] == 1 and Mutex[1] == 0:
                print "slight left - add loop or recursive"
                self.vecMoves.forward(0, 100)
            elif Mutex[0] == 0 and Mutex[1] == 0:
                print "STOP"
                self.vecMoves.stop()
            else:
                print "ERROR: Unknown condition"

            time.sleep(0.01)

    def __thread4(self, Mutex):
        print "Process4"


def main():

    Mutex = [-1, -1, -1]

    IRThread = Controller("process1", Mutex)
    USThread = Controller("process2", Mutex)
    Motorthread = Controller("process3", Mutex)
    # FutureThread = Controller("process4")

    IRThread.start()
    USThread.start()
    Motorthread.start()

    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        IRThread.run_event.clear()
        USThread.run_event.clear()
        Motorthread.run_event.clear()

        IRThread.join()
        USThread.join()
        Motorthread.join()

        print "threads successfully closed"
        GPIO.cleanup()
        print "GPIO cleaned!"

main()
