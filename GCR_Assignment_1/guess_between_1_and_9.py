import random


def random_number_between_1_and_9():
    return random.randint(1, 9)


if __name__ == "__main__":
    correct_guess = False
    num = random_number_between_1_and_9()
    while not correct_guess:
        guess = int(input("Guess the number: "))
        if guess == num:
            print(f'You guessed right! The number was {num}')
            correct_guess = True
        else:
            print('Oops! Wrong guess, try again.\n')
