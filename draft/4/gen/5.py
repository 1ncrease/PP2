#возвращает все число от а до 0
def atonol(num):
    for i in range(num, -1, -1):
        yield i

num = int(input())
gen = atonol(num)

for i in gen:
    print(i)