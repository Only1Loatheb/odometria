from math import atan2, pi, sqrt, cos, sin
class Odometry():
    def __init__(self,p,r,d):
        self.position = p
        self.wheel_r = r
        self.track_d = d
    def getPosition(self):
        return self.position
    def distance(self, t):
        return sqrt( (self.position[0] - t[0]) * (self.position[0] - t[0]) + (self.position[1] - t[1]) * (self.position[1] - t[1]))
    def close(self, t, d):
        return self.distance(t) < d
    def angle(self, t):
        d = self.distance(t)
        x = t[0] -  self.position[0]
        y = t[1] -  self.position[1]
        sin = y/d
        cos = x/d
        angleDif =  self.position[2] - atan2(sin,cos)
        if angleDif > pi:
                angleDif = angleDif - 2*pi
        elif angleDif < -pi:
                angleDif = angleDif + 2*pi
        return angleDif 
    def goodDirection(self, t, a):
        return abs(self.angle(t)) < a
    def update(self, d):
        dTheta = self.wheel_r * (- d[0] + d[1]) / self.track_d 
        self.position[0] = self.position[0] + self.wheel_r * (d[0] + d[1]) * cos(self.position[2] + dTheta / 2) / 2 
        self.position[1] = self.position[1] + self.wheel_r * (d[0] + d[1]) * sin(self.position[2] + dTheta / 2) / 2
        self.position[2] = (self.position[2] + dTheta)
        if self.position[2] > pi:
        	self.position[2] = self.position[2] - 2*pi
        elif self.position[2] < -pi:
        	self.position[2] = self.position[2] + 2*pi   
       
