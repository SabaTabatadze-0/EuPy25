arr = []

while True:
    arr.append(int(input()))
    if len(arr) == 4:
        break
sum = 0

for i in range(0, 4):
    sum += arr[i]
    i += 1

mul = 1

for i in range(0, 4):
    mul *= arr[i]
    i += 1

print(sum)
print(mul)
