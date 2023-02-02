import time
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "BumpAvoid")

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_bumper = TouchSensor(Port.S1)
right_bumper = TouchSensor(Port.S4)


SPEED = 360
left_motor.run(SPEED)
right_motor.run(SPEED)

while True: 
    pressed = ev3.buttons.pressed()
    if left_motor.pressed:
        left_bumper.run(0)
        right_bumper.run(SPEED)
        time.wait(5)
    if right_motor.pressed:
        left_bumper.run(SPEED)
        right_bumper.run(0)
        time.wait(5)