from Controller.Controller import Controller
import RPi.GPIO as GPIO
import time


def main():
    """
    Mutex variable Mutex[0]-> right IR sensor,
    Mutex[1]-> left IR sensor, and Mutex[2]-> Ultrasonic sensor
    """
    Mutex = [-1, -1, -1]

    IRThread = Controller(thread1="Combine IR process", Mutex=Mutex)
    USThread = Controller(thread2="Ultrasonic process", Mutex=Mutex)
    Motorthread = Controller(thread3="DC Motor process", Mutex=Mutex)
    # FutureThread = Controller(thread4="OtherProcess", Mutex=Mutex)

    IRThread.start()
    USThread.start()
    Motorthread.start()

    try:
        while 1:
            time.sleep(0.1)
    except KeyboardInterrupt:

        # required to stop the run event threads
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