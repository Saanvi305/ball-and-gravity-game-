import pgzrun,random
from random import randint
TITLE="fluffy ball"
WIDTH=600
HEIGHT=600
R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)
gravity=2000.0

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_x
        self.vx=200
        self.vy=0
        self.radius=40
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"blue")

ball1=Ball(50,100)
ball2=Ball(60,100)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

def update(dt):
    uy1=ball1.vy
    ball1.vy+=gravity*dt 
    ball1.vy+=gravity*dt 
    ball1.y+=(uy1+ball1.vy)*0.5*dt
    uy2=ball2.vy
    ball2.vy+=gravity*dt
    ball2.y+=(uy2+ball2.vy)*0.5*dt

    if ball1.y>HEIGHT-ball1.radius:
        ball1.y=HEIGHT-ball1.radius
        ball1.vy=-ball1.vy*0.9

    ball1.x +=ball1.vx*dt
    if ball1.x>WIDTH-ball1.radius or ball1.x<ball1.radius:
        ball1.vx=-ball1.vx
    #ball1
    if ball2.y>HEIGHT-ball2.radius:
         ball2.y=HEIGHT-ball2.radius
         ball2.vy=-ball2.vy*0.9

         ball2.x +=ball2.vx*dt
    if ball2.x>WIDTH-ball2.radius or ball2.x<ball2.radius:
         ball2.vx=-ball2.vx
def on_key_down(key):

    """Pressing a key will kick the ball upwards."""

    if key == keys.SPACE:

        ball1.vy = -500

        ball1.vy = -250
    

pgzrun.go()


