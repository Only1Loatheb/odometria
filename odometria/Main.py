#!/usr/bin/env python3
from Map import Map
from Controller import Controller
from Odometry import Odometry
from Timer import Timer
from ev3dev import ev3
from math import pi
RUNNING_STRAIGHT = 0
TAKING_TURN = 1
WHEEL_RADIUS = 2.7 
TRACK_DISTANCE = 16 
DRIFT_COMPENSATION = 1.04   #dla malego 100 i 9 
CLOSE_DISTANCE = 2
CLOSE_ANGLE = 0.7 * pi / 180 # pi / 180 == 1*
CLOSE_ANGLE_STRAIGHT = 5 * pi / 180
TIME = 0.1
#x,y,theta
STARTING_POSITION = [0,0,pi/2]
ts = ev3.TouchSensor()
m = Map()
c = Controller()

o = Odometry(STARTING_POSITION,WHEEL_RADIUS,TRACK_DISTANCE * DRIFT_COMPENSATION)
target = m.position()
state = 0
t = Timer(TIME)
while True:
    if state == RUNNING_STRAIGHT: 
        o.update(c.getDeltaPhis())
        if (not o.close(target,CLOSE_DISTANCE)) and o.goodDirection(target,CLOSE_ANGLE_STRAIGHT): 
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
        c.stop()
        while ts.value():
            t.sleep()
        while True:
            if ts.value():
                break
            t.sleep()
        while ts.value():
            t.sleep()	
    print(o.position)
    t.sleep()
