def is_list_unique(arr):
    for i in range(1, len(arr)):
        curr = arr[i-1]
        for j in range(i, len(arr)):
            if curr == arr[j]:
                return False

    return True


if __name__ == "__main__":
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list)
    print(is_list_unique(list))
    print("\n")

    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
    print(list)
    print(is_list_unique(list))
