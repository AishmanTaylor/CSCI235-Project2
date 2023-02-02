import time
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)

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
    if ev3sonar.distance < 10:
        left_motor.run(SPEED)
        right_motor.run(0)
        time.wait(5)
