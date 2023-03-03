import math
from math import tan
def polygon(n,a):
    def ctg(x):
        return 1 / tan(x)

    S = (n / 4) * a ** 2 * ctg(math.pi / n)
    print((round(S, 2)))


print("numb of sides: ")
n = int(input())
print("length: ")
a = float(input())
polygon(n,a)