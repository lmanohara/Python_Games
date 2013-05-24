# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_vel = [0, 0]
ball_pos = [0, 0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    rand_vel_x = random.randrange(2,4)
    rand_vel_y = random.randrange(1,3)
    
    if(right):
        ball_vel[0] = -rand_vel_x
        ball_vel[1] = -rand_vel_y
    else:
        ball_vel[0] = rand_vel_x 
        ball_vel[1] = -rand_vel_y
    
        
# define event handlers
def init():
    ball_init(random.randrange(-1,1))
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_vel = 0.00
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if(paddle1_pos <=  PAD_HEIGHT/2):
        paddle1_pos = PAD_HEIGHT/2
    elif(paddle1_pos >= (HEIGHT-1) - PAD_HEIGHT/ 2):
        paddle1_pos = (HEIGHT-1) - PAD_HEIGHT/ 2
    elif paddle2_pos <= PAD_HEIGHT/2:
        paddle2_pos = PAD_HEIGHT/2
    elif paddle2_pos >= (HEIGHT-1) - PAD_HEIGHT/2:     
        paddle2_pos = (HEIGHT-1) - PAD_HEIGHT/2
        
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([[0,paddle1_pos - PAD_HEIGHT/2], [PAD_WIDTH, paddle1_pos - PAD_HEIGHT/2 ], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT/2], [0,paddle1_pos + PAD_HEIGHT/2]] ,1, "White", "White")
    c.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos - PAD_HEIGHT/2], [WIDTH, paddle2_pos - PAD_HEIGHT/2 ], [WIDTH, paddle2_pos + PAD_HEIGHT/2], [WIDTH - PAD_WIDTH,paddle2_pos + PAD_HEIGHT/2]] ,1, "White", "White")
   
    # update ball
    ball_pos[1] += ball_vel[1]
    ball_pos[0] += ball_vel[0]
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] =- ball_vel[1]
    elif(ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS):
        ball_vel[1] =- ball_vel[1]
    elif(ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] <= paddle1_pos +PAD_HEIGHT/2 and ball_pos[1] >= paddle1_pos - PAD_HEIGHT/2 ):
        ball_vel[0] =- (ball_vel[0] + (ball_vel[0] * 0.1))
    elif(ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        score2 += 1
        ball_init(0)
    elif(ball_pos[0] >= (WIDTH-PAD_WIDTH-1) - BALL_RADIUS and ball_pos[1] <= paddle2_pos +PAD_HEIGHT/2 and ball_pos[1] >= paddle2_pos - PAD_HEIGHT/2 ):
        ball_vel[0] =- (ball_vel[0] + (ball_vel[0] * 0.1))
    elif(ball_pos[0] >= (WIDTH-PAD_WIDTH-1) - BALL_RADIUS):
        score1 += 1
        ball_init(1)
         
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1) ,[250, 100], 30, "White" )
    c.draw_text(str(score2) ,[350, 100], 30, "White" )
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()
