test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

print("Matrix: " + str(test_list))

temp = [ele for sub in test_list for ele in sub]

res = list(zip(*temp))

print("The converted tuple list : " + str(res))
