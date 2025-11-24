def reverser(str1):
    leng = len(str1)
    str2 = ""
    while leng > 0:
        str2 += str1[leng - 1]
        leng -= 1
    return str2


print(reverser("it works?"))