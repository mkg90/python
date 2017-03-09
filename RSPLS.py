# Rock-paper-scissors-lizard-Spock template


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
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        number = 0
    elif name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print
        'name not in RSPLS'
    return number


# convert number to a name using if/elif/else
# don't forget to return the result!

def number_to_name(number):
    # fill in your code below
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print
        'number not in range'
    return name


import random


def rpsls(name):
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if 0 < difference < 3:
        a = 'Player wins!'
    elif difference == 0:
        a = 'Player and Computer tie'
    else:
        a = 'Computer wins!'
        # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    # print results

    print
    'Player chooses', name
    print
    'Computer chooses', comp_name
    print
    a
    print
    ''
    print
    ''


# test your code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


