#Bubble Sort
x = [1, 3, 2, 5, 4]

n = len(x)

for i in range(n):
    for j in range(n - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]

print(x)
