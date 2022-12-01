import random


# decisions = ['rock', 'paper', 'scissors']
# computer_decision = random.choice(decisions)
# user_decision = input('rock, pager or scissors? ')
# while user_decision.lower() not in decisions:
#     user_decision = input('rock, pager or scissors? ')
# if user_decision.lower() == 'rock' and computer_decision == 'paper':
#     print('I won, I chose paper.')
# elif user_decision.lower() == 'paper' and computer_decision == 'scissors':
#     print('I won, I chose scissors.')
# elif user_decision.lower() == 'scissors' and computer_decision == 'rock':
#     print('I won, I chose rock.')
# elif user_decision == computer_decision:
#     print('We both choose',user_decision + ",let's play again.")
# else:
#     print('You win, I chose',computer_decision)

decisions = ['rock', 'paper', 'scissors']
random_decision = random.randint(0,2)
if random_decision == 0:
    computer_decision = 'rock'
elif random_decision == 1:
    computer_decition = 'paper'
else:
    computer_decision = 'scissors'
while True:
    user_decision = input('rock, pager or scissors? ')
    if user_decision.lower() in decisions:
        break
if user_decision.lower() == 'rock':
    user_decision_num = 0
elif user_decision.lower() == 'paper':
    user_decision_num = 1
else:
    user_decision_num = 2
if (user_decision_num - random_decision) in [1,-2]:
    print('You win, I chose',computer_decision)
elif user_decision_num == random_decision:
    print('We both chose', user_decision + ", Let's play again")
else:
    print('I win, I chose', computer_decision)