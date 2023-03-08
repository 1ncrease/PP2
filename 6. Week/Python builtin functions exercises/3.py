def isp(s):
    k = 0
    r = s[::-1]
    for i in range(len(s)):
        if s[i] != r[i]:
            k += 1
    if k>= 1:
        return False
    else:
        return True
s = str(input())
if isp(s):
    print("palindrome")
else:
    print("not")