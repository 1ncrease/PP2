a = int(input())
i = 1
c, d = 0, 1
while d <= a:
    c, d = d, c + d
    i += 1
    if d == a:
        print(i)
        break
else:
    print('-1')
