#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, TouchSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "ForwardBumpFunction")

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_bumper = TouchSensor(Port.S1)
right_bumper = TouchSensor(Port.S4)

SPEED = 360
while True:
    if ( not left_bumper.pressed() or not right_bumper.pressed()): 
        left_motor.run(SPEED)
        right_motor.run(SPEED)
    if (left_bumper.pressed() or right_bumper.pressed()):
        left_motor.run(0)
        right_motor.run(0)