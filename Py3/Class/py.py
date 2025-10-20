n = int(input())
i = 1
arr = []
while i <= n:
    if n % i == 0:
        arr.append(i)
    i += 1

arr.pop(0)

if len(arr) > 1:
    print("Not Prime")
else:
    print(arr, "is Prime")
