a, b, c, d = input(), input(), input(), input()

if abs(ord(a) - ord(c)) == 2 and abs(ord(b) - ord(d)) == 1:
    print("YES")
elif abs(ord(a) - ord(c)) == 1 and abs(ord(b) - ord(d)) == 2:
    print("YES")
else:
    print("NO")