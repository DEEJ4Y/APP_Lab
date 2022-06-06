if __name__ == "__main__":
    numberStr = input("Enter a phone number: ")
    count = len(numberStr)
    missingIndexes = []
    for index in range(0, len(numberStr)):
        char = numberStr[index]
        if char == " ":
            missingIndexes.append(index + 1)
            count -= 1

    if len(missingIndexes) == 0 and count == 10:
        print("Phone number is valid!")
        quit()

    if count != 10:
        print("Number is not long enough")

    if len(missingIndexes) > 0:
        print(f'The letters at these positions were missing: {missingIndexes}')
