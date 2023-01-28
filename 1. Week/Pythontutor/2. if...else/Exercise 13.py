n, m, x, y = int(input()), int(input(), int(input()), int(input()))
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
if x < y:
    print(x)
else:
    print(y)