#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, UltrasonicSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "UltrasonicAvoid")

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
ev3sonar = UltrasonicSensor(Port.S2)

SPEED = 360
left_motor.run(SPEED)
right_motor.run(SPEED)

while True:
    if not ev3sonar.distance() < 75:
        left_motor.run(SPEED)
        right_motor.run(SPEED)  
    elif ev3sonar.distance() < 75:
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(-SPEED)
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(SPEED)