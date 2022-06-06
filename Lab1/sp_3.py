# 3. Create a Lottery Application to generate a three-digit lottery number. The program
# prompts the user to enter a three-digit number and determines whether the user wins.

from random import random


def generate_lottery():
    generated = False
    lottery = 0
    while not generated:
        lottery = random() * 1000
        if not lottery < 100 and not lottery > 1000:
            return lottery.__floor__()


if __name__ == "__main__":
    lottery = generate_lottery()
    user_in = input("Enter your 3 digit lottery number: ")
    if user_in == lottery:
        print("Congratulations! You won the lottery!")
    else:
        print(f'Better luck next time! The lottery number was {lottery}')
