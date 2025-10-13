s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
s6 = int(input())

s = (s1+s2+s3+s4+s5+s6) / 6
if s >= 91 and s <= 100:
    print("Grade : A")
elif s >= 81 and s <= 90:
    print("Grade : B")
elif s >= 71 and s <=80:
    print("Grade : C")
elif s >= 61 and s <=70:
    print("Grade : D")
elif s >= 51 and s <= 60:
    print("Grade : E")
elif s <= 50:
    print("Grade : F")
else :
    print("invalid number")