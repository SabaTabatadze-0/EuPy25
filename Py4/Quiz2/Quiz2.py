a = int(input())
arr = []
i = 1

while i <= a:
    if a % i == 0:
        arr.append(i)
    i += 1

if len(arr) < 1:
    print("not prime")
elif len(arr) <= 2:
    print("prime")
elif len(arr) > 2:
    print("not prime")
