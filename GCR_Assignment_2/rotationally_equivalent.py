def reverse_string(s: str):
    slen = len(s)
    reversed = ""

    for i in range(slen-1, -1, -1):
        reversed += s[i]

    return reversed


user_in_1 = input("Enter a string: ")
user_in_2 = input("Enter another string: ")

if user_in_1 == reverse_string(user_in_2):
    print("Strings are rotationally equivalent")
else:
    print("Strings are not rotationally equivalent")
