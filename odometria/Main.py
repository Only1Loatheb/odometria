#!/usr/bin/env python3
from Map import Map
from Controller import Controller
from Odometry import Odometry
from Timer import Timer
from ev3dev import ev3
RUNNING_STRAIGHT = 0
TAKING_TURN = 1
WHEEL_RADIUS = 2.7 #TO_DO
TRACK_DISTANCE = 15 #TO_DO
TIME = 0.5
#x,y,theta
STARTING_POSITION = [0,0,2]
ts = ev3.TouchSensor()
m = Map()
c = Controller()

o = Odometry(STARTING_POSITION,WHEEL_RADIUS,TRACK_DISTANCE)	
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
    elif state == TAKING_TURN: 
        o.update(c.getDeltaPhis())
        if not o.goodDirection(target): 
            c.rotate(o.angle(target))
        else:
            c.stop()
            state = RUNNING_STRAIGHT
    if ts.value():
        break
    print(o.position)
    t.sleep()
