SPRITE_SIZE = 1920/80
SPRITE_FALSE_COLOR = (10,10,10)
SPRITE_TRUE_COLOR = (237, 255, 38)

with open('speed.speed',"r") as f:
    for t in f:
        s =t.strip()
        break

SPEED = int(s)