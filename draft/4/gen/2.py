# от 0 до N только четные 

def x2(n, k = 1):
    for k in range(1, n + 1):
        if (k % 2 == 0):
            yield k

n = int(input())
gen = x2(n)

for i in gen:
    print(i, end = ' ')