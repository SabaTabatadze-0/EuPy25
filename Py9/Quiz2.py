def rev_erser(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev


print(rev_erser(input()))
