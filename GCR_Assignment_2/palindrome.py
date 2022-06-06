def reverse_string(s: str):
    slen = len(s)
    reversed = ""

    for i in range(slen-1, -1, -1):
        reversed += s[i]

    return reversed


def isPalindrome(s: str):
    s_rev = reverse_string(s)

    if s == s_rev:
        return True

    return False


palincheck = input("Enter a string: ")
print(f"Palindrome: {isPalindrome(palincheck)}")
