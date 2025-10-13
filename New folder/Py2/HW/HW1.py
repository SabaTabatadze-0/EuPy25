vow = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"

while True:
    inp = str(input())
    if inp == "!":
        print("over")
        break
    elif inp in vow:
        print("vowel")
    else :
        print("now vowel")