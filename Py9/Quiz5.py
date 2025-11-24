arr = [5, 2, 3, 20, 12]

def min_fun(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


print(min_fun(arr))