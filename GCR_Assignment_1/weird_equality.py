def weird_equality(a: int, b: int):
    if a == b or a + b == 5 or a - b == 5:
        return True

    return False


if __name__ == "__main__":
    a = int(input("Enter the first num: "))
    b = int(input("Enter the second num: "))
    print(weird_equality(a, b))
