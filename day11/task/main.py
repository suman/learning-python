# 1. Ask user if he wants to play the game, if user chose no, exit the game
# 2. if user choose yes, pick th two random number for the user, pick one number for the computer
# 3. if sum of two number of user is more than 21 then quit the game, declare computer is the winner, print the loose message, jump to step 1
# 4. if sum of two number of user  is equivalent to 21 then the user wins game, declare the winner, inform user about the same, jump to step 1
# 5. if sum is less than 21, ask user if he wants to pick another number/card,
# 6. in case of yes, pick another random number and repeat the number from 3 to 5
# 7. in case of no, computer will choose the pick card, make the sum
# 8. if sum is 21, declare the winner, inform the user he loses the game, jump to step 1
# 9. if sum is less n 17, repeat the number from 7 to 8
# 10.if sum is more thn 17, exit the loop
# 11. if winner is not declared yet, compare the total score of computer and user and declare the winner who has the greater value
# 12, Jump to step 1

import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_play_game = 'y'


def game_over(user_card_numbers):
    """Check if game is over when the it's started with intial card and score"""
    user_sum = sum(user_card_numbers)
    print(f"Your total cards {user_card_numbers} and score is {user_sum}")

    if user_sum == 21:
        print("You win!")
        return True
    elif user_sum > 21:
        print("Dealer Win!")
        return True
    return False

def declare_winner():
    print(f"Your total cards is {user_cards} and score is {sum(user_cards)}")
    print(f"Computer's total cards is {computer_cards} and score is {sum(computer_cards)}")

    user_total_value = sum(user_cards)
    computer_total_value = sum(computer_cards)

    if user_total_value == computer_total_value:
        print("It's a Tie")
    elif user_total_value > computer_total_value and user_total_value < 22:
        print("You Win!")
    elif computer_total_value > user_total_value and computer_total_value < 22:
        print("Dealer Win!")

while continue_play_game == 'y':
    winner_declare = False
    user_wants_game = input("Do you want to play the Jack Game, press 'y' for yes 'n' for no")
    if user_wants_game == 'n':
        continue_play_game = 'n'
    else:
        print("\n" * 20)
        print(logo)
        user_cards = []
        computer_cards = []


        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

        winner_declare = game_over(user_cards)

        if winner_declare:
            continue_play_game = 'n'
        else:
            ask_for_card = True
            while ask_for_card:
                pick_card = input("Do you want to pick another card?, press 'y' for yes or press 'n' for pass on")
                if pick_card == 'y':
                    user_cards.append(random.choice(cards))
                    winner_declare = game_over(user_cards)
                    if winner_declare:
                        ask_for_card = False
                elif pick_card == 'n':
                    ask_for_card = False

            if not winner_declare:
                while sum(computer_cards) <= 17:
                    computer_cards.append(random.choice(cards))
                declare_winner()