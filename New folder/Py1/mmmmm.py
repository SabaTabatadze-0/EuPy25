# a = 100

# b = a * 0.2
# c = a * 0.8

# print(b)
# print(c)

# 1.
W = 5
L = 4

P = (W * 2) + (L * 2)
print("Perimeter is", P)

# 2.
F = 108
C = (F - 32) * (5 / 9)

print("Celsius is", C)

# 3.

p1 = 20
p2 = 100
p3 = 40
p4 = 60

if (p1 + p2 + p3 + p4) / 4 > 100:
    print("Expensive :<")
else:
    print("Not Expensive :>")

# 4.
a = -9

if a > 0:
    print("Positive")
elif a == 0:
    print("null")
else:
    print("Negative")

# 5.

a = 10
b = 5
c = 10

if a == b == c:
    print("3")
elif a == b or a == c or b == c:
    print("2")
else:
    print("1")
