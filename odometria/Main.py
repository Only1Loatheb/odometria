#!/usr/bin/env python3
from Map import Map
from Controller import Controller
from Odometry import Odometry
from Timer import Timer
RUNNING_STRAIGHT = 0
TAKING_TURN = 1
TIME = 0.5
#x,y,theta
STARTING_POSITION = [0,0,0]

m = Map()
c = Controller()

o = Odometry(STARTING_POSITION)	
target = m.position()
state = 0
t = Timer(TIME)
while True:
    if state == RUNNING_STRAIGHT: 
        o.update(c.getDeltaPhis())
        if (not o.close(target)) and o.goodDirection(target): 
            c.runStraight(o.distance(target))
        elif not o.close(target):
            c.stop()
            state = TAKING_TURN
        else:
            c.stop()
            target = m.position()
            state = TAKING_TURN
    if state == TAKING_TURN: 
        o.update(c.getDeltaPhis())
        if not o.goodDirection(target): 
            c.rotate(o.angle(target))
        else:
            c.stop()
            state = RUNNING_STRAIGHT
    t.sleep()
