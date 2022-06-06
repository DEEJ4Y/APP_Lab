def remove_punctuation_and_special_characters(s: str):
    slen = len(s)
    removed = ""
    for i in range(0, slen):
        if s[i].isalnum() or s[i] == " ":
            removed += s[i]

    return removed


user_in = input("Enter a string: ")
print("\nThe special characters were removed")
print(remove_punctuation_and_special_characters(user_in))
