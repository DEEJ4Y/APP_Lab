from cmath import sqrt


def distance_between_two_coordinates(x1: int, y1: int, x2: int, y2: int):
    return sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))


if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print(distance_between_two_coordinates(x1, y1, x2, y2))
