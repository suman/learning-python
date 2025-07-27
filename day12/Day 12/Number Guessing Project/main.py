import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def make_ready_attempt():
    attempt = 0
    if level == "hard":
        attempt = 5
    else:
        attempt = 10
    return attempt

level = input("Choose a difficulty. Type 'easy' or 'hard':")
computer_chose_number = random.randint(1, 100)
remaining_attempt = make_ready_attempt()

for i in range(0, remaining_attempt):
    print(f"You have {remaining_attempt} attempts remaining to guess the number. ")
    guess = int(input("Make a guess:"))
    if guess == computer_chose_number:
        print(f"You got it! The answer was {guess}.")
        break
    elif guess < computer_chose_number:
        print("Too low.")
        print("Guess Again.")
    elif guess > computer_chose_number:
        print("Too High.")
        print("Guess Again.")
    remaining_attempt -= 1
