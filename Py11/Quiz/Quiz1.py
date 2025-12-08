n = input("Input Number: ")


def dig(number):
    s = str(number)

    total = 0

    for x in s:
        total += int(x)

    return total


print("sum of all digits is: ", dig(n))
