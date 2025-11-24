arr = [12, 3, 5, 10, 8, 1]

i = 1
while i < len(arr):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and tmp <= arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp
    i += 1

print(arr)
