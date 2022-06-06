def month_to_days(month: str):
    month = month.lower()

    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        return 31

    if month == "april" or month == "june" or month == "september" or month == "november":
        return 30

    if month == "february":
        return 28


if __name__ == "__main__":
    m = input("Enter the name of a month: ")
    print(f'The number of days in {m} is: {month_to_days(m)}')
