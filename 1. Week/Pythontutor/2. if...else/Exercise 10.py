a, b, c, d = int(input()), int(input()), int(input()), int(input())
if abs(a - c) <= 1 and abs(b - d) <= 1:
    print ('YES')
elif abs(a - c) == abs(b - d):
    print ('YES')
elif (a == c or b == d):
    print ('YES')
else:
    print ('NO')