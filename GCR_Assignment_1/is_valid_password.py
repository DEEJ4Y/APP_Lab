from curses.ascii import isdigit, islower, isupper


def is_valid_password(password: str):
    contains_at_least_one_lowercase = False
    contains_at_least_one_uppercase = False
    contains_at_least_one_number = False
    contains_at_least_one_special_character = False

    password_length = len(password)

    if password_length < 6:
        return False

    if password_length > 16:
        return False

    for i in range(0, password_length):
        if isdigit(password[i]):
            contains_at_least_one_number = True

        if islower(password[i]):
            contains_at_least_one_lowercase = True

        if isupper(password[i]):
            contains_at_least_one_uppercase = True

        if password[i] == '$' or password[i] == "#" or password[i] == '@':
            contains_at_least_one_special_character = True

    if contains_at_least_one_lowercase and contains_at_least_one_uppercase and contains_at_least_one_number and contains_at_least_one_special_character:
        return True
    else:
        return False


if __name__ == "__main__":

    p = input("Enter your password: ")
    valid = is_valid_password(p)

    if valid:
        print("Valid Password!")

    else:
        print("Invalid Password :(")
