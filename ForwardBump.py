from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "ForwardBumpFunction")

left = Motor(Port.A)
right = Motor(Port.D)

SPEED = 360
REFRESH = 10000

left.run(SPEED)
right.run(SPEED)

while True: 
    pressed = ev3.buttons.pressed()
    if pressed:
        left.run(0)
        right.run(0)
    else: 
        left.run(SPEED)
        right.run(SPEED)