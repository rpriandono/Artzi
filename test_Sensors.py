from Sensors.Sensors import Sensor
import time

distanceSensor = Sensor(USTriggerPin=17, USEchoPin=18)
LineTracker1 = Sensor(PinIR=25)
LineTracker2 = Sensor(PinIR=23)

try:
    # Repeat the next indented block forever
    while True:
        print "Distance: %2.f cm" % float(distanceSensor.MeasureDistance())
        print "IR-1 sensor detect an object: ", LineTracker1.StatusRead()
        print "IR-2 sensor detect an object: ", LineTracker2.StatusRead()
        time.sleep(0.1)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    distanceSensor.CleanGPIOPins()
