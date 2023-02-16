def Bond(a):
    str="False"
    for i in range(len(a)):
        if int(a[i]) == 0 and int(a[i+1]) == 0 and int(a[i+2]) == 7:
            str="True"
    print(str)
a = input().split()
Bond(a)