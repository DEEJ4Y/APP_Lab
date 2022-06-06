def calc_digit_sum(num: int):
    numstr = str(num)
    sum = 0
    for i in range(0, len(num)):
        sum += int(numstr[i])

    return sum


def subtract_digit_sum_till_negative(num: int):
    steps = 0
    while num > 0:
        stringNum = str(num)
        split = stringNum
        sum = 0
        for char in split:
            print(char)
            int_char = int(char)
            sum += int_char
        num -= sum
        steps += 1

    return {"num": num, "steps": steps}


if __name__ == "__main__":
    num = int(input("Enter a positive number: "))
    if num <= 0:
        print("Not a positive number :/")
    else:
        res = subtract_digit_sum_till_negative(num)
        print(f'Number: {res["num"]}')
        print(f'Steps: {res["steps"]}')
