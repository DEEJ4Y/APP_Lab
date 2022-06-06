# Get the marks for three subjects. Find the total and average. calculate the Grade as follows
#   avg > 90  Grade = O
#   avg > 80 and avg <= 90 Grade A
#   avg > 70 and avg <= 80 Grade B
#   avg > 60 and avg <= 70 Grade C
#   avg > 50 and avg <= 60 Grade D
#   avg <= 50 Grade F


# Get subject marks
def get_marks():
    sub1 = float(input("Subject 1: "))
    sub2 = float(input("Subject 2: "))
    sub3 = float(input("Subject 3: "))

    return {"sub1": sub1, "sub2": sub2, "sub3": sub3}


# Calculate average
def calc_average(sub1: float, sub2: float, sub3: float):
    avg = (sub1+sub2+sub3)/3.0

    return avg


# Get grades
def get_grade(grade: float):
    if(grade < 0.0 or grade > 100.0):
        return False
    elif(grade > 90):
        return "O"
    elif(grade > 80 and grade <= 90):
        return "A"
    elif(grade > 70 and grade <= 80):
        return "B"
    elif(grade > 60 and grade <= 70):
        return "C"
    elif(grade > 50 and grade <= 60):
        return "D"
    else:
        return "F"


# Main
if __name__ == "__main__":
    print("Average Calculator. Enter the marks for three subjects.")
    marks = get_marks()
    avg = calc_average(marks["sub1"], marks["sub2"], marks["sub3"])
    grade = get_grade(avg)

    print(f'Average: {avg}')
    print(f'Grade: {grade}')
