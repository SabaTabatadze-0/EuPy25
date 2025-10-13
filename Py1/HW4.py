a = int(input())
b = int(input())
c = int(input())

max = 0
if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > a and c > b:
    max = c

min=0
if a < b and a < c:
    min = a
elif b < a and b < c:
    min = b
elif c < a and c < b:
    min = c


mid = 0
if a != max and a != min:
    mid = a
elif b != max and b != min:
    mid = b
elif c != max and c != min:
    mid = c

print(min, mid, max)