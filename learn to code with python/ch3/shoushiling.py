import random

# Setup the computer's choice by choice() from Random module
# decisions = ['rock', 'paper', 'scissors']
# computer_decision = random.choice(decisions)

# Get user's choice by input keyword.
# If the input isn't one of the three choices, prompt the input message again and ask for another input.
# user_decision = input('rock, pager or scissors? ').lower()
# while user_decision.lower() not in decisions:
#     user_decision = input('rock, pager or scissors? ').lower()

# Game logic and output who won the game.
# if user_decision == 'rock' and computer_decision == 'paper':
#     print('I won, I chose paper.')
# elif user_decision == 'paper' and computer_decision == 'scissors':
#     print('I won, I chose scissors.')
# elif user_decision == 'scissors' and computer_decision == 'rock':
#     print('I won, I chose rock.')
# elif user_decision == computer_decision:
#     print('We both choose',user_decision + ",let's play again.")
# else:
#     print('You win, I chose',computer_decision)

# Setup computer's choice by randint() from Random module,then mapping to corresponding string.
decisions = ['rock', 'paper', 'scissors']
random_decision = random.randint(0,2)
if random_decision == 0:
    computer_decision = 'rock'
elif random_decision == 1:
    computer_decition = 'paper'
else:
    computer_decision = 'scissors'

# Get user's choice by input method, keep asking until the input is one of three choices.
while True:
    user_decision = input('rock, pager or scissors? ')
    if user_decision.lower() in decisions:
        break

# Mapping user's choice to corresponding integer.
if user_decision.lower() == 'rock':
    user_decision_num = 0
elif user_decision.lower() == 'paper':
    user_decision_num = 1
else:
    user_decision_num = 2

# Game logic, and output the winner.
if (user_decision_num - random_decision) in [1,-2]:
    print('You win, I chose',computer_decision)
elif user_decision_num == random_decision:
    print('We both chose', user_decision + ", Let's play again")
else:
    print('I win, I chose', computer_decision)