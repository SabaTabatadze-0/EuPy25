st = int(input())
fin = int(input())
arr = []

i = st
while i <= fin:
    cnt = 0

    for i2 in range(1, i + 1):
        if i%i2 == 0:
            cnt += 1
    if cnt == 2:
        arr.append(i)
    i += 1
print(arr)