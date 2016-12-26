from Movement.Moves import BasicMoves
import time
import sys
sys.path.append('../')

# test script - for Movement component
vecMoves = BasicMoves(10, 7, 9, 8)

vecMoves.forward(100, 100)
time.sleep(3)

vecMoves.forward(50, 100)
time.sleep(3)

vecMoves.forward(100, 50)
time.sleep(3)

vecMoves.forward(75, 75)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.backward(100, 100)
time.sleep(3)

vecMoves.backward(50, 100)
time.sleep(3)

vecMoves.backward(100, 50)
time.sleep(3)

vecMoves.backward(75, 75)
time.sleep(3)

vecMoves.stop()
time.sleep(3)

vecMoves.CleanUpPinSignal()
