from LineFollower.LineFollower import LFalgorithm
from ObstacleAvoidance.ObstacleAvoidance import OAalgorithm


class Algorithm(LFalgorithm, OAalgorithm):
    """The Algorithm class acts as an interface for Alogirithm
        it inherits all the class on Algorithms components
        Therefore, it can be expand to add future algorithms.

        example:
        object1 = Algorithm(LineFollower=True)
        object2 = Algorithm(ObstacleAvoidance=True)
    """

    def __init__(self, ObstacleAvoidance=False, LineFollower=False):
        super(Algorithm, self).__init__(
            ObstacleAvoidance=ObstacleAvoidance, LineFollower=LineFollower)
