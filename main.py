from pygame import *
from pygame.locals import *
import sys

init()

screen = display.set_mode((800, 600))
display.set_caption('Hola mundo!')
background_color = (30,46,222)

while True:

    for ev in event.get():
        if ev.type == quit:
            quit()
            sys.exit()

        screen.fill(background_color)

        display.flip()