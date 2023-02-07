s=input()
c=s.count('f')
if c==1:
    print('-1')
elif c==0:
    print('-2')
else:
    i1=s.index('f')
    for i in range(i1+1,len(s)):
        if s[i]=='f':
            print(i)
            break