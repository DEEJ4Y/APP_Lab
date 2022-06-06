# Nisha have to design an multi task tool.
# When she enters 1 the system has to display fibonaci series
# and when she enters 2 multiplication upto 15 have to be displayed


# Fibonacci
def fibonacci(n):
    arr = []
    sum = 0
    rng = range(0, n)
    for i in rng:
        if(i == 1):
            sum = 1
        elif(i == 2):
            sum = sum
        else:
            sum = sum + i
        arr.append(sum)

    return arr


# factorial
def factorial(n):
    mul = 1
    rng = range(1, n)
    for i in rng:
        mul = mul * i

    return mul


if __name__ == "__main__":
    print("Multitasking tool. Choose an option.")

    running = True
    if (running == True):
        print("Enter 1 for fibonacci")
        print("Enter 2 for factorial")
        print("Enter anything else to exit")

        choice = 0
        choice = int(input("Choice: "))
        if (choice == 1):
            print("\nFibonacci")
            num = int(input("Enter a number: "))
            fib = fibonacci(num)
            print(f'Fibonacci of {num}: {fib}')
        elif(choice == 2):
            print("\n Factorial")
            num = int(input("Enter a number: "))
            fact = factorial(num)
            print(f'Factorial of {num}: {fact}')
        else:
            running = False
