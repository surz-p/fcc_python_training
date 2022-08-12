# game of rock paper scissors

import random
import sys

def get_choices():
  possible_choices = ['rock', 'paper', 'scissors']
  user_choice = input('Enter your choice (rock, paper, scissors): ')
  # validation to check possible choices later
  if user_choice not in possible_choices:
    sys.exit(f'You entered incorrect choice {user_choice}')
  computer_choice = random.choice(possible_choices)
  choice_dict = {'user': user_choice, 'computer': computer_choice}
  return choice_dict

def print_result(user_chose, computer_chose, status):
  print(f'You chose {user_chose}, computer chose {computer_chose}. You {status}')

def get_result():
  choices_made = get_choices()
  user_chose = choices_made['user']
  computer_chose = choices_made['computer']

  if user_chose == computer_chose:
    print_result(user_chose, computer_chose, 'tied.')
  elif user_chose == 'rock':
    if computer_chose == 'scissors':
      print_result(user_chose, computer_chose, 'win!')
    else:
      print_result(user_chose, computer_chose, 'lose.')
  elif user_chose == 'paper':
    if computer_chose == 'rock':
      print_result(user_chose, computer_chose, 'win!')
    else:
      print_result(user_chose, computer_chose, 'lose.')
  elif user_chose == 'scissors':
    if computer_chose == 'paper':
      print_result(user_chose, computer_chose, 'win!')
    else:
      print_result(user_chose, computer_chose, 'lose.')
  return

get_result()