def gen_squares(n, k = 1):
    while k <= n:
        yield pow(k, 2)
        k += 1

n = int(input())
gen = gen_squares(n)
for i in gen:
    print(i, end = ' ')