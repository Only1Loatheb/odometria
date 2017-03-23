import ev3dev.ev3 as ev3
class Controller():
    def __init__(self):
        self.speed = 300
        self.turnSpeed = 100
        self.ts = ev3.TouchSensor()
        self.lm = ev3.LargeMotor('outA')
        self.rm = ev3.LargeMotor('outB')
        self.prevLmPosition = self.lm.position()
        self.prevRmPosition = self.rm.position()        
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
        if a < 0:
            self.rm.run_forever(speed_sp=self.turnSpeed)
            self.lm.run_forever(speed_sp=-self.turnSpeed)
    def getDeltaPhis(self):
        newLmPosition = self.lm.position()
        newRmPosition = self.rm.position()
        deltaLm = self.prevLmPosition - newLmPosition
        deltaRm = self.prevRmPosition - newRmPosition
        self.prevLmPosition = newLmPosition
        self.prevRmPosition = newRmPosition
        return [deltaLm, deltaRm]