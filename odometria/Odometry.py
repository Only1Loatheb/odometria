from math import atan2, pi, sqrt
class Odometry():
    def __init__(self,p):
        self.position = p
        self.CLOSE_DISTANCE = 10
        self.CLOSE_ANGLE = pi / 20
    def getPosition(self):
        return self.position
    def distance(self, t):
        return sqrt( (self.position[0] - t[0]) * (self.position[0] - t[0]) + (self.position[1] - t[1]) * (self.position[1] - t[1]))
    def close(self, t):
        return self.distance(t) < self.CLOSE_DISTANCE
    def angle(self, t):
        d = self.distance(t)
        x = t[0] -  self.position[0]
        y = t[1] -  self.position[1]
        sin = y/d
        cos = x/d
        return self.position[2] - atan2(sin,cos)
    def goodDirection(self, t):
        return abs(self.angle(t)) < self.CLOSE_ANGLE
    def update(self, d):
        pass