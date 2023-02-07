a, b = int(input()), int(input())
for i in range(a, b - 1, -1):
    if (i % 2 == 1):
        print(i, end = " ")