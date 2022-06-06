from curses.ascii import isalpha, isdigit


def calc_digits_and_alpha(s: str):
    alpha_count = 0
    digit_count = 0

    for i in range(0, len(s)):
        if isdigit(s[i]):
            digit_count += 1
        if isalpha(s[i]):
            alpha_count += 1

    return {
        "alpha": alpha_count,
        "digit": digit_count,
    }


if __name__ == "__main__":
    s = input("Enter a string: ")
    res = calc_digits_and_alpha(s)
    a = res["alpha"]
    d = res["digit"]
    print(f'Letters: {a}')
    print(f'Digits: {d}')
