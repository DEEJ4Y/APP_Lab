# 5. Write a program that reads integers, finds the largest of them, and counts its occurrences.
# Assume that the input ends with number 0. Suppose that you entered 3 5 2 5 5 5 0
# the program finds that the largest number is 5 and the occurrence count for 5 is 4.

if __name__ == "__main__":
    liststring = input("Enter space separated integers: ")
    in_list = liststring.split(" ")

    maxNum = max(in_list)
    print(f'Max: {maxNum}')
    count = 0
    for str in in_list:
        if str == maxNum:
            count += 1

    print(f'Count: {count}')
