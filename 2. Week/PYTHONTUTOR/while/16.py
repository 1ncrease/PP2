k=0
km=0
a=int(input())
n=a
while a!=0:
    if a==n:
        k+=1
        if k>km:
            km=k
    else:
        n=a
        if k>km:
            km=k
        k=1
    a=int(input())
print(km)