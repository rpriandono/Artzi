from Movement.Moves import BasicMoves
import time

"""
vecMoves.forward(25, 100) = 90 degree right turn
vecMoves.forward(100, 25) = 90 degree right turn

"""


# Calibration script - Forward backward
vecMoves = BasicMoves(9, 8, 10, 7)

vecMoves.forward(25, 25)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.backward(50, 50)
time.sleep(3)

vecMoves.CleanUpPinSignal()
