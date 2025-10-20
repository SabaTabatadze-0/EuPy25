a = 1000


for i in range(1, a + 1):
    Sum = 0
    for i2 in range(1, i):
        if i % i2 == 0:
            Sum += i2

    if Sum == i:
        print(i)
