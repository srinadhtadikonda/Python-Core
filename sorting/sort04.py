#Inserttion Sort
x = [1, 3, 2, 5, 4]

for i in range(1, len(x)):
    key = x[i]
    j = i - 1

    while j >= 0 and x[j] > key:
        x[j + 1] = x[j]
        j -= 1

    x[j + 1] = key

print(x)
