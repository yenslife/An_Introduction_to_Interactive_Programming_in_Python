# implementation of card game - Memory

import simplegui
import random

# global
L1 = [0, 1, 2, 3, 4, 5, 6, 7]
L2 = [0, 1, 2, 3, 4, 5, 6, 7]
L3 = L1 + L2
EXPOSED = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
C1 = -1
C2 = -1
TURNS = 0
STATE = 0

# helper function to initialize globals
def new_game():
    global L1, L2, L3, TURNS, EXPOSED, STATE, C1, C2
    # init the two lists and combine them
    random.shuffle(L3)
    TURNS = 0
    EXPOSED = [False for x in range(16)]
    STATE = 0
    C1 = -1
    C2 = -1
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global L3, STATE, C1, C2, TURNS
    x = pos[0]
    y = pos[1]

    if STATE == 0 and EXPOSED[x // 50] != True:
        #record the card 1 number
        C1 = x // 50
        EXPOSED[C1] = True
        TURNS += 1
        STATE = 1
    elif STATE == 1 and EXPOSED[x // 50] != True:
        #record the card 2 number
        C2 = x // 50
        EXPOSED[C2] = True
        STATE = 2
    elif EXPOSED[x // 50] != True:
        TURNS += 1
        # check
        if L3[C1] != L3[C2]:
            EXPOSED[C1] = False
            EXPOSED[C2] = False
        #record the card 1 number
        C1 = x // 50
        EXPOSED[C1] = True
        STATE = 1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global L3, EXPOSED, STATE, TURNS, C1, C2
    for i in range(16):
        canvas.draw_text(str(L3[i]), [i * 50 + 12 , 70], 50, "White")
        if not EXPOSED[i]:
            canvas.draw_polygon([(i * 50, 0), (i * 50 + 50, 0), (i * 50 + 50, 100), (i * 50, 100)], 5, 'Blue', 'Green')
    label.set_text("Turns = " + str(TURNS))    
       


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(TURNS))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
