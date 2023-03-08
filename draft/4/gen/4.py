#квадрат всех чисел от а до б

def atob(a, b):
    for i in range(a, b + 1):
        yield pow(i, 2)

a, b = int(input()), int(input())
gen = atob(a, b)

for i in gen:
    print(i)