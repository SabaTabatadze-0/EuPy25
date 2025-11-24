arr = [1, 2, 3]


def med_fun(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum // len(arr)


print(med_fun(arr))
