# template for "Guess the number" mini-project

import simplegui as sg
import random
import math

# input will come from buttons and an input field
# all output for the game will be printed in the console

secret_number = 0
range_start = 0
range_end = 100
remain = 7

# helper function to start and restart the game
def new_game():
    
    print
    
    # initialize global variables used in your code here
    
    global secret_number
    global range_end
    global range_start
    global remain
    
    secret_number = random.randrange(range_start , range_end)
    remain = int(math.ceil(math.log(range_end, 2)))
    
    if range_end == 100:
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is " + str(remain)
    elif range_end == 1000:
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is " + str(remain)
    else:
        print "unexpected range"
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global range_end
    global range_start
    
    range_start = 0
    range_end = 100
    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global range_end
    global range_start
    
    range_start = 0
    range_end = 1000
    
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here
    
    print
    
    global remain
    
    try:
        guess_num = int(guess)
        print "Guess was " + guess
    except:
        print "Please Enter Number"
        return
    
    remain -= 1
    
    
    
    if guess_num > secret_number:
        print "Number of remaining guesses is " + str(remain)
        print "Lower!"
    elif guess_num < secret_number:
        print "Number of remaining guesses is " + str(remain)
        print "Higher!"
    else:
        print "Correct!"
        new_game()
        
    if remain == 0:
        print "You lose, the secret number is " + str(secret_number) + "."
        print "Let's start a new game!"
        new_game()
    
    
# create frame

f = sg.create_frame("Guess number", 200, 200)

# register event handlers for control elements and start frame

f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 100)

f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

