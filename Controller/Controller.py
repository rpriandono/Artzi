from Movement.Moves import BasicMoves
from Sensors.Sensors import Sensor
from Algorithms.Algorithm import Algorithm
import time
import threading
import sys
sys.path.append('../')


class Controller(threading.Thread):
    """Controller class is the robot main controller.
    It can run max 4 pararel processes (due to the Rasp Pi quad core)
    It has optional Mutex variable as exchange variable between threads
    This is where all components interacts with eachother.

    example:
            IRThread = Controller(thread1="Combine IR process", Mutex=Mutex)
            USThread = Controller(thread2="Ultrasonic process", Mutex=Mutex)
            Motorthread = Controller(thread3="DC Motor process", Mutex=Mutex)
    """

    def __init__(self, thread1=0, thread2=0, thread3=0, thread4=0, Mutex=[], **book):
        super(Controller, self).__init__(**book)
        # Ultrasonic Sensor
        self.Ultrasonic = Sensor(USTriggerPin=17, USEchoPin=18)

        # IR Sensor - Right wheel
        self.IRright = Sensor(PinIR=23)

        # IR Sensor - left wheel
        self.IRleft = Sensor(PinIR=25)

        # DC Motor movement
        self.vecMoves = BasicMoves(10, 7, 9, 8)

        # Threading
        self.Thread1 = thread1
        self.Thread2 = thread2
        self.Thread3 = thread3
        self.Thread4 = thread4
        self.run_event = threading.Event()
        self.run_event.set()
        self.Mutex = Mutex

    def run(self):
        if self.Thread1:
            self.thread1(self.Mutex)
        elif self.Thread2:
            self.thread2(self.Mutex)
        elif self.Thread3:
            self.thread3(self.Mutex)
        elif self.Thread4:
            self.thread4(self.Mutex)
        else:
            print "ERROR: Unknown thread ID proccess fail to start."

    def thread1(self, Mutex):
        while self.run_event.is_set():
            Mutex[0] = self.IRright.StatusRead()
            Mutex[1] = self.IRleft.StatusRead()
            time.sleep(0.01)

    def thread2(self, Mutex):
        while self.run_event.is_set():
            Mutex[2] = self.Ultrasonic.MeasureDistance()
            time.sleep(0.5)

    def thread3(self, Mutex):
        Algo1 = Algorithm(LineFollower=True)
        Algo2 = Algorithm(ObstacleAvoidance=True)

        while self.run_event.is_set():
            print Mutex[0], ",", Mutex[1], ",", Mutex[2]
            if Algo2.OAcalculation(Mutex[2]):
                self.vecMoves.stop()
            else:
                DCmotorA, DCmotorB = Algo1.LFcalculation(Mutex[0], Mutex[1])
                self.vecMoves.forward(DCmotorA, DCmotorB)
            time.sleep(0.01)

    def thread4(self, Mutex):
        print "Process4"
