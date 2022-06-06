def comb(L):

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i != j and j != k and i != k):
                    print(L[i], L[j], L[k])


digits = [1, 2, 3]

print(f'digits = {digits}\n\n')
comb(digits)
