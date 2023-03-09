s = input()
cntUP = 0
cntDOWN = 0
for i in range(len(s)):
    if (s[i] > 'A' and s[i] < 'Z'):
        cntUP += 1
    elif (s[i] > 'a' and s[i] < 'z'):
        cntDOWN += 1

print("Number of upper case - ", cntUP)
print("Number of lower case - ", cntDOWN)