x = int(input())
max1 = 0
max2 = 0
while x != 0:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
    x = int(input())
print(max2)