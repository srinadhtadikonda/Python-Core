#selection Sort
x = [1, 3, 2, 5, 4]

n = len(x)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if x[j] < x[min_index]:
            min_index = j

    x[i], x[min_index] = x[min_index], x[i]

print(x)
