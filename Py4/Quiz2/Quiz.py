a = int(input())
b = int(input())
arr = []
mult = 1

while a <= b:
    if a % 2 == 0:
        arr.append(a)
    a += 1

for i in arr:
    mult = mult * i

print(mult)