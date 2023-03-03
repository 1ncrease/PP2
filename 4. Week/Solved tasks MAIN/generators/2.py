def gen_even(n, k = 0):
    while k <= n:
        if(k % 2 == 0):
            yield k
        k += 1
n = int(input())
gen = gen_even(n)
for i in gen:
    print(i, end = ' ')