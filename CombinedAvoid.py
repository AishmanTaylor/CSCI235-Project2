import time
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
                 
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
    pressed = ev3.buttons.pressed()
    if ev3sonar.distance < 10:
        left_motor.run(SPEED)
        right_motor.run(0)
        time.wait(5)
    elif (ev3sonar.distance < 10 and left_bumper.pressed):
        left_motor.run(0)
        right_motor.run(SPEED)
        time.wait(5)
    elif (ev3sonar.distance < 10 and right_bumper.pressed):
        left_motor.run(SPEED)
        right_motor.run(0)
        time.wait(5)