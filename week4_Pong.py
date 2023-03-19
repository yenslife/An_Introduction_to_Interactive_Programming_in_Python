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
LEFT = False
RIGHT = True
PAD_MOVE_SPEED = 3
BALL_COLOR = ['red', 'orange', 'yellow', 'lime', 'blue', 'Fuchsia']
BALL_COLOR_COUNTER = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2 , HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60, random.randrange(60, 180) / 60 ]
    else:
        ball_vel = [-1 * random.randrange(120, 240) / 60, random.randrange(60, 180) / 60 ]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global up_down, BALL_COLOR_COUNTER # my additional global var
    up_down = False
    paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global up_down, BALL_COLOR_COUNTER # my additional global var
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "red")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "yellow")
        
    # update ball
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1] * (1 if up_down else -1)
    
    # touch the up and bottom
    if ball_pos[1] < 0 + BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        up_down = not up_down
        BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, BALL_RADIUS, BALL_COLOR[BALL_COLOR_COUNTER], BALL_COLOR[BALL_COLOR_COUNTER])
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos] , [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT] , PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos] , [WIDTH - HALF_PAD_WIDTH , paddle2_pos + PAD_HEIGHT] , PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide 
    if (ball_pos[0] < 0 + BALL_RADIUS):
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] *= -1.1 # increase 10 %
            BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
        else:
            spawn_ball(RIGHT)
            score1 += 1
            BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
            
    elif (ball_pos[0] > WIDTH - BALL_RADIUS):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] *= -1.1
            BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
        else:
            spawn_ball(LEFT)
            score2 += 1
            BALL_COLOR_COUNTER = (BALL_COLOR_COUNTER + 1) % len(BALL_COLOR)
            
    # draw scores
    canvas.draw_text(str(score1), [WIDTH - 100, 80], 50, 'white')
    canvas.draw_text(str(score2), [100, 80], 50, 'white')
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_MOVE_SPEED
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_MOVE_SPEED
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_MOVE_SPEED
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_MOVE_SPEED
    

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_btn = frame.add_button("Restart", new_game, 200)


# start frame
new_game()
frame.start()

