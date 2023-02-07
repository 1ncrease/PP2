string = str(input())
n = int(len(string))
for i in range(n):
    if i % 3 != 0:
        print(string[i], sep='', end='')