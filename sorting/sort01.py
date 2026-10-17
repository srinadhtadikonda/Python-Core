#Bubble Sort
x = [1, 3, 2, 5, 4]

def qsort(x):
    if len(x) <= 1:
        return x

    pivot = x[-1]
    less = []
    greater = []

    for i in x[:-1]:
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)

    return qsort(less) + [pivot] + qsort(greater)

print(qsort(x))
