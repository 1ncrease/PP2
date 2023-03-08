#пишем число N, нужно вывеси все чисто от 1(возведенные в квадрат) до квадрата н
def square_num(num):
    for i in range(1, num + 1):
        yield pow(i, 2)

num = int(input())
gen = square_num(num)

for i in gen:
    print(i, end = ' ')