s = input("enter text: ")

cnt_m = {}

for x in s:
    if x in cnt_m.keys():
        cnt_m[x] = cnt_m[x] + 1
    else:
        cnt_m[x] = 1

for k, v in cnt_m.items():
    print(k, v)