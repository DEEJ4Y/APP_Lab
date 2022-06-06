if __name__ == "__main__":
    size = 9
    for i in range(size, -1, -1):
        strtmp = ''
        for j in range(0, i):
            strtmp += str(i)

        print(strtmp)
