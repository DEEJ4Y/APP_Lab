def reverse_string(s: str):
    slen = len(s)
    reversed = ""

    for i in range(slen-1, 0, -1):
        reversed += s[i]

    return reversed


user_in = input("Enter something to be mirrored: ")
print(reverse_string(user_in))
