# start game at 5:39

# import the logo
# Pick the random two element
# display this two random element to screen
# append these into already displayed list
# set current highest element
# ask user which is the highest element
# append chosen element into  already displayed list
# if answer is correct pick the another element and displayed into the screen
# if answer is incorrect, the game is over

import random
from art import logo
from game_data import data
print("Welcome to Higher and Lower follower game")
print(logo)
print("You have to choose 'h' highest follower and 'l' for lowest follower for the second personality")

already_chosen_personality = []
user_score = 0
def select_personality(index):
    return data[index]

def pick_personality_index(data):
    return random.randint(0, len(data) - 1)

def update_first_personality(previous, to_be_update):
    previous = to_be_update
    return previous

def get_second_personality(all_personalities, already_chosen_personalities):
    chosen_personality_index = pick_personality_index(all_personalities)
    while chosen_personality_index in already_chosen_personalities:
        chosen_personality_index = pick_personality_index(all_personalities)

    already_chosen_personalities.append(chosen_personality_index)
    return all_personalities[chosen_personality_index]

def display_personality_challenge(first_personality, second_personality):
    print(f"Score is {user_score}.")
    print(logo)
    print(f"{first_personality['name']} has followers {first_personality['follower_count']},  {second_personality['name']} has or lower follower{second_personality['follower_count']}, ")
    user_choice = input("Type h for higher or type l for lower")
    return user_choice


def get_first_personality(data, all_personalities):
    index1 = pick_personality_index(data)
    selected_personality = select_personality(index1)
    all_personalities.append(index1)
    return selected_personality


game_over = False
first_personality  = get_first_personality(data, already_chosen_personality)
second_personality = get_second_personality(data, already_chosen_personality)

while not game_over:
    higher_or_lower = display_personality_challenge(first_personality, second_personality)
    if (higher_or_lower == 'h' and
            first_personality['follower_count'] < second_personality['follower_count']):
        user_score += 1
    elif (higher_or_lower == 'l' and
          first_personality['follower_count'] > second_personality['follower_count']):
        user_score +=1
    else:
        game_over = True
        print(f"You loose th game and your final score is {user_score}")

    first_personality = update_first_personality(first_personality,
                                                 second_personality)
    second_personality = get_second_personality(data, already_chosen_personality)
