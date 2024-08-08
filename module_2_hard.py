n = int(input('Введите целое число от 3 до 20: '))
keys = list(range(1,n))
result = []
for i in keys:
    keys2 = list(range(int(i) + 1, n))
    for j in keys2:
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)
print(*result)












