from pygame import *
from pygame.locals import *
import sys

init()

class Robot:
    speed = 2
    pictures = ['robot_r01.png', 'robot_r02.png','robot_r03.png','robot_r04.png',]

    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)

        self.frame_act = 0
        self.num_frames = len(self.frames)

       # self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in sel.pictures]  

    def change_frame(self):
        self.frame_act += 1
        if self.frame_act == self.num_frames:
            self.frame_act = 0
        
    def go_up(self):
        self.y = max(0, self.y - self.speed)
        self.change_frame()

    def go_down(self):
        self.y = min(600, self.y + self.speed)
        self.change_frame()

    def go_left(self):
        self.x = max(0, self.x - self.speed)
        self.change_frame()

    def go_right(self):
        self.x = min(800, self.x + self.speed)
        self.change_frame()

    @property
    def position(self):
        return self.x ,self.y

    @property
    def image(self):
        return self.frames[self.frame_act]


screen = display.set_mode((800, 600))
display.set_caption('Hola mundo!')
background_color = (150,150,222)
clock = time.Clock()

robot = Robot(400,300)

while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                robot.go_up()
            if ev.key == K_DOWN:
                robot.go_down()
            if ev.key == K_LEFT:              
                robot.go_left()
            if ev.key == K_RIGHT:
                robot.go_right()


    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        robot.go_up()
    if keys_pressed[K_DOWN]:
        robot.go_down()
    if keys_pressed[K_LEFT]:
        robot.go_left()
    if keys_pressed[K_RIGHT]:
        robot.go_right()

    


    screen.fill(background_color)
    screen.blit(robot.image,robot.position)


    display.flip()