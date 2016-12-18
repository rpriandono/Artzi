from Movement.Moves import BasicMoves
import time

# test script - for Movement component
vecMoves = BasicMoves(9, 8, 10, 7)

vecMoves.forward(50, 50)
time.sleep(3)

vecMoves.forward(25, 25)
time.sleep(3)

vecMoves.forward(75, 75)
time.sleep(3)

vecMoves.backward(50, 50)
time.sleep(3)

vecMoves.backward(25, 25)
time.sleep(3)

vecMoves.backward(75, 75)
time.sleep(3)

vecMoves.CleanUpPinSignal()
