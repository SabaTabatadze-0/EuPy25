arr = [1, 2, 3, 20, 12]

def max_fun(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


print(max_fun(arr))
