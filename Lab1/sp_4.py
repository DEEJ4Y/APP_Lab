# 4. Create a Scissor and Rock simulator that plays the popular scissor-rockpaper game. (A
# scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.) The
# program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper. The
# program prompts the user to enter a number 0, 1, or 2 and displays a message indicating
# whether the user or the computer wins, loses, or draws.

from random import random


def generate_random_int_0_to_3():
    return (3 * random()).__floor__()


def handle_rock_paper_scissors(inp):
    inp = str(inp)
    if inp == "0" or inp == "rock":
        return "rock"
    if inp == "1" or inp == "paper":
        return "paper"
    if inp == "2" or inp == "scissors":
        return "scissors"
    return False


def decide_winner(in1, in2):
    if in1 == in2:
        return "Tie!"
    if (in1 == "rock" and in2 == "scissors") or (in1 == "paper" and in2 == "rock") or (in1 == "scissors" and in2 == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"


if __name__ == "__main__":
    user_in = input("Enter rock, paper or scissors: ")
    valid_user_input = handle_rock_paper_scissors(user_in)
    if not valid_user_input:
        print("Invalid value entered :(")
        quit()

    computer_input = handle_rock_paper_scissors(generate_random_int_0_to_3())

    print(f'User: {valid_user_input}')
    print(f'Computer: {computer_input}')

    print(decide_winner(valid_user_input, computer_input))
