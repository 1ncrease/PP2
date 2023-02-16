def uniq(a):

    for i in range(len(a)):
        str = "True"
        for j in range(i,len(a)):
            if int(a[i])==int(a[j]) and i != j:
                str="False"
        if(str=="True"):
            print(int(a[i]))
a = input().split()
uniq(a)