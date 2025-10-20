arr = [1, 2, 3, 4, 5, 6]
n = int(input())
i = 0
count = 0

while i <= n:
    if arr[i] % n == 0:
        count += i
    i += 1

if count == 1:
    print("Found")
else:
    print("Not Found")
