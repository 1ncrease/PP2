import math
sum, sum_s, n = 0, 0, 0
x = int(input())
while x != 0:
    n += 1
    sum += x
    sum_s += x ** 2
    x = int(input())
print(math.sqrt((sum_s - sum ** 2 / n) / (n - 1)))