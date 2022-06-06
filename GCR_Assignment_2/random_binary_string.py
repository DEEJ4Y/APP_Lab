import random


def rand_binary_number(p):

    key1 = ""

    for i in range(p):
        temp = str(random.randint(0, 1))

        key1 += temp

    return(key1)


n = int(input("Enter the length of the required binary string: "))
str1 = rand_binary_number(n)
print("Desired length random binary string is: ", str1)
