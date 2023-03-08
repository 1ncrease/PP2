s = str(input())
l=0
u=0
for i in range(len(s)):
    if s[i].isupper():
        u+=1
    elif s[i].islower():
        l+=1
print("lower:")
print(l)
print("upper")
print(u)