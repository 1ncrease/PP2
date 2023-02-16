def next3(a):
    str="False"
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            str="True"
    print(str)
a = input().split()
next3(a)