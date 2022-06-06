
def generate_matrix(rows: int, cols: int):
    arr = []
    for i in range(0, rows):
        nested = []
        for j in range(0, cols):
            nested.append(i * j)

        arr.append(nested)

    return arr


if __name__ == "__main__":
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of cols: "))
    print(generate_matrix(r, c))
