# insert(?) sort
arr = [10, 2, 1, 3, 5]


def find_smallest(arr, i):
    mn = arr[i]
    mn_index = i
    while i < len(arr):
        if arr[i] < mn:
            mn = arr[i]
            mn_index = i
        i += 1
    return mn_index

i = 0
while i < len(arr):
    pos = find_smallest(arr, i)
    tmp = arr[i]
    arr[i] = arr[pos]
    arr[pos] = tmp
    i += 1

print(arr)