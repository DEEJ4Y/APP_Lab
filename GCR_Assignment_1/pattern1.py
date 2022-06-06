if __name__ == "__main__":
    max = 5
    for i in range(0, max + 1):
        s = ''
        for j in range(0, i):
            s += '*'

        print(f'{s}')
    for i in range(max - 1, 0, -1):
        s = ''
        for j in range(0, i):
            s += '*'

        print(f'{s}')
