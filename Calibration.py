from Movement.Moves import BasicMoves
import time

# calibration script - for Movement component
vecMoves = BasicMoves(10, 7, 9, 8)

# Straight line
vecMoves.forward(50, 43)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.backward(49, 50)
time.sleep(3)

vecMoves.stop()
time.sleep(3)


#=== rotate 180 degree ===
vecMoves.rotateRight(50, 50)
time.sleep(1)

vecMoves.stop()
time.sleep(3)


#=== rotate 180 degree ===
vecMoves.rotateLeft(50, 50)
time.sleep(1)

vecMoves.stop()
time.sleep(3)

vecMoves.CleanUpPinSignal()
