import time
from Sensors.IR.IR import InfraRed
import sys
sys.path.append('../')

sensor = InfraRed(25)

try:
    # Repeat the next indented block forever
    while True:
        # If the sensor is Low (= 0), it is above the black line
        if sensor.StatusRead() == 0:
            print('The sensor is seeing a black surface'), sensor.StatusRead()
            time.sleep(0.1)
            # If not (else), print the following
        else:
            print('The sensor is seeing a white surface'), sensor.StatusRead()
            # Wait, then do the same again
            time.sleep(0.1)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    sensor.CleanGPIOPins()
    print "GPIO cleaned"
