d = 0
k = 0
s = -1
while s != 0:
    s = int(input())
    if d < s:
        d = s
        k = 1
    elif d == s:
        k += 1
print(k)