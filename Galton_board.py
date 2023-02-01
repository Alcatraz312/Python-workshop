import pygame as pg
import pymunk.pygame_util as pym
pym.positive_y_is_up = False
from sys import exit
from random import randrange
import pymunk

#initilising pygame
pg.init()

#setting the screen
sc_l=700
sc_b=700
sc=pg.display.set_mode((sc_l,sc_b))
draw_option =pym.DrawOptions(sc)#making drawing option for pymunk on pygame
pg.display.set_caption("Galton Board Simulation")

#creating space for rendering physics objects
space=pymunk.Space()
space.gravity=(0,1000)

#making game time
clock=pg.time.Clock()

# variable for running
run=True

#ball class
def create_ball(x,y):
    mass=1
    radius=6
    moment=pymunk.moment_for_circle(mass,0,radius)
    body=pymunk.Body(mass,moment)
    body.position=(x,y)
    shape=pymunk.Circle(body,radius)
    #shape.color=pg.color.THECOLORS['blue']
    shape.elasticity=0.8
    shape.friction = 0.5
    space.add(body,shape)

def create_segment(st,ed):
    shape=pymunk.Segment(space.static_body,st,ed,5)
    shape.friction=0.5
    space.add(shape)

def create_peg(x,y):
    peg_shape=pymunk.Circle(space.static_body,radius=10,offset=(x,y))
    # peg_mass=1
    # peg_moment=pymunk.moment_for_circle(peg_mass,0,10)
    # peg_body=pymunk.Body(peg_mass,peg_moment)

    peg_shape.color =pg.color.THECOLORS['red'] 
    peg_shape.elasticity = 0.1
    peg_shape.friction = 0.5
    space.add(peg_shape)

# creating the upper part
create_segment((5,5),(5,50))
create_segment((sc_b-5,5),(sc_b-5,50))
create_segment((5,50),(250,100))
create_segment((sc_b-5,50),(sc_b-250,100))
# create_segment((330,100),(330,120))
# create_segment((sc_b-330,100),(sc_b-330,120))
create_segment((0,sc_l),(sc_b,sc_l))

#Creating peges
p_x=0
p_y=150
st=60
for l in range(7):
    if(l % 2 == 0):
        p_x=-20
    else:
        p_x=-10
    for p in range(16):
        p_x+=50
        create_peg(p_x,p_y)
        if(l == 6):
            create_segment((p_x,p_y+80),(p_x,sc_l))
    p_y+=40


while run :
    sc.fill('black')
    for event in pg.event.get():
        if(event.type  == pg.QUIT):
            exit()
        if(event.type == pg.MOUSEBUTTONDOWN):
            x,y=pg.mouse.get_pos()
            create_ball(x,y)
    key=pg.key.get_pressed()
    if(key[pg.K_SPACE]):
        for x in range(50):
            create_ball(randrange(10,sc_b-10),randrange(10,50))

    space.step(1/60)
    space.debug_draw(draw_option)
    pg.display.update()

    clock.tick(60)

