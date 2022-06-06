def is_divisible_by_8(num: int):
    if num % 8 == 0:
        return True
    else:
        return False


def is_divisible_by_5(num: int):
    if num % 5 == 0:
        return True
    else:
        return False


def is_divisible_by_both_8_and_5(num: int):
    if is_divisible_by_5(num) and is_divisible_by_8(num):
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(1000, 2001):
        if is_divisible_by_both_8_and_5(i):
            print(f'{i}\n')
