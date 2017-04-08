import ev3dev.ev3 as ev3
from math import pi
class Controller():
    def __init__(self):
        self.speed = 400
        self.turnSpeed = 100
        self.ts = ev3.TouchSensor()
        self.lm = ev3.LargeMotor('outA')
        self.rm = ev3.LargeMotor('outB')
        self.lm.reset()
        self.rm.reset()
        self.cpr = self.lm.count_per_rot
        self.prevLmPosition = self.lm.position
        self.prevRmPosition = self.rm.position        
    def runStraight(self, d): #d is distance, we can adjust speed to distance later
        self.rm.run_forever(speed_sp=self.speed)
        self.lm.run_forever(speed_sp=self.speed)
    def stop(self):
        self.rm.run_forever(speed_sp=0)
        self.lm.run_forever(speed_sp=0)
    def rotate(self,a):
        if a > 0 :
            self.rm.run_forever(speed_sp= -self.turnSpeed)
            self.lm.run_forever(speed_sp= self.turnSpeed)
        else:
            self.rm.run_forever(speed_sp=self.turnSpeed)
            self.lm.run_forever(speed_sp=-self.turnSpeed)
    def getDeltaPhis(self):
        newLmPosition = self.lm.position
        newRmPosition = self.rm.position
        deltaLm =  newLmPosition - self.prevLmPosition
        deltaRm =  newRmPosition - self.prevRmPosition
        self.prevLmPosition = newLmPosition
        self.prevRmPosition = newRmPosition
        return [2 * pi * deltaLm / self.cpr, 2 * pi * deltaRm / self.cpr]
