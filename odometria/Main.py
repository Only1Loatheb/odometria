#!/usr/bin/env python3
from Map import Map
from Controller import Controller
from Odometry import Odometry
from Timer import Timer
from ev3dev import ev3
from math import pi
RUNNING_STRAIGHT = 0
TAKING_TURN = 1
WHEEL_RADIUS = 2.7 #TO_DO
TRACK_DISTANCE = 15 #TO_DO
CLOSE_DISTANCE = 2
CLOSE_ANGLE = 2 * pi / 180 # pi / 180 == 1*
TIME = 0.5
#x,y,theta
STARTING_POSITION = [0,0,pi/2]
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
        if (not o.close(target,CLOSE_DISTANCE)) and o.goodDirection(target,CLOSE_ANGLE): 
            c.runStraight(o.distance(target))
        elif not o.close(target,CLOSE_DISTANCE):
            c.stop()
            state = TAKING_TURN
        else:
            c.stop()
            target = m.position()
            state = TAKING_TURN
    elif state == TAKING_TURN: 
        o.update(c.getDeltaPhis())
        if not o.goodDirection(target,CLOSE_ANGLE): 
            c.rotate(o.angle(target))
        else:
            c.stop()
            state = RUNNING_STRAIGHT
    if ts.value():
        break
    print(o.position)
    t.sleep()
