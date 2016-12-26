class OAalgorithm(object):
    """OAalgorithm class represent the Obstacle Avoidance Algorithm
    It requires min 1 Ultrasonic sensor to measure the distance

    example: Algorithm = OAalgorithm(LineFollower=True)
    """

    def __init__(self, ObstacleAvoidance=False, **book):
        if ObstacleAvoidance:
            super(OAalgorithm, self).__init__(**book)

    def OAcalculation(self, Sensor):
        """ The OAcalculation method gives boolean value to answer
        is the object infront close enough?

        if the it's return TRUE the vehicle better be stop
        otherwise it means the object still far ahead

        example: object.OAcalculation(variable1)
        """
        if Sensor > 0.0 and Sensor <= 15.0:
            return True
        else:
            return False
