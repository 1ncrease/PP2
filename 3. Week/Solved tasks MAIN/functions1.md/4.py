def filter_prime(a):
    m = 1
    for i in range(2,a):
        if(a%i==0):
            m=0
    if(m==1):
        print(a, end=" ")

list = input().split()
for i in range(len(list)):
    filter_prime(int(list[i]))