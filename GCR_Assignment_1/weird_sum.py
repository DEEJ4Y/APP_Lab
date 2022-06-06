def weird_sum(a: int, b: int):
    sum = a + b
    if sum >= 105 and sum <= 200:
        return 200
    else:
        return sum


if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sum = weird_sum(a, b)
    print(f'Weird sum: {sum}')
