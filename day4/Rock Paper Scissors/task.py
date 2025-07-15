from threading import RLock
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 = Rock, 1 = Paper, 2 = Scissor

all_choices = [0, 1, 2]
all_choice_images = [rock, paper, scissors]
computer_choice_index = random.randint(0, 2)
user_choice = int(input("Play the game! 0 for Rock, 1 for Paper and 2 for Scissor"))
if user_choice > 2:
    print("Invalid number!")
else:
    print('Computer choose')
    print(all_choice_images[computer_choice_index])
    print('You choose')
    print(all_choice_images[user_choice])

if user_choice == 0 and all_choices[computer_choice_index] == 2:
    print('\nYou won!')
elif user_choice == 1 and all_choices[computer_choice_index] == 0:
    print('\nYou won!')
elif user_choice == 2 and all_choices[computer_choice_index] == 1:
    print('\nYou won!')
elif user_choice == all_choices[computer_choice_index]:
    print('\nYou and computer choose the same option, it\'s a tie')
else:
    print('\nYou loose!')