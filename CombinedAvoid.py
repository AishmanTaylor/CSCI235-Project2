#!/usr/bin/env pybricks-micropython
#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)
                 
ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "CombinedAvoid")

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_bumper = TouchSensor(Port.S1)
right_bumper = TouchSensor(Port.S4)
ev3sonar = UltrasonicSensor(Port.S2)

SPEED = 360
left_motor.run(SPEED)
right_motor.run(SPEED)

while True:    
    if (not ev3sonar.distance < 75 or not left_bumper.pressed() or not right_bumper.pressed()):
        left_motor.run(SPEED)
        right_motor.run(SPEED)  
    elif ev3sonar.distance < 75 and left_bumper.pressed():
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(-SPEED)
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(SPEED)
    elif ev3sonar.distance() < 75 and right_bumper.pressed():
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(-SPEED)
        for x in range(0,1000):
            left_motor.run(-SPEED)
            right_motor.run(SPEED)
    else: 
        left_motor.run(SPEED)
        right_motor.run(SPEED)  
