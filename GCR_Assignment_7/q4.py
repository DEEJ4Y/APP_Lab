def average(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result


nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n", average(nums))
