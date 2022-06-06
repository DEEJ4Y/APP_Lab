def display_histogram(arr):
    for i in range(0, len(arr)):
        tmpstr = f'{str(arr[i])}  '
        for j in range(0, arr[i]):
            tmpstr += '|'

        print(tmpstr)


if __name__ == "__main__":
    display_histogram([12, 23, 10, 15, 13])
