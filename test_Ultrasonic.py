from Sensors.Ultrasonic.Ultrasonic import UltraSonic


sensor = UltraSonic(17, 18)

try:
    # Repeat the next indented block forever
    while True:
        distance = sensor.MeasureDistance()
        print("Distance: %.1f cm" % float(distance))

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    sensor.CleanUltrasonicPins()
