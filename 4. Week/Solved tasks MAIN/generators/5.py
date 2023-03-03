def ret(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
gen = ret(n)
for i in gen:
    print(i, end = ' ')