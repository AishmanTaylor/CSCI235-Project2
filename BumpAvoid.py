#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, TouchSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "BumpAvoid")

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_bumper = TouchSensor(Port.S1)
right_bumper = TouchSensor(Port.S4)


SPEED = 360

while True: 
    if ( not left_bumper.pressed() or not right_bumper.pressed()): 
        left_motor.run(SPEED)
        right_motor.run(SPEED)
    elif left_bumper.pressed():
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(-SPEED)
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(SPEED)
    elif right_bumper.pressed():
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(-SPEED)
        for x in range(0,1000):
            left_motor.run(SPEED)
            right_motor.run(-SPEED)