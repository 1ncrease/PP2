def gen_squares(a, b):
    while a <= b :
        yield a**2
        a += 1

a = int(input())
b = int(input())
gen = gen_squares(a, b)
for i in gen:
    print(i, end = ' ')