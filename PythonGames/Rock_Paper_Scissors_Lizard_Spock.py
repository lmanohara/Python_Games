#Rock-paper-scissors-lizard-Spock 
#author Lahiru Manohara

import random

# to convert number to a name
def number_to_name(number):
    """ to comapir with number and return string name"""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name

#to convert name to a number
def name_to_number(name):
    """ to compair with name and return integer number """
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4 

    return number

#to do logic and print result
def rpsls(name): 
    
    """ display output and game logics are in here"""
    
    player_number = name_to_number(name)
    player_guess = name
    
    comp_number = random.randrange(0, 5)
    

    difference  = (player_number - comp_number) % 5

    if difference == 1 or difference == 2:
        result = "Player wins!"
    elif difference == 3 or difference == 4:
        result = "Computer wins!"
    else:
        result = "Game is tie!"
        
    comp_guess = number_to_name(comp_number)
    
    print "Player chooses", player_guess
    print "Computer chooses", comp_guess
    print result
    print " "

    
# test cases
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

