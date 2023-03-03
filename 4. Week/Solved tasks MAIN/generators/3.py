def thr_for(n, k = 1):
    while k <= n:
        if(k % 3 == 0 and k % 4 == 0):
            yield k
        k += 1
n = int(input())
gen = thr_for(n)
for i in gen:
    print(i, end = ' ')