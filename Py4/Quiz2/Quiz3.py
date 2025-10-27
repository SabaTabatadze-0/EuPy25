arr = [1, 3, 6, 7, 9]
a = int(input())
b = len(arr)
i = 0

for i in range(b):
    if a <= arr[i]:
        print("index is", i)
        break
    else:
        print("index is", b + 1)
        break
