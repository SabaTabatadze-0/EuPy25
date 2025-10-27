n = int(input())
arr = []
i = 1
sum = 0

while i <= n:
    grade = int(input())
    arr.append(grade)
    sum += grade
    i += 1

gpa = sum / n

print(gpa)