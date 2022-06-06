t1 = (11, 2, 3, 14)
t2 = (13, 5, 22, 10)
t3 = (12, 2, 3, 10)
t4 = (t1[0] + t2[0] + t3[0], t1[1] + t2[1] + t3[1],
      t1[2] + t2[2] + t3[2], t1[3] + t2[3] + t3[3])

print(f'Given tuples: \n{t1}\n{t2}\n{t3}\n\n')
print(f'Element wise sum: {t4}')
