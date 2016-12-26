class LFalgorithm(object):
    """LFalgorithm class represent the Line Follower Algorithm
    It requires min 2 IR Sensors to control the DC motors

    example: Algorithm = LFalgorithm(LineFollower=True)
    """

    def __init__(self, LineFollower=False, **book):
        if LineFollower:
            super(LFalgorithm, self).__init__(**book)

    def LFcalculation(self, sensor1, sensor2):
        """ The LFCalculation method defines the DC motor action
        sensor1 represents the right IR sensor
        sensor2 represents the left IR sensor

        example: object.LFcalculation(variable1, variable2)
        """
        if sensor1 == 1 and sensor2 == 1:
            return 40, 40
        elif sensor1 == 0 and sensor2 == 1:
            return 100, 0
        elif sensor1 == 1 and sensor2 == 0:
            return 0, 100
        elif sensor1 == 0 and sensor2 == 0:
            return 0, 0
        else:
            print "ERROR: Unknown condition"
