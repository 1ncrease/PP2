#выводит цифры, которые деляться на 3 и 4 от 0 до N 

def trii4etiri(num):
    for i in range(1, num + 1):
        if(i % 3 == 0 and i % 4 == 0):
            yield i

num = int(input())
gen = trii4etiri(num)

for i in gen:
    print(i)