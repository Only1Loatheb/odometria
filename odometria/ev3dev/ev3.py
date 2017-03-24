"""fake ev3 package"""
class TouchSensor(object): 
    def __init__(self):
        print("TouchSensor constructor")
    def value(self):
        return False

class LargeMotor(object): 
    def __init__(self, n):
        self.name = n
        self.pos = 0
        self.count_per_rot = 360
        print("LargeMotor constructor on output: ",n)
    def run_forever(self, **args):
        s = args.get("speed_sp")
        self.pos = self.pos + s / 10
        print(self.name, s)
    def position(self):
        return self.pos
    def reset(self):
        print("reset")