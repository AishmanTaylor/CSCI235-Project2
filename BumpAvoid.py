from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
import time

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "BumpAvoid")

left = Motor(Port.A)
right = Motor(Port.D)

SPEED = 360
REFRESH = 10000

left.run(SPEED)
right.run(SPEED)

while True: 
    pressed = ev3.buttons.pressed()
    if left.pressed:
        left.run(0)
        right.run(SPEED)
        time.wait(5)
    if right.pressed:
        left.run(SPEED)
        right.run(0)
        time.wait(5)