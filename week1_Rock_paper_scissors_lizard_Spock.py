import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):

    num = -1
    
    if name == "rock":
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    else:
        num = 4
        
    return num

def number_to_name(number):

    name = "x"
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    
    return name

def rpsls(player_choice): 
    
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    
    comp_choice = number_to_name(comp_number);
    
    print "Player chooses " + player_choice
    print "Computer chooses " + comp_choice
    
    if (player_number == comp_number):
        print "Player and computer tie!"
    else:
        if (player_number + 1) % 5 == comp_number or (player_number + 2) % 5 == comp_number:
            print "Computer wins!"
        else:
            print "Player wins!"
    
    print
    

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



