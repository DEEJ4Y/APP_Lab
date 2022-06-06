def reverse_string(s: str) -> str:
    reversed_string = ''
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]

    return reversed_string


if __name__ == "__main__":
    user_in = input("Enter a string to be reversed: ")
    print(reverse_string(user_in))
