# "Guess the number" game
#Autor Lahiru Manoha

import simplegui
import random

# initialize global
num_range = 100
count = 0

#helper functions
""" default value and function call """
def init():
    global num_range
    global count
    range100()
    
# define event handlers
    """ event handlers for tow buttons and input field """
def range100():
    global num_range
    global count
    count = 7
    num_range = random.randrange(0, 101)
    print "New game. Range is from 0 to 100 "
    print "Number of remaining guesses is 7"
    print ""

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global count
    count = 10
    num_range = random.randrange(0, 1001)
    print "New game. Range is from 0 to 1000 "
    print "Number of remaining guesses is 10"
    print ""

# main game logic goes here	
""" the logic of the game determine win or lose the game """
def get_input(guess):
    global count
    match_guess = int(guess)
    count = count - 1
        
    if(match_guess == num_range and not(count == 0)):
       print "Guess Was", match_guess
       print "number of remaining gusses is", count
       print "correct!"
       print""
       init()
    elif(match_guess > num_range):
       print "Guess Was", match_guess
       print "number of remaining gusses is", count
       print "Lower!"
       print ""
    elif(match_guess < num_range):
       print "Guess Was", match_guess
       print "number of remaining gusses is", count
       print "Higher!"
       print ""
        
    if(count == 0):
       print "number of remaining gusses is 0"
       print "You ran out of guesses The number was", num_range
       print ""
       init()
        
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

#call when start the game
init()

# start frame
f.start()