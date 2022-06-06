def are_all_digits_even(num: int):
    strnum = str(num)

    for i in range(0, len(strnum)):
        currint = int(strnum[i])
        if not currint % 2 == 0:
            return False

    return True


if __name__ == "__main__":
    strn = ''
    for i in range(100, 401):

        res = are_all_digits_even(i)
        if res == True:
            strn += f'{i}, '

    print(strn)
