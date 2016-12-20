from Movement.Moves import BasicMoves
import time

"""
Straight line 		 = vecMoves(??,??)
90 degree turn right = vecMoves(??,??)
90 degree turn left  = vecMoves(??,??)

"""


# Calibration script - Forward backward
vecMoves = BasicMoves(10, 7, 9, 8)

vecMoves.forward(100, 100)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.backward(100, 100)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.CleanUpPinSignal()
